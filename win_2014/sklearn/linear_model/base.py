"""
Generalized Linear models.
"""

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Fabian Pedregosa <fabian.pedregosa@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Vincent Michel <vincent.michel@inria.fr>
#         Peter Prettenhofer <peter.prettenhofer@gmail.com>
#         Mathieu Blondel <mathieu@mblondel.org>
#         Lars Buitinck <L.J.Buitinck@uva.nl>
#
# License: BSD 3 clause

from __future__ import division
from abc import ABCMeta, abstractmethod
import numbers
import warnings

import numpy as np
import scipy.sparse as sp
from scipy import linalg
from scipy import sparse

from ..externals import six
from ..externals.joblib import Parallel, delayed
from ..base import BaseEstimator, ClassifierMixin, RegressorMixin
from ..utils import as_float_array, check_array, check_X_y, deprecated
from ..utils import check_random_state, column_or_1d
from ..utils.extmath import safe_sparse_dot
from ..utils.sparsefuncs import mean_variance_axis, inplace_column_scale
from ..utils.fixes import sparse_lsqr
from ..utils.validation import NotFittedError, check_is_fitted
from ..utils.seq_dataset import ArrayDataset, CSRDataset


###
### TODO: intercept for all models
### We should define a common function to center data instead of
### repeating the same code inside each fit method.

### TODO: bayesian_ridge_regression and bayesian_regression_ard
### should be squashed into its respective objects.

SPARSE_INTERCEPT_DECAY = 0.01
# For sparse data intercept updates are scaled by this decay factor to avoid
# intercept oscillation.


def make_dataset(X, y, sample_weight, random_state=None):
    """Create ``Dataset`` abstraction for sparse and dense inputs.

    This also returns the ``intercept_decay`` which is different
    for sparse datasets.
    """

    rng = check_random_state(random_state)
    # seed should never be 0 in SequentialDataset
    seed = rng.randint(1, np.iinfo(np.int32).max)

    if sp.issparse(X):
        dataset = CSRDataset(X.data, X.indptr, X.indices,
                             y, sample_weight, seed=seed)
        intercept_decay = SPARSE_INTERCEPT_DECAY
    else:
        dataset = ArrayDataset(X, y, sample_weight, seed=seed)
        intercept_decay = 1.0

    return dataset, intercept_decay


def sparse_center_data(X, y, fit_intercept, normalize=False):
    """
    Compute information needed to center data to have mean zero along
    axis 0. Be aware that X will not be centered since it would break
    the sparsity, but will be normalized if asked so.
    """
    if fit_intercept:
        # we might require not to change the csr matrix sometimes
        # store a copy if normalize is True.
        # Change dtype to float64 since mean_variance_axis accepts
        # it that way.
        if sp.isspmatrix(X) and X.getformat() == 'csr':
            X = sp.csr_matrix(X, copy=normalize, dtype=np.float64)
        else:
            X = sp.csc_matrix(X, copy=normalize, dtype=np.float64)

        X_mean, X_var = mean_variance_axis(X, axis=0)
        if normalize:
            # transform variance to std in-place
            # XXX: currently scaled to variance=n_samples to match center_data
            X_var *= X.shape[0]
            X_std = np.sqrt(X_var, X_var)
            del X_var
            X_std[X_std == 0] = 1
            inplace_column_scale(X, 1. / X_std)
        else:
            X_std = np.ones(X.shape[1])
        y_mean = y.mean(axis=0)
        y = y - y_mean
    else:
        X_mean = np.zeros(X.shape[1])
        X_std = np.ones(X.shape[1])
        y_mean = 0. if y.ndim == 1 else np.zeros(y.shape[1], dtype=X.dtype)

    return X, y, X_mean, y_mean, X_std


def center_data(X, y, fit_intercept, normalize=False, copy=True,
                sample_weight=None):
    """
    Centers data to have mean zero along axis 0. This is here because
    nearly all linear models will want their data to be centered.

    If sample_weight is not None, then the weighted mean of X and y
    is zero, and not the mean itself
    """
    X = as_float_array(X, copy)
    if fit_intercept:
        if isinstance(sample_weight, numbers.Number):
            sample_weight = None
        if sp.issparse(X):
            X_mean = np.zeros(X.shape[1])
            X_std = np.ones(X.shape[1])
        else:
            X_mean = np.average(X, axis=0, weights=sample_weight)
            X -= X_mean
            if normalize:
                # XXX: currently scaled to variance=n_samples
                X_std = np.sqrt(np.sum(X ** 2, axis=0))
                X_std[X_std == 0] = 1
                X /= X_std
            else:
                X_std = np.ones(X.shape[1])
        y_mean = np.average(y, axis=0, weights=sample_weight)
        y = y - y_mean
    else:
        X_mean = np.zeros(X.shape[1])
        X_std = np.ones(X.shape[1])
        y_mean = 0. if y.ndim == 1 else np.zeros(y.shape[1], dtype=X.dtype)
    return X, y, X_mean, y_mean, X_std


def _rescale_data(X, y, sample_weight):
    """Rescale data so as to support sample_weight"""
    n_samples = X.shape[0]
    sample_weight = sample_weight * np.ones(n_samples)
    sample_weight = np.sqrt(sample_weight)
    sw_matrix = sparse.dia_matrix((sample_weight, 0),
                                  shape=(n_samples, n_samples))
    X = safe_sparse_dot(sw_matrix, X)
    y = safe_sparse_dot(sw_matrix, y)
    return X, y


class LinearModel(six.with_metaclass(ABCMeta, BaseEstimator)):
    """Base class for Linear Models"""

    @abstractmethod
    def fit(self, X, y):
        """Fit model."""

    @deprecated(" and will be removed in 0.19.")
    def decision_function(self, X):
        """Decision function of the linear model.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = (n_samples, n_features)
            Samples.

        Returns
        -------
        C : array, shape = (n_samples,)
            Returns predicted values.
        """
        return self._decision_function(X)

    def _decision_function(self, X):
        check_is_fitted(self, "coef_")

        X = check_array(X, accept_sparse=['csr', 'csc', 'coo'])
        return safe_sparse_dot(X, self.coef_.T,
                               dense_output=True) + self.intercept_

    def predict(self, X):
        """Predict using the linear model

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = (n_samples, n_features)
            Samples.

        Returns
        -------
        C : array, shape = (n_samples,)
            Returns predicted values.
        """
        return self._decision_function(X)

    _center_data = staticmethod(center_data)

    def _set_intercept(self, X_mean, y_mean, X_std):
        """Set the intercept_
        """
        if self.fit_intercept:
            self.coef_ = self.coef_ / X_std
            self.intercept_ = y_mean - np.dot(X_mean, self.coef_.T)
        else:
            self.intercept_ = 0.


# XXX Should this derive from LinearModel? It should be a mixin, not an ABC.
# Maybe the n_features checking can be moved to LinearModel.
class LinearClassifierMixin(ClassifierMixin):
    """Mixin for linear classifiers.

    Handles prediction for sparse and dense X.
    """

    def decision_function(self, X):
        """Predict confidence scores for samples.

        The confidence score for a sample is the signed distance of that
        sample to the hyperplane.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = (n_samples, n_features)
            Samples.

        Returns
        -------
        array, shape=(n_samples,) if n_classes == 2 else (n_samples, n_classes)
            Confidence scores per (sample, class) combination. In the binary
            case, confidence score for self.classes_[1] where >0 means this
            class would be predicted.
        """
        if not hasattr(self, 'coef_') or self.coef_ is None:
            raise NotFittedError("This %(name)s instance is not fitted "
                                 "yet" % {'name': type(self).__name__})

        X = check_array(X, accept_sparse='csr')

        n_features = self.coef_.shape[1]
        if X.shape[1] != n_features:
            raise ValueError("X has %d features per sample; expecting %d"
                             % (X.shape[1], n_features))

        scores = safe_sparse_dot(X, self.coef_.T,
                                 dense_output=True) + self.intercept_
        return scores.ravel() if scores.shape[1] == 1 else scores

    def predict(self, X):
        """Predict class labels for samples in X.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            Samples.

        Returns
        -------
        C : array, shape = [n_samples]
            Predicted class label per sample.
        """
        scores = self.decision_function(X)
        if len(scores.shape) == 1:
            indices = (scores > 0).astype(np.int)
        else:
            indices = scores.argmax(axis=1)
        return self.classes_[indices]

    def _predict_proba_lr(self, X):
        """Probability estimation for OvR logistic regression.

        Positive class probabilities are computed as
        1. / (1. + np.exp(-self.decision_function(X)));
        multiclass is handled by normalizing that over all classes.
        """
        prob = self.decision_function(X)
        prob *= -1
        np.exp(prob, prob)
        prob += 1
        np.reciprocal(prob, prob)
        if prob.ndim == 1:
            return np.vstack([1 - prob, prob]).T
        else:
            # OvR normalization, like LibLinear's predict_probability
            prob /= prob.sum(axis=1).reshape((prob.shape[0], -1))
            return prob


class SparseCoefMixin(object):
    """Mixin for converting coef_ to and from CSR format.

    L1-regularizing estimators should inherit this.
    """

    def densify(self):
        """Convert coefficient matrix to dense array format.

        Converts the ``coef_`` member (back) to a numpy.ndarray. This is the
        default format of ``coef_`` and is required for fitting, so calling
        this method is only required on models that have previously been
        sparsified; otherwise, it is a no-op.

        Returns
        -------
        self: estimator
        """
        msg = "Estimator, %(name)s, must be fitted before densifying."
        check_is_fitted(self, "coef_", msg=msg)
        if sp.issparse(self.coef_):
            self.coef_ = self.coef_.toarray()
        return self

    def sparsify(self):
        """Convert coefficient matrix to sparse format.

        Converts the ``coef_`` member to a scipy.sparse matrix, which for
        L1-regularized models can be much more memory- and storage-efficient
        than the usual numpy.ndarray representation.

        The ``intercept_`` member is not converted.

        Notes
        -----
        For non-sparse models, i.e. when there are not many zeros in ``coef_``,
        this may actually *increase* memory usage, so use this method with
        care. A rule of thumb is that the number of zero elements, which can
        be computed with ``(coef_ == 0).sum()``, must be more than 50% for this
        to provide significant benefits.

        After calling this method, further fitting with the partial_fit
        method (if any) will not work until you call densify.

        Returns
        -------
        self: estimator
        """
        msg = "Estimator, %(name)s, must be fitted before sparsifying."
        check_is_fitted(self, "coef_", msg=msg)
        self.coef_ = sp.csr_matrix(self.coef_)
        return self


class LinearRegression(LinearModel, RegressorMixin):
    """
    Ordinary least squares Linear Regression.

    Parameters
    ----------
    fit_intercept : boolean, optional
        whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (e.g. data is expected to be already centered).

    normalize : boolean, optional, default False
        If True, the regressors X will be normalized before regression.

    copy_X : boolean, optional, default True
        If True, X will be copied; else, it may be overwritten.

    n_jobs : int, optional, default 1
        The number of jobs to use for the computation.
        If -1 all CPUs are used. This will only provide speedup for
        n_targets > 1 and sufficient large problems.

    Attributes
    ----------
    coef_ : array, shape (n_features, ) or (n_targets, n_features)
        Estimated coefficients for the linear regression problem.
        If multiple targets are passed during the fit (y 2D), this
        is a 2D array of shape (n_targets, n_features), while if only
        one target is passed, this is a 1D array of length n_features.

    intercept_ : array
        Independent term in the linear model.

    Notes
    -----
    From the implementation point of view, this is just plain Ordinary
    Least Squares (scipy.linalg.lstsq) wrapped as a predictor object.

    """

    def __init__(self, fit_intercept=True, normalize=False, copy_X=True,
                 n_jobs=1):
        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.copy_X = copy_X
        self.n_jobs = n_jobs

    def fit(self, X, y, sample_weight=None):
        """
        Fit linear model.

        Parameters
        ----------
        X : numpy array or sparse matrix of shape [n_samples,n_features]
            Training data

        y : numpy array of shape [n_samples, n_targets]
            Target values

        sample_weight : numpy array of shape [n_samples]
            Individual weights for each sample

        Returns
        -------
        self : returns an instance of self.
        """

        n_jobs_ = self.n_jobs
        X, y = check_X_y(X, y, accept_sparse=['csr', 'csc', 'coo'],
                         y_numeric=True, multi_output=True)

        if ((sample_weight is not None) and np.atleast_1d(sample_weight).ndim > 1):
            sample_weight = column_or_1d(sample_weight, warn=True)

        X, y, X_mean, y_mean, X_std = self._center_data(
            X, y, self.fit_intercept, self.normalize, self.copy_X,
            sample_weight=sample_weight)

        if sample_weight is not None:
            # Sample weight can be implemented via a simple rescaling.
            X, y = _rescale_data(X, y, sample_weight)

        if sp.issparse(X):
            if y.ndim < 2:
                out = sparse_lsqr(X, y)
                self.coef_ = out[0]
                self.residues_ = out[3]
            else:
                # sparse_lstsq cannot handle y with shape (M, K)
                outs = Parallel(n_jobs=n_jobs_)(
                    delayed(sparse_lsqr)(X, y[:, j].ravel())
                    for j in range(y.shape[1]))
                self.coef_ = np.vstack(out[0] for out in outs)
                self.residues_ = np.vstack(out[3] for out in outs)
        else:
            self.coef_, self.residues_, self.rank_, self.singular_ = \
                linalg.lstsq(X, y)
            self.coef_ = self.coef_.T

        if y.ndim == 1:
            self.coef_ = np.ravel(self.coef_)
        self._set_intercept(X_mean, y_mean, X_std)
        return self


def _pre_fit(X, y, Xy, precompute, normalize, fit_intercept, copy,
             Xy_precompute_order=None):
    """Aux function used at beginning of fit in linear models"""
    n_samples, n_features = X.shape
    if sparse.isspmatrix(X):
        precompute = False
        X, y, X_mean, y_mean, X_std = sparse_center_data(
            X, y, fit_intercept, normalize)
    else:
        # copy was done in fit if necessary
        X, y, X_mean, y_mean, X_std = center_data(
            X, y, fit_intercept, normalize, copy=copy)
    if hasattr(precompute, '__array__') and (
            fit_intercept and not np.allclose(X_mean, np.zeros(n_features))
            or normalize and not np.allclose(X_std, np.ones(n_features))):
        warnings.warn("Gram matrix was provided but X was centered"
                      " to fit intercept, "
                      "or X was normalized : recomputing Gram matrix.",
                      UserWarning)
        # recompute Gram
        precompute = 'auto'
        Xy = None

    # precompute if n_samples > n_features
    if precompute == 'auto':
        precompute = (n_samples > n_features)

    if precompute is True:
        precompute = np.dot(X.T, X)
        if Xy_precompute_order == 'F':
            precompute = np.dot(X.T, X).T

    if not hasattr(precompute, '__array__'):
        Xy = None  # cannot use Xy if precompute is not Gram

    if hasattr(precompute, '__array__') and Xy is None:
        if Xy_precompute_order == 'F':
            Xy = np.dot(y.T, X).T
        else:
            Xy = np.dot(X.T, y)

    return X, y, X_mean, y_mean, X_std, precompute, Xy
