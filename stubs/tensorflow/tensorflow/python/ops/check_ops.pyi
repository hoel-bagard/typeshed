from collections.abc import Iterable, Sequence
from typing import Any, TypeVar
from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt
from tensorflow import DType, Operation, Tensor, TensorCompatible
from tensorflow._aliases import AnyArray, FloatArray, ShapeLike

# str is not a valid input type.
_AssertInput: TypeAlias = AnyArray | Tensor | float | int | Sequence[str] | Sequence[_AssertInput]
_AssertInputT = TypeVar("_AssertInputT", AnyArray, Tensor, float, int, Sequence[str], Sequence[_AssertInput])
_AssertInputFloat: TypeAlias = FloatArray | Tensor | float | complex | Sequence[_AssertInputFloat]
_AssertInputFloatT = TypeVar("_AssertInputFloatT", FloatArray, Tensor, float, complex, Sequence[_AssertInputFloat])

def assert_equal_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_greater_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_greater_equal_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_integer_v2(x: object, message: str | None = None, name: str | None = None) -> Operation | None: ...
def assert_less_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_less_equal_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_near_v2(
    x: _AssertInputFloatT,
    y: _AssertInputFloatT,
    rtol: _AssertInputFloatT | None = None,
    atol: _AssertInputFloatT | None = None,
    message: str | None = None,
    summarize: int | None = None,
    name: str | None = None,
) -> Operation | None: ...
def assert_negative_v2(
    x: _AssertInput, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_non_negative_v2(
    x: _AssertInput, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_non_positive_v2(
    x: _AssertInput, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_none_equal_v2(
    x: _AssertInputT, y: _AssertInputT, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_positive_v2(
    x: _AssertInput, message: str | None = None, summarize: int | None = None, name: str | None = None
) -> Operation | None: ...
def assert_proper_iterable(values: Iterable[Any]) -> Operation | None: ...
def assert_rank_v2(
    x: TensorCompatible, rank: int | Tensor | npt.NDArray[np.int32], message: str | None = None, name: str | None = None
) -> Operation | None: ...
def assert_rank_at_least_v2(
    x: TensorCompatible, rank: int | Tensor | npt.NDArray[np.int32], message: str | None = None, name: str | None = None
) -> Operation | None: ...
def assert_rank_in_v2(
    x: TensorCompatible,
    rank: Iterable[int | Tensor | npt.NDArray[np.int32]] | Tensor | npt.NDArray[np.int32],
    message: str | None = None,
    name: str | None = None,
) -> Operation | None: ...
def assert_same_float_dtype(tensors: Iterable[Tensor] | None = None, dtype: DType | None = None) -> Operation | None: ...
def assert_scalar_v2(tensor: str | bytes | complex | Tensor | AnyArray, dtype: DType | None = None) -> Operation | None: ...

# TODO: not sure about the types for the one bellow.
def assert_shapes_v2(
    shapes: dict[Tensor, ShapeLike] | list[tuple[Tensor, ShapeLike]],
    data: Iterable[Tensor] | None = None,
    message: str | None = None,
    summarize: int | None = None,
    name: str | None = None,
) -> Operation | None: ...
def assert_type_v2(tensor: object, tf_type: DType, message: str | None = None, name: str | None = None) -> Operation | None: ...
def is_numeric_tensor(tensor: object) -> bool: ...
