from ctypes import c_void_p

from .dll_handle import DllHandle
from .error import Error


class ComplexObject:
    def __init__(self, dll_handle: DllHandle, impl: c_void_p):
        self._dll_handle = dll_handle
        self.__impl = impl.value

    def __get_impl(self):
        if self.__impl is None:
            raise Error(0x0563958d, "Using of deleted object")
        return c_void_p(self.__impl)

    _impl = property(fget=__get_impl)

    def __del__(self):
        self._dll_handle.apiObject_destructor(
            c_void_p(self.__impl)
        )
