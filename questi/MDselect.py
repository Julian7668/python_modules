"""Menús de selección interactivos con questionary."""

from typing import Any, Callable, Dict, Optional, Sequence, Union
import questionary
from questionary.prompts.common import Choice

from .CONquesti_utils._MDvalidate_result import _validate_result


def select(
    # argumentos de questionary.select()
    message: str = "Seleccione una opción:",
    choices: Sequence[Union[str, Choice, Dict[str, Any]]] = ("A.", "B.", "C."),
    # argumentos de _validate_result()
    return_type: type = str,
    indice: slice = slice(None),
    use_strip: bool = True,
    exit_callback: Optional[Callable[[], Any]] = None,
    # argumentos de questionary.select()
    **kwargs: Any,
) -> Optional[Union[str, int, float, bool]]:
    """Presenta un menú de selección al usuario.

    Args:
        message: Texto del prompt
        choices: Lista de opciones disponibles
        return_type: Tipo al que convertir la selección
        indice: Slice para extraer parte de la opción seleccionada
        use_strip: Si aplicar strip() al resultado
        exit_callback: Función a ejecutar si el usuario cancela
        **kwargs: Argumentos adicionales para questionary.select

    Returns:
        Opción seleccionada convertida al tipo especificado

    Examples:
        >>> select("Elige:", ["Opción 1", "Opción 2"])
        "Opción 1"
        >>> select("Número:", ["1. Uno", "2. Dos"], int, slice(0, 1))
        1
    """
    arguments_questionary_select: Dict[str, Any] = {
        "message": message,
        "choices": choices,
        **kwargs,
    }
    arguments_validate_result: Dict[str, Any] = {
        "result": questionary.select(**arguments_questionary_select).ask(),
        "return_type": return_type,
        "use_strip": use_strip,
        "exit_callback": exit_callback,
        "indice": indice,
    }
    return _validate_result(**arguments_validate_result)
