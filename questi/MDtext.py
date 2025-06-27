"""Entrada de texto con validaciones automáticas usando questionary."""

from typing import Any, Callable, Dict, Optional, Union
import questionary

from .CONquesti_utils._MDvalidate_result import _validate_result
from .CONquesti_utils.CONtext_utils._MDvalidate_lambda import _validate_lambda


def text(
    # argumento de questionary.text()
    message: str = "Ingrese algun valor:",
    # argumento de _validate_lambda() y _validate_result()
    return_type: type = str,
    # argumentos de _validate_lambda()
    inicio_rango: float = float("-inf"),
    fin_rango: float = float("inf"),
    inclusive_inicio: bool = True,
    inclusive_fin: bool = True,
    # argumento de _validate_lambda() y _validate_result()
    use_strip: bool = True,
    # argumento de _validate_result()
    exit_callback: Optional[Callable[[], Any]] = None,
    # argumentos de questionary.text()
    validate: Any = None,
    **kwargs: Any,
) -> Optional[Union[str, int, float, bool]]:
    """Solicita entrada de texto con validación automática por tipo.

    Args:
        message: Texto del prompt
        return_type: Tipo esperado (str, int, float, bool)
        inicio_rango: Límite inferior para números
        fin_rango: Límite superior para números
        inclusive_inicio: Si incluir el límite inferior
        inclusive_fin: Si incluir el límite superior
        use_strip: Si aplicar strip() al input
        exit_callback: Función a ejecutar si el usuario cancela
        validate: Función de validación personalizada
        **kwargs: Argumentos adicionales para questionary.text

    Returns:
        Valor ingresado convertido al tipo especificado

    Examples:
        >>> text("Edad:", int, 0, 120)
        25
        >>> text("Precio:", float, 0.0, 1000.0)
        19.99
        >>> text("Nombre:")
        "Juan"

    Note:
        Para return_type=bool: la validación es limitada; solo se fuerza use_strip=False. Usese bajo su responsabilidad.
    """
    if validate is None:
        arguments_validate_lambda: Dict[str, Any] = {
            "return_type": return_type,
            "inicio_rango": inicio_rango,
            "fin_rango": fin_rango,
            "inclusive_inicio": inclusive_inicio,
            "inclusive_fin": inclusive_fin,
            "use_strip": use_strip,
        }
        validator: Callable[[str], bool] = _validate_lambda(**arguments_validate_lambda)
    else:
        validator = validate

    arguments_questionary_text: Dict[str, Any] = {
        "message": message,
        "validate": validator,
        **kwargs,
    }
    arguments_validate_result: Dict[str, Any] = {
        "result": questionary.text(**arguments_questionary_text).ask(),
        "return_type": return_type,
        "use_strip": use_strip,
        "exit_callback": exit_callback,
    }
    return _validate_result(**arguments_validate_result)
