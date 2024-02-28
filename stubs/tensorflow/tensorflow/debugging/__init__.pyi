from collections.abc import Sequence
from typing import TypeVar
from typing_extensions import TypeAlias

from tensorflow import IndexedSlices, Operation, Tensor, TensorCompatible
from tensorflow._aliases import AnyArray, FloatArray, FloatDataSequence
from tensorflow.debugging import experimental as experimental

# str is not a valid input type.
_AssertInput: TypeAlias = AnyArray | Tensor | float | int | Sequence[str] | Sequence[_AssertInput]
_AssertInputT = TypeVar("_AssertInputT", AnyArray, Tensor, float, int, Sequence[str], Sequence[_AssertInput])

class Assert:
    def __init__(
        self, condition: TensorCompatible, data: Tensor, summarize: int | None = None, name: str | None = None
    ) -> None: ...

def assert_all_finite(
    x: Tensor | FloatArray | FloatDataSequence | IndexedSlices, message: str, name: str | None = None
) -> Tensor: ...
def assert_equal(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_greater(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_greater_equal(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_integer(


def assert_less(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_less_equal(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_positive(
    x: TensorCompatible, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_negative(
    x: TensorCompatible, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_non_positive(
    x: TensorCompatible, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_non_negative(
    x: TensorCompatible, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...

def disable_traceback_filtering() -> None: ...
def enable_traceback_filtering() -> None: ...
def enable_check_numerics(stack_height_limit: int = 30, path_length_limit: int = 50) -> None: ...
def disable_check_numerics() -> None: ...
