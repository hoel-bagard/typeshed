from collections.abc import Callable, Iterable, Mapping
from typing import Any, Concatenate, ParamSpec, TypeVar, overload

from behave.runner import Context

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_P = ParamSpec("_P")

# Type aliases for fixture registry
_FixtureFunc = Callable[..., _T]
_FixtureData = _FixtureFunc[_T] | tuple[_FixtureFunc[_T], tuple[Any, ...], dict[str, Any]]
_FixtureRegistry = Mapping[str, _FixtureData[Any]]
_FixtureCallParams = tuple[_FixtureFunc[_T], tuple[Any, ...], dict[str, Any]]

class InvalidFixtureError(RuntimeError): ...

def use_fixture(
    fixture_func: Callable[Concatenate[Context, _P], _T],
    context: Context,
    *fixture_args: _P.args,
    **fixture_kwargs: _P.kwargs,
) -> _T: ...
def use_fixture_by_tag(tag: str, context: Context, fixture_registry: _FixtureRegistry) -> Any: ...
def fixture_call_params(fixture_func: Callable[..., _T], *args: Any, **kwargs: Any) -> _FixtureCallParams[_T]: ...
def use_composite_fixture_with(context: Context, fixture_funcs_with_params: Iterable[_FixtureCallParams[Any]]) -> list[Any]: ...

# fixture decorator overloads
@overload
def fixture(func: _F) -> _F: ...
@overload
def fixture(func: None = None, name: str | None = None, pattern: str | None = None) -> Callable[[_F], _F]: ...
