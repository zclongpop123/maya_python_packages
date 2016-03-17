# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_CGAL_AABB_tree', [dirname(__file__)])
        except ImportError:
            import _CGAL_AABB_tree
            return _CGAL_AABB_tree
        if fp is not None:
            try:
                _mod = imp.load_module('_CGAL_AABB_tree', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _CGAL_AABB_tree = swig_import_helper()
    del swig_import_helper
else:
    import _CGAL_AABB_tree
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import CGAL.CGAL_Kernel
import CGAL.CGAL_Polyhedron_3
class Object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Object()
        try: self.this.append(this)
        except: self.this = this
    def is_Point_2(self): return _CGAL_AABB_tree.Object_is_Point_2(self)
    def get_Point_2(self): return _CGAL_AABB_tree.Object_get_Point_2(self)
    def is_Point_3(self): return _CGAL_AABB_tree.Object_is_Point_3(self)
    def get_Point_3(self): return _CGAL_AABB_tree.Object_get_Point_3(self)
    def is_Triangle_2(self): return _CGAL_AABB_tree.Object_is_Triangle_2(self)
    def get_Triangle_2(self): return _CGAL_AABB_tree.Object_get_Triangle_2(self)
    def is_Triangle_3(self): return _CGAL_AABB_tree.Object_is_Triangle_3(self)
    def get_Triangle_3(self): return _CGAL_AABB_tree.Object_get_Triangle_3(self)
    def is_Segment_3(self): return _CGAL_AABB_tree.Object_is_Segment_3(self)
    def get_Segment_3(self): return _CGAL_AABB_tree.Object_get_Segment_3(self)
    def is_Segment_2(self): return _CGAL_AABB_tree.Object_is_Segment_2(self)
    def get_Segment_2(self): return _CGAL_AABB_tree.Object_get_Segment_2(self)
    def is_Line_3(self): return _CGAL_AABB_tree.Object_is_Line_3(self)
    def get_Line_3(self): return _CGAL_AABB_tree.Object_get_Line_3(self)
    def is_Line_2(self): return _CGAL_AABB_tree.Object_is_Line_2(self)
    def get_Line_2(self): return _CGAL_AABB_tree.Object_get_Line_2(self)
    def is_Plane_3(self): return _CGAL_AABB_tree.Object_is_Plane_3(self)
    def get_Plane_3(self): return _CGAL_AABB_tree.Object_get_Plane_3(self)
    def is_Ray_2(self): return _CGAL_AABB_tree.Object_is_Ray_2(self)
    def get_Ray_2(self): return _CGAL_AABB_tree.Object_get_Ray_2(self)
    def is_Ray_3(self): return _CGAL_AABB_tree.Object_is_Ray_3(self)
    def get_Ray_3(self): return _CGAL_AABB_tree.Object_get_Ray_3(self)
    def empty(self): return _CGAL_AABB_tree.Object_empty(self)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Object
    __del__ = lambda self : None;
Object_swigregister = _CGAL_AABB_tree.Object_swigregister
Object_swigregister(Object)

class Point_and_Polyhedron_3_Facet_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point_and_Polyhedron_3_Facet_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point_and_Polyhedron_3_Facet_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Point_and_Polyhedron_3_Facet_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_first_get, _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_second_get, _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Point_and_Polyhedron_3_Facet_handle
    __del__ = lambda self : None;
Point_and_Polyhedron_3_Facet_handle_swigregister = _CGAL_AABB_tree.Point_and_Polyhedron_3_Facet_handle_swigregister
Point_and_Polyhedron_3_Facet_handle_swigregister(Point_and_Polyhedron_3_Facet_handle)

class Point_and_Polyhedron_3_Halfedge_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point_and_Polyhedron_3_Halfedge_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point_and_Polyhedron_3_Halfedge_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Point_and_Polyhedron_3_Halfedge_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_first_get, _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_second_get, _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Point_and_Polyhedron_3_Halfedge_handle
    __del__ = lambda self : None;
Point_and_Polyhedron_3_Halfedge_handle_swigregister = _CGAL_AABB_tree.Point_and_Polyhedron_3_Halfedge_handle_swigregister
Point_and_Polyhedron_3_Halfedge_handle_swigregister(Point_and_Polyhedron_3_Halfedge_handle)

class Point_and_Integer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point_and_Integer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point_and_Integer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Point_and_Integer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Point_and_Integer_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Point_and_Integer_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Point_and_Integer_first_get, _CGAL_AABB_tree.Point_and_Integer_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Point_and_Integer_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Point_and_Integer_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Point_and_Integer_second_get, _CGAL_AABB_tree.Point_and_Integer_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Point_and_Integer
    __del__ = lambda self : None;
Point_and_Integer_swigregister = _CGAL_AABB_tree.Point_and_Integer_swigregister
Point_and_Integer_swigregister(Point_and_Integer)

class Object_and_Polyhedron_3_Facet_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object_and_Polyhedron_3_Facet_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object_and_Polyhedron_3_Facet_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Object_and_Polyhedron_3_Facet_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_first_get, _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_second_get, _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Object_and_Polyhedron_3_Facet_handle
    __del__ = lambda self : None;
Object_and_Polyhedron_3_Facet_handle_swigregister = _CGAL_AABB_tree.Object_and_Polyhedron_3_Facet_handle_swigregister
Object_and_Polyhedron_3_Facet_handle_swigregister(Object_and_Polyhedron_3_Facet_handle)

class Object_and_Polyhedron_3_Halfedge_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object_and_Polyhedron_3_Halfedge_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object_and_Polyhedron_3_Halfedge_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Object_and_Polyhedron_3_Halfedge_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_first_get, _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_second_get, _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Object_and_Polyhedron_3_Halfedge_handle
    __del__ = lambda self : None;
Object_and_Polyhedron_3_Halfedge_handle_swigregister = _CGAL_AABB_tree.Object_and_Polyhedron_3_Halfedge_handle_swigregister
Object_and_Polyhedron_3_Halfedge_handle_swigregister(Object_and_Polyhedron_3_Halfedge_handle)

class Object_and_Integer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object_and_Integer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object_and_Integer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_Object_and_Integer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _CGAL_AABB_tree.Object_and_Integer_first_set
    __swig_getmethods__["first"] = _CGAL_AABB_tree.Object_and_Integer_first_get
    if _newclass:first = _swig_property(_CGAL_AABB_tree.Object_and_Integer_first_get, _CGAL_AABB_tree.Object_and_Integer_first_set)
    __swig_setmethods__["second"] = _CGAL_AABB_tree.Object_and_Integer_second_set
    __swig_getmethods__["second"] = _CGAL_AABB_tree.Object_and_Integer_second_get
    if _newclass:second = _swig_property(_CGAL_AABB_tree.Object_and_Integer_second_get, _CGAL_AABB_tree.Object_and_Integer_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _CGAL_AABB_tree.delete_Object_and_Integer
    __del__ = lambda self : None;
Object_and_Integer_swigregister = _CGAL_AABB_tree.Object_and_Integer_swigregister
Object_and_Integer_swigregister(Object_and_Integer)

class Optional_Polyhedron_3_Halfedge_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Polyhedron_3_Halfedge_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Polyhedron_3_Halfedge_handle, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Polyhedron_3_Halfedge_handle()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Polyhedron_3_Halfedge_handle_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Polyhedron_3_Halfedge_handle_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Polyhedron_3_Halfedge_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Polyhedron_3_Halfedge_handle
    __del__ = lambda self : None;
Optional_Polyhedron_3_Halfedge_handle_swigregister = _CGAL_AABB_tree.Optional_Polyhedron_3_Halfedge_handle_swigregister
Optional_Polyhedron_3_Halfedge_handle_swigregister(Optional_Polyhedron_3_Halfedge_handle)

class Optional_Polyhedron_3_Facet_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Polyhedron_3_Facet_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Polyhedron_3_Facet_handle, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Polyhedron_3_Facet_handle()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Polyhedron_3_Facet_handle_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Polyhedron_3_Facet_handle_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Polyhedron_3_Facet_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Polyhedron_3_Facet_handle
    __del__ = lambda self : None;
Optional_Polyhedron_3_Facet_handle_swigregister = _CGAL_AABB_tree.Optional_Polyhedron_3_Facet_handle_swigregister
Optional_Polyhedron_3_Facet_handle_swigregister(Optional_Polyhedron_3_Facet_handle)

class Optional_Integer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Integer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Integer, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Integer()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Integer_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Integer_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Integer_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Integer
    __del__ = lambda self : None;
Optional_Integer_swigregister = _CGAL_AABB_tree.Optional_Integer_swigregister
Optional_Integer_swigregister(Optional_Integer)

class Optional_Object_and_Polyhedron_3_Halfedge_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Object_and_Polyhedron_3_Halfedge_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Object_and_Polyhedron_3_Halfedge_handle, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Object_and_Polyhedron_3_Halfedge_handle()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Halfedge_handle_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Halfedge_handle_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Halfedge_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Object_and_Polyhedron_3_Halfedge_handle
    __del__ = lambda self : None;
Optional_Object_and_Polyhedron_3_Halfedge_handle_swigregister = _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Halfedge_handle_swigregister
Optional_Object_and_Polyhedron_3_Halfedge_handle_swigregister(Optional_Object_and_Polyhedron_3_Halfedge_handle)

class Optional_Object_and_Polyhedron_3_Facet_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Object_and_Polyhedron_3_Facet_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Object_and_Polyhedron_3_Facet_handle, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Object_and_Polyhedron_3_Facet_handle()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Facet_handle_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Facet_handle_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Facet_handle_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Object_and_Polyhedron_3_Facet_handle
    __del__ = lambda self : None;
Optional_Object_and_Polyhedron_3_Facet_handle_swigregister = _CGAL_AABB_tree.Optional_Object_and_Polyhedron_3_Facet_handle_swigregister
Optional_Object_and_Polyhedron_3_Facet_handle_swigregister(Optional_Object_and_Polyhedron_3_Facet_handle)

class Optional_Object_and_Integer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Optional_Object_and_Integer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Optional_Object_and_Integer, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _CGAL_AABB_tree.new_Optional_Object_and_Integer()
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _CGAL_AABB_tree.Optional_Object_and_Integer_empty(self)
    def value(self): return _CGAL_AABB_tree.Optional_Object_and_Integer_value(self)
    def deepcopy(self, *args): return _CGAL_AABB_tree.Optional_Object_and_Integer_deepcopy(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_Optional_Object_and_Integer
    __del__ = lambda self : None;
Optional_Object_and_Integer_swigregister = _CGAL_AABB_tree.Optional_Object_and_Integer_swigregister
Optional_Object_and_Integer_swigregister(Optional_Object_and_Integer)

class AABB_tree_Polyhedron_3_Facet_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AABB_tree_Polyhedron_3_Facet_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AABB_tree_Polyhedron_3_Facet_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_AABB_tree_Polyhedron_3_Facet_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    def rebuild(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_rebuild(self, *args)
    def clear(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_clear(self)
    def size(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_size(self)
    def empty(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_empty(self)
    def do_intersect(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_do_intersect(self, *args)
    def number_of_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_number_of_intersected_primitives(self, *args)
    def all_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_all_intersected_primitives(self, *args)
    def any_intersected_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_any_intersected_primitive(self, *args)
    def any_intersection(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_any_intersection(self, *args)
    def all_intersections(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_all_intersections(self, *args)
    def squared_distance(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_squared_distance(self, *args)
    def closest_point(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_closest_point(self, *args)
    def closest_point_and_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_closest_point_and_primitive(self, *args)
    def accelerate_distance_queries(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_accelerate_distance_queries(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_AABB_tree_Polyhedron_3_Facet_handle
    __del__ = lambda self : None;
AABB_tree_Polyhedron_3_Facet_handle_swigregister = _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Facet_handle_swigregister
AABB_tree_Polyhedron_3_Facet_handle_swigregister(AABB_tree_Polyhedron_3_Facet_handle)

class AABB_tree_Polyhedron_3_Halfedge_handle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AABB_tree_Polyhedron_3_Halfedge_handle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AABB_tree_Polyhedron_3_Halfedge_handle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_AABB_tree_Polyhedron_3_Halfedge_handle(*args)
        try: self.this.append(this)
        except: self.this = this
    def rebuild(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_rebuild(self, *args)
    def clear(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_clear(self)
    def size(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_size(self)
    def empty(self): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_empty(self)
    def do_intersect(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_do_intersect(self, *args)
    def number_of_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_number_of_intersected_primitives(self, *args)
    def all_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_all_intersected_primitives(self, *args)
    def any_intersected_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_any_intersected_primitive(self, *args)
    def any_intersection(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_any_intersection(self, *args)
    def all_intersections(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_all_intersections(self, *args)
    def squared_distance(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_squared_distance(self, *args)
    def closest_point(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_closest_point(self, *args)
    def closest_point_and_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_closest_point_and_primitive(self, *args)
    def accelerate_distance_queries(self, *args): return _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_accelerate_distance_queries(self, *args)
    __swig_destroy__ = _CGAL_AABB_tree.delete_AABB_tree_Polyhedron_3_Halfedge_handle
    __del__ = lambda self : None;
AABB_tree_Polyhedron_3_Halfedge_handle_swigregister = _CGAL_AABB_tree.AABB_tree_Polyhedron_3_Halfedge_handle_swigregister
AABB_tree_Polyhedron_3_Halfedge_handle_swigregister(AABB_tree_Polyhedron_3_Halfedge_handle)

class AABB_tree_Segment_3_soup(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AABB_tree_Segment_3_soup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AABB_tree_Segment_3_soup, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_AABB_tree_Segment_3_soup(*args)
        try: self.this.append(this)
        except: self.this = this
    def rebuild(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_rebuild(self, *args)
    def clear(self): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_clear(self)
    def size(self): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_size(self)
    def empty(self): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_empty(self)
    def do_intersect(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_do_intersect(self, *args)
    def number_of_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_number_of_intersected_primitives(self, *args)
    def all_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_all_intersected_primitives(self, *args)
    def any_intersected_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_any_intersected_primitive(self, *args)
    def any_intersection(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_any_intersection(self, *args)
    def all_intersections(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_all_intersections(self, *args)
    def squared_distance(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_squared_distance(self, *args)
    def closest_point(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_closest_point(self, *args)
    def closest_point_and_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_closest_point_and_primitive(self, *args)
    def accelerate_distance_queries(self, *args): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_accelerate_distance_queries(self, *args)
    def reset_id(self): return _CGAL_AABB_tree.AABB_tree_Segment_3_soup_reset_id(self)
    __swig_destroy__ = _CGAL_AABB_tree.delete_AABB_tree_Segment_3_soup
    __del__ = lambda self : None;
AABB_tree_Segment_3_soup_swigregister = _CGAL_AABB_tree.AABB_tree_Segment_3_soup_swigregister
AABB_tree_Segment_3_soup_swigregister(AABB_tree_Segment_3_soup)

class AABB_tree_Triangle_3_soup(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AABB_tree_Triangle_3_soup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AABB_tree_Triangle_3_soup, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _CGAL_AABB_tree.new_AABB_tree_Triangle_3_soup(*args)
        try: self.this.append(this)
        except: self.this = this
    def rebuild(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_rebuild(self, *args)
    def clear(self): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_clear(self)
    def size(self): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_size(self)
    def empty(self): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_empty(self)
    def do_intersect(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_do_intersect(self, *args)
    def number_of_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_number_of_intersected_primitives(self, *args)
    def all_intersected_primitives(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_all_intersected_primitives(self, *args)
    def any_intersected_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_any_intersected_primitive(self, *args)
    def any_intersection(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_any_intersection(self, *args)
    def all_intersections(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_all_intersections(self, *args)
    def squared_distance(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_squared_distance(self, *args)
    def closest_point(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_closest_point(self, *args)
    def closest_point_and_primitive(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_closest_point_and_primitive(self, *args)
    def accelerate_distance_queries(self, *args): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_accelerate_distance_queries(self, *args)
    def reset_id(self): return _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_reset_id(self)
    __swig_destroy__ = _CGAL_AABB_tree.delete_AABB_tree_Triangle_3_soup
    __del__ = lambda self : None;
AABB_tree_Triangle_3_soup_swigregister = _CGAL_AABB_tree.AABB_tree_Triangle_3_soup_swigregister
AABB_tree_Triangle_3_soup_swigregister(AABB_tree_Triangle_3_soup)

# This file is compatible with both classic and new-style classes.


