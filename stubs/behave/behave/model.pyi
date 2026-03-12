from typing import Any

class Feature:
    keyword: str
    name: str
    description: list[str]
    filename: str
    line: int
    tags: list[str]
    language: str | None
    scenarios: list[Scenario]
    background: Background | None
    status: Any  # Status enum
    duration: float
    hook_failed: bool

class Scenario:
    keyword: str
    name: str
    description: list[str]
    filename: str
    line: int
    tags: list[str]
    steps: list[Step]
    feature: Feature | None
    background: Background | None
    status: Any  # Status enum
    duration: float
    hook_failed: bool

class ScenarioOutline(Scenario):
    examples: list[Examples]

class Background:
    keyword: str
    name: str
    steps: list[Step]
    filename: str
    line: int
    duration: float

class Step:
    keyword: str
    name: str
    step_type: str
    text: Text | None
    table: Table | None
    filename: str
    line: int
    status: Any  # Status enum
    duration: float
    error_message: str | None

class Examples:
    keyword: str
    name: str
    table: Table | None
    filename: str
    line: int
    tags: list[str]

class Table:
    headings: list[str]
    rows: list[Row]
    line: int

    def __init__(self, headings: list[str], rows: list[list[str]] | None = None, line: int | None = None) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, index: int) -> Row: ...
    def __len__(self) -> int: ...
    def add_row(self, row: list[str] | Row, line: int | None = None) -> None: ...
    def add_column(self, column_name: str, values: list[str] | None = None, default_value: str = "") -> int: ...
    def has_column(self, column_name: str) -> bool: ...
    def get_column_index(self, column_name: str) -> int: ...

class Row:
    headings: list[str]
    cells: list[str]
    line: int | None

    def __init__(self, headings: list[str], cells: list[str], line: int | None = None, comments: Any | None = None) -> None: ...
    def __getitem__(self, name: str | int) -> str: ...
    def __contains__(self, item: str) -> bool: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def items(self) -> list[tuple[str, str]]: ...
    def get(self, key: str, default: str | None = None) -> str | None: ...
    def as_dict(self) -> dict[str, str]: ...

class Tag(str):
    line: int
    def __new__(cls, name: str, line: int) -> Tag: ...

class Text(str):
    content_type: str
    line: int
    def __new__(cls, value: str, content_type: str = "text/plain", line: int = 0) -> Text: ...

class Rule:
    keyword: str
    name: str
    description: list[str]
    filename: str
    line: int
    tags: list[str]
    scenarios: list[Scenario]
    background: Background | None
    status: Any  # Status enum
    duration: float
