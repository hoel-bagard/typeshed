# Note: these stubs are incomplete. The more complex type
# signatures are currently omitted.

from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import SupportsFloat, overload

__all__ = ["Number", "Complex", "Real", "Rational", "Integral"]

class Number(metaclass=ABCMeta):
    @abstractmethod
    def __hash__(self) -> int: ...

class Complex(Number):
    @abstractmethod
    def __complex__(self) -> complex: ...
    def __bool__(self) -> bool: ...
    @property
    @abstractmethod
    def real(self): ...
    @property
    @abstractmethod
    def imag(self): ...
    @abstractmethod
    def __add__(self, other): ...
    @abstractmethod
    def __radd__(self, other): ...
    @abstractmethod
    def __neg__(self): ...
    @abstractmethod
    def __pos__(self): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    @abstractmethod
    def __mul__(self, other): ...
    @abstractmethod
    def __rmul__(self, other): ...
    @abstractmethod
    def __truediv__(self, other): ...
    @abstractmethod
    def __rtruediv__(self, other): ...
    @abstractmethod
    def __pow__(self, exponent): ...
    @abstractmethod
    def __rpow__(self, base): ...
    @abstractmethod
    def __abs__(self) -> Real: ...
    @abstractmethod
    def conjugate(self): ...
    @abstractmethod
    def __eq__(self, other: object) -> bool: ...

class Real(Complex, SupportsFloat):
    @abstractmethod
    def __float__(self) -> float: ...
    @abstractmethod
    def __trunc__(self) -> int: ...
    @abstractmethod
    def __floor__(self) -> int: ...
    @abstractmethod
    def __ceil__(self) -> int: ...
    @abstractmethod
    @overload
    def __round__(self, ndigits: None = None) -> int: ...
    @abstractmethod
    @overload
    def __round__(self, ndigits: int): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    @abstractmethod
    def __floordiv__(self, other) -> int: ...
    @abstractmethod
    def __rfloordiv__(self, other) -> int: ...
    @abstractmethod
    def __mod__(self, other): ...
    @abstractmethod
    def __rmod__(self, other): ...
    @abstractmethod
    def __lt__(self, other) -> bool: ...
    @abstractmethod
    def __le__(self, other) -> bool: ...
    def __complex__(self) -> complex: ...
    @property
    def real(self): ...
    @property
    def imag(self): ...
    def conjugate(self): ...

class Rational(Real):
    @property
    @abstractmethod
    def numerator(self) -> int: ...
    @property
    @abstractmethod
    def denominator(self) -> int: ...
    def __float__(self) -> float: ...

class Integral(Rational):
    @abstractmethod
    def __int__(self) -> int: ...
    def __index__(self) -> int: ...
    @abstractmethod
    def __pow__(self, exponent, modulus: Incomplete | None = None): ...
    @abstractmethod
    def __lshift__(self, other): ...
    @abstractmethod
    def __rlshift__(self, other): ...
    @abstractmethod
    def __rshift__(self, other): ...
    @abstractmethod
    def __rrshift__(self, other): ...
    @abstractmethod
    def __and__(self, other): ...
    @abstractmethod
    def __rand__(self, other): ...
    @abstractmethod
    def __xor__(self, other): ...
    @abstractmethod
    def __rxor__(self, other): ...
    @abstractmethod
    def __or__(self, other): ...
    @abstractmethod
    def __ror__(self, other): ...
    @abstractmethod
    def __invert__(self): ...
    def __float__(self) -> float: ...
    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...
