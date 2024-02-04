from _typeshed import Incomplete
from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager, contextmanager
from typing import Any, Literal
from typing_extensions import Self

import numpy as np
import numpy.typing as npt
import tensorflow as tf
from tensorflow.experimental.dtensor import Mesh

class SummaryWriter:
    def as_default(self, step: int | None = None) -> AbstractContextManager[Self]: ...
    def close(): ...
    def flush() -> None: ...
    def init() -> None: ...
    def set_as_default(self, step: int | None = None) -> None: ...

def audio(
    name: str,
    data: tf.Tensor,
    sample_rate: int | tf.Tensor,
    step: int | tf.Tensor | None = None,
    max_outputs: int | tf.Tensor | None = 3,
    encoding: Literal["wav"] | None = None,
    description: str | None = None,
) -> bool: ...
def scalar(name: str, data: float | tf.Tensor, step: int | tf.Tensor | None = None, description: str | None = None) -> bool: ...
def image(
    name: str,
    data: tf.Tensor | npt.NDArray[np.uint8 | np.number[Any]],
    step: int | tf.Tensor | None = None,
    description: str | None = None,
) -> bool: ...
def text(name: str, data: str | tf.Tensor, step: int | tf.Tensor | None = None, description: str | None = None) -> bool: ...
def histogram(
    name: str, data: tf.Tensor, step: int | None = None, buckets: int | None = None, description: str | None = None
) -> bool: ...
def graph(graph_data: tf.Graph | tf.compat.v1.GraphDef) -> bool: ...
@contextmanager
def record_if(condition: bool | tf.Tensor | Callable[[], bool]) -> Iterator[None]: ...
def create_file_writer(
    logdir: str,
    max_queue: int | None = None,
    flush_millis: int | None = None,
    filename_suffix: str | None = None,
    name: str | None = None,
    experimental_trackable: bool = False,
    experimental_mesh: Mesh | None = None,
) -> SummaryWriter: ...
def flush(writer: SummaryWriter | None = None, name: str | None = None) -> tf.Operation: ...
def __getattr__(name: str) -> Incomplete: ...
