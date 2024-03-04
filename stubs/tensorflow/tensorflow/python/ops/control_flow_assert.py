from tensorflow import Tensor, TensorCompatible


class Assert:
    def __init__(
        self, condition: TensorCompatible, data: Tensor, summarize: int | None = None, name: str | None = None
    ) -> None: ...
