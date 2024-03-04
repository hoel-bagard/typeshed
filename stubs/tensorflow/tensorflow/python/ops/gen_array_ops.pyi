from collections.abc import Sequence
from typing_extensions import TypeAlias

from tensorflow import Operation, Tensor
from tensorflow._aliases import FloatArray

# str is not a valid input type.
_AssertInputFloat: TypeAlias = FloatArray | Tensor | float | complex | Sequence[_AssertInputFloat]

def check_numerics(tensor: _AssertInputFloat, message: str, name: str | None = None) -> Operation | None: ...
