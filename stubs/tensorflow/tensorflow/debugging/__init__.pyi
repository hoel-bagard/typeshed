# ruff: noqa: F401
from collections.abc import Sequence
from typing import TypeVar
from typing_extensions import TypeAlias

from tensorflow import Tensor
from tensorflow._aliases import AnyArray, FloatArray
from tensorflow.debugging import experimental as experimental
from tensorflow.python.eager.context import (
    get_log_device_placement as get_log_device_placement,
    set_log_device_placement as set_log_device_placement,
)
from tensorflow.python.ops.check_ops import (
    assert_equal_v2 as assert_equal,
    assert_greater_equal_v2 as assert_greater_equal,
    assert_greater_v2 as assert_greater,
    assert_integer_v2 as assert_integer,
    assert_less_equal_v2 as assert_less_equal,
    assert_less_v2 as assert_less,
    assert_near_v2 as assert_near,
    assert_negative_v2 as assert_negative,
    assert_non_negative_v2 as assert_non_negative,
    assert_non_positive_v2 as assert_non_positive,
    assert_none_equal_v2 as assert_non_equal,
    assert_positive_v2 as assert_positive,
    assert_proper_iterable as assert_proper_iterable,
    assert_rank_at_least_v2 as assert_rank_at_least,
    assert_rank_in_v2 as assert_rank_in,
    assert_rank_v2 as assert_rank,
    assert_same_float_dtype as assert_same_float_dtype,
    assert_scalar_v2 as assert_scalar,
    assert_shapes_v2 as assert_shapes,
    assert_type_v2 as assert_type,
    is_numeric_tensor as is_numeric_tensor,
)
from tensorflow.python.ops.control_flow_assert import Assert as Assert
from tensorflow.python.ops.gen_array_ops import check_numerics as check_numerics
from tensorflow.python.ops.numerics import verify_tensor_all_finite_v2 as assert_all_finite
from tensorflow.python.util.traceback_utils import (
    disable_traceback_filtering as disable_traceback_filtering,
    enable_traceback_filtering as enable_traceback_filtering,
    is_traceback_filtering_enabled as is_traceback_filtering_enabled,
)

# module 'tensorflow.python.debug' has no attribute 'lib'
def disable_check_numerics() -> None: ...

# module 'tensorflow.python.debug' has no attribute 'lib'
def enable_check_numerics(stack_height_limit: int = 30, path_length_limit: int = 50) -> None: ...
