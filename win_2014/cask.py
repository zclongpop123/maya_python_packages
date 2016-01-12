from __future__ import absolute_import, division, print_function, unicode_literals

import sys

from injector import Injector
from six import reraise

__version__ = '0.1.1'
__all__ = ('Cask',)


class RunMainDescriptor(object):
    def __get__(self, instance, owner):
        if instance is None:
            return owner._class_run_main
        else:
            return instance._instance_run_main


class Cask(object):
    run_main = RunMainDescriptor()

    def __init__(self, target=None, injector=None, modules=()):
        '''
        :type target: main application callable
        :type modules: iterable of :class:`injector.Module`
        :type injector: :class:`injector.Injector`
        '''
        self._modules = list(modules)
        self._injector = injector
        self._target = target

        self._before_main_funcs = []
        self._after_main_funcs = []
        self._exception_handlers = []

    def module(self, m):
        self._modules.append(m)
        return m

    def exception_handler(self, exception_class):
        def decorator(f):
            self._exception_handlers.append((exception_class, f))
            return f

        return decorator

    def before_main(self, f):
        self._before_main_funcs.append(f)
        return f

    def after_main(self, f):
        self._after_main_funcs.append(f)
        return f

    def _call(self, f):
        return self._injector.call_with_injection(callable=f, self_=None)

    def _instance_run_main(self, f=None):
        if f.__module__ == '__main__':
            self._target = f or self._target
            self.run()

        return f

    @classmethod
    def _class_run_main(cls, **kwargs):
        def decorator(func):
            if func.__module__ == '__main__':
                cli = cls(target=func, **kwargs)
                cli.run()

            return func

        return decorator

    def main(self, f):
        self._target = f
        return f

    def _init_injection(self):
        self._injector = Injector(self._modules)
        self._injector.install_into(self)

    def run(self):
        """ Call to run the application. """

        try:
            self._init_injection()
            result = self._run_before_main()
            if not result:
                result = self._call(self._target)
            self._run_after_main(result)
        except Exception as e:
            self._handle_exception(e)

    def _run_before_main(self):
        for f in self._before_main_funcs:
            result = self._call(f)
            if result:
                return result

        return None

    def _run_after_main(self, result):
        for f in self._after_main_funcs:
            result = f(result)
        return result

    def _handle_exception(self, e):
        for exception_class, handler in self._exception_handlers:
            if isinstance(e, exception_class):
                handler(e)
                return

        reraise(*sys.exc_info())
