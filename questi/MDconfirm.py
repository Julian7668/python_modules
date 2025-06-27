"""Confirmaciones booleanas interactivas usando questionary."""

from typing import Any, Callable, Dict, Optional
import questionary

from .CONquesti_utils._MDvalidate_result import _validate_result


def confirm(
    # argumento de questionary.confirm()
    message: str = "¿True or False?",
    # argumento de _validate_result()
    exit_callback: Optional[Callable[[], Any]] = None,
    # argumentos de questionary.confirm()
    **kwargs: Any,
) -> bool:
    """Solicita confirmación booleana al usuario.

    Args:
        message: Pregunta a mostrar al usuario
        exit_callback: Función a ejecutar si el usuario cancela
        **kwargs: Argumentos adicionales para questionary.confirm

    Returns:
        Respuesta booleana del usuario

    Examples:
        >>> confirm("¿Continuar con la operación?")
        True  # Si el usuario confirma
        >>> confirm("¿Eliminar archivo?", default=False)
        False  # Si el usuario rechaza
    """
    arguments_questionary_confirm: Dict[str, Any] = {
        "message": message,
        **kwargs,
    }
    arguments_validate_result: Dict[str, Any] = {
        "result": questionary.confirm(**arguments_questionary_confirm).ask(),
        "exit_callback": exit_callback,
    }
    return _validate_result(**arguments_validate_result)
