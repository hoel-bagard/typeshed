from collections.abc import Callable, Iterable
from datetime import date, datetime, timedelta
from time import _TimeTuple, struct_time
from typing import Any, Generic, NamedTuple, TypeVar, overload
from typing_extensions import TypeAlias

from webob.byterange import ContentRange, Range
from webob.etag import IfRange, IfRangeDate

_T = TypeVar("_T")
_DefaultT = TypeVar("_DefaultT")
_GetterReturnType = TypeVar("_GetterReturnType")
_SetterValueType = TypeVar("_SetterValueType")
_ConvertedGetterReturnType = TypeVar("_ConvertedGetterReturnType")
_ConvertedSetterValueType = TypeVar("_ConvertedSetterValueType")
_ContentRangeParams: TypeAlias = (
    ContentRange
    | list[int]
    | list[None]
    | list[int | None]
    | tuple[int, int]
    | tuple[None, None]
    | tuple[int, int, int | None]
    | tuple[None, None, int | None]
    | str
    | None
)

class _AsymmetricProperty(Generic[_GetterReturnType, _SetterValueType]):
    @overload
    def __get__(self, __obj: None, __type: type | None = ...) -> property: ...
    @overload
    def __get__(self, __obj: Any, __type: type | None = ...) -> _GetterReturnType: ...
    def __set__(self, __obj: Any, __value: _SetterValueType) -> None: ...

class _AsymmetricPropertyWithDelete(_AsymmetricProperty[_GetterReturnType, _SetterValueType]):
    def __delete__(self, __obj: Any) -> None: ...

class _SymmetricProperty(_AsymmetricProperty[_T, _T]): ...
class _SymmetricPropertyWithDelete(_AsymmetricPropertyWithDelete[_T, _T]): ...
class _StringProperty(_SymmetricPropertyWithDelete[str | None]): ...
class _ListProperty(_AsymmetricPropertyWithDelete[tuple[str, ...] | None, Iterable[str] | str | None]): ...
class _DateProperty(
    _AsymmetricPropertyWithDelete[datetime | None, date | datetime | timedelta | _TimeTuple | struct_time | float | str | None]
): ...

@overload
def environ_getter(key: str, default: None, rfc_section: str | None = None) -> _SymmetricPropertyWithDelete[Any | None]: ...
@overload
def environ_getter(
    key: str, default: _DefaultT, rfc_section: str | None = None
) -> _AsymmetricPropertyWithDelete[Any | _DefaultT, Any | _DefaultT | None]: ...
@overload
def environ_getter(key: str, *, rfc_section: str | None = None) -> _SymmetricProperty[Any]: ...
@overload
def environ_decoder(
    key: str, default: str, rfc_section: str | None = None, encattr: str | None = None
) -> _AsymmetricPropertyWithDelete[str, str | None]: ...
@overload
def environ_decoder(
    key: str, default: None, rfc_section: str | None = None, encattr: str | None = None
) -> _SymmetricPropertyWithDelete[str | None]: ...
@overload
def environ_decoder(key: str, *, rfc_section: str | None = None, encattr: str | None = None) -> _SymmetricProperty[str]: ...
def upath_property(key: str) -> _SymmetricProperty[str]: ...
def deprecated_property(attr: _T, name: str, text: str, version: str) -> _T: ...
def header_getter(header: str, rfc_section: str) -> _StringProperty: ...
@overload
def converter(
    prop: _AsymmetricPropertyWithDelete[_GetterReturnType, _SetterValueType],
    parse: Callable[[_GetterReturnType], _ConvertedGetterReturnType],
    serialize: Callable[[_ConvertedSetterValueType], _SetterValueType],
    convert_name: str | None = None,
) -> _AsymmetricPropertyWithDelete[_ConvertedGetterReturnType, _ConvertedSetterValueType]: ...
@overload
def converter(
    prop: _AsymmetricProperty[_GetterReturnType, _SetterValueType],
    parse: Callable[[_GetterReturnType], _ConvertedGetterReturnType],
    serialize: Callable[[_ConvertedSetterValueType], _SetterValueType],
    convert_name: str | None = None,
) -> _AsymmetricProperty[_ConvertedGetterReturnType, _ConvertedSetterValueType]: ...
def list_header(header: str, rfc_section: str) -> _ListProperty: ...
def parse_list(value: str | None) -> tuple[str, ...] | None: ...
def serialize_list(value: Iterable[str] | str) -> str: ...
def converter_date(prop: _StringProperty) -> _DateProperty: ...
def date_header(header: str, rfc_section: str) -> _DateProperty: ...
def parse_etag_response(value: str | None, strong: bool = False) -> str | None: ...
def serialize_etag_response(value: str | tuple[str, bool]) -> str: ...
def serialize_if_range(value: IfRange | IfRangeDate | datetime | date | str) -> str | None: ...
def parse_range(value: str | None) -> Range | None: ...
def serialize_range(value: tuple[int, int | None] | list[int | None] | list[int] | str | None) -> str | None: ...
def parse_int(value: str | None) -> int | None: ...
def parse_int_safe(value: str | None) -> int | None: ...

serialize_int: Callable[[int], str]

def parse_content_range(value: str | None) -> ContentRange | None: ...
def serialize_content_range(value: _ContentRangeParams) -> str | None: ...
def parse_auth_params(params: str) -> dict[str, str]: ...

known_auth_schemes: dict[str, None]

class _authorization(NamedTuple):
    authtype: str
    params: dict[str, str] | str

def parse_auth(val: str | None) -> _authorization | None: ...
def serialize_auth(val: tuple[str, dict[str, str] | str] | list[Any] | str | None) -> str | None: ...
