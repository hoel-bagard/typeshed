from tensorflow import IndexedSlices, Tensor
from tensorflow._aliases import FloatArray, FloatDataSequence

# debugging's assert_all_finite
def verify_tensor_all_finite_v2(
    x: Tensor | FloatArray | FloatDataSequence | IndexedSlices, message: str, name: str | None = None
) -> Tensor: ...
