from collections.abc import Callable
from typing_extensions import Self

from tensorflow import DType, Tensor
from tensorflow._aliases import ShapeLike
from tensorflow.python.feature_column.feature_column_v2 import SequenceDenseColumn, _ExampleSpec, _FeatureColumn

# Strangely at runtime most of Sequence feature columns are defined in feature_column_v2 except
# for this one.
class SequenceNumericColumn(SequenceDenseColumn):
    key: str
    shape: ShapeLike
    default_value: float
    dtype: DType
    normalizer_fn: Callable[[Tensor], Tensor] | None

    def __new__(
        _cls, key: str, shape: ShapeLike, default_value: float, dtype: DType, normalizer_fn: Callable[[Tensor], Tensor] | None
    ) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[_FeatureColumn | str]: ...
