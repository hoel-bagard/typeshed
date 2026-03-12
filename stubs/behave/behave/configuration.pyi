import re
from typing import Any

from behave.formatter.base import StreamOpener
from behave.userdata import UserData

class Configuration:
    color: str
    dry_run: bool
    format: list[str] | None
    include_re: re.Pattern[str] | None
    exclude_re: re.Pattern[str] | None
    junit: bool
    junit_directory: str
    jobs: int
    lang: str | None
    logging_format: str | None
    logging_datefmt: str | None
    logging_level: int
    logging_filter: str | None
    logging_clear_handlers: bool
    name: list[str] | None
    name_re: re.Pattern[str] | None
    paths: list[str]
    quiet: bool
    runner: str
    show_skipped: bool
    show_snippets: bool
    show_multiline: bool
    show_source: bool
    show_timings: bool
    stage: str | None
    steps_catalog: bool
    stop: bool
    summary: bool
    tags: str | None
    tag_expression: Any  # TagExpression
    verbose: bool
    wip: bool
    capture: bool | None
    capture_stdout: bool
    capture_stderr: bool
    capture_log: bool
    capture_hooks: bool
    userdata: UserData
    outputs: list[StreamOpener]
    reporters: list[Any]
    formatters: list[Any]
    steps_dir: str
    environment_file: str
    base_dir: str | None
    default_format: str
    scenario_outline_annotation_schema: str | None

    def __init__(
        self,
        command_args: list[str] | str | None = None,
        load_config: bool = True,
        verbose: bool | None = None,
        **kwargs: Any,
    ) -> None: ...
    def setup_logging(
        self,
        level: int | None = None,
        filename: str | None = None,
        configfile: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def exclude(self, filename: str) -> bool: ...
    def should_capture(self) -> bool: ...
    def should_capture_hooks(self) -> bool: ...
    def has_colored_mode(self, file: Any | None = None) -> bool: ...
    def update_userdata(self, data: dict[str, Any]) -> None: ...
