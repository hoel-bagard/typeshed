from tensorflow.python.trackable.base import Trackable

# Internal type that is commonly used as a base class
# and some public apis the signature needs it.
class CapturableResource(Trackable): ...
