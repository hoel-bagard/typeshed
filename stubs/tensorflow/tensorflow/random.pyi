from collections.abc import Sequence
from enum import Enum
from typing import Generic, Literal, TypeAlias, TypeVar

import tensorflow as tf
from tensorflow._aliases import DTypeLike, ScalarTensorCompatible, ShapeLike
from tensorflow.python.trackable import autotrackable

_STATE_TYPE = TypeVar("_STATE_TYPE")
_State: TypeAlias = Sequence[_STATE_TYPE]

class Algorithm(Enum):
    PHILOX = 1
    THREEFRY = 2
    AUTO_SELECT = 3

class Generator(autotrackable.AutoTrackable, Generic[_STATE_TYPE]):
    @classmethod
    def from_state(
        cls, state: _State[_STATE_TYPE], alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_seed(
        cls, seed: int, alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_non_deterministic_state(
        cls, alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_key_counter(
        cls,
        key: _STATE_TYPE,
        counter: Sequence[_STATE_TYPE],
        alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None,
    ) -> Generator[_STATE_TYPE]: ...
    def __init__(
        self,
        copy_from: Generator[_STATE_TYPE] | None = None,
        state: _State[_STATE_TYPE] | None = None,
        alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None,
    ) -> None: ...
    def reset(self, state: _State[_STATE_TYPE]) -> None: ...
    def reset_from_seed(self, seed: int) -> None: ...
    def reset_from_key_counter(self, key: _STATE_TYPE, counter: Sequence[_STATE_TYPE]) -> None: ...
    @property
    def state(self): ...
    @property
    def algorithm(self): ...
    @property
    def key(self): ...
    def skip(self, delta: int): ...
    def normal(
        self,
        mean: ScalarTensorCompatible = 0.0,
        stddev: ScalarTensorCompatible = 1.0,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def truncated_normal(
        self,
        shape: ShapeLike,
        mean: ScalarTensorCompatible = 0.0,
        stddev: ScalarTensorCompatible = 1.0,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def uniform(
        self,
        shape: ShapeLike,
        minval: ScalarTensorCompatible = 0.0,
        maxval: ScalarTensorCompatible | None = None,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def uniform_full_int(self, shape: ShapeLike, dtype: DTypeLike = ..., name: str | None = None): ...
    def binomial(self, shape: ShapeLike, counts, probs, dtype: DTypeLike = ..., name: str | None = None): ...
    def make_seeds(self, count: int = 1): ...
    def split(self, count: int = 1): ...

def uniform(
    shape: ShapeLike,
    minval: ScalarTensorCompatible = 0.0,
    maxval: ScalarTensorCompatible | None = None,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_uniform(
    shape: ShapeLike,
    seed: tuple[int, int],
    minval: ScalarTensorCompatible = 0.0,
    maxval: ScalarTensorCompatible | None = None,
    dtype: DTypeLike = ...,
    name: str | None = None,
    alg: Literal["philox", "auto_select", "threefry"] = "auto_select",
) -> tf.Tensor: ...
def normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def truncated_normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def poisson(
    shape: ShapeLike, lam: ScalarTensorCompatible = 1.0, dtype: DTypeLike = ..., seed: int | None = None, name: str | None = None
) -> tf.Tensor: ...
def shuffle(value: tf.Tensor, seed: int | None = None, name: str | None = None) -> tf.Tensor: ...
def set_seed(seed: int) -> None: ...
