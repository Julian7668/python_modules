"""Confirmaciones booleanas interactivas usando questionary."""

from typing import Any
import questionary

from .CONquesti_utils._MDvalidate_result import validate_result


def confirm(message: str = "¿True or False?", **kwargs: Any) -> bool:
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
    return validate_result(questionary.confirm(message, **kwargs).ask())
