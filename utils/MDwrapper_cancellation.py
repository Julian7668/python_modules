from typing import Any, Callable, Optional


def wrapper_cancellation(result: Optional[Any], exit_callback: Callable[[], Any]):
    return exit_callback() if not result else result
