"""Formateo del contenido de líneas de código desde la pila de llamadas."""

import inspect
from inspect import FrameInfo
import re
from typing import Optional


def _validate_pattern(
    cadena: str,
    pattern: Optional[str | re.Pattern[str]],
) -> str:
    """Aplica un patrón regex a una cadena y retorna la primera coincidencia.

    Args:
        cadena: Cadena de texto a validar
        pattern: Patrón de expresión regular (str o Pattern compilado)

    Returns:
        Primera coincidencia del patrón o la cadena original si pattern es None

    Raises:
        SystemExit: Si el patrón no encuentra coincidencias en la cadena

    Examples:
        >>> _validate_pattern("func_test_123", r"test_\\d+")
        "test_123"
        >>> _validate_pattern("mi_funcion", None)
        "mi_funcion"
    """
    if pattern is None:
        return cadena

    if match := re.search(pattern, cadena):
        return match.group(0)
    raise SystemExit(
        f"En: {cadena}\nNo se encontró coincidencia con el patrón: {pattern}"
    )


def get_line_name(
    pattern: Optional[str | re.Pattern[str]] = None,
    pila: int = 2,
    use_strip: bool = True,
) -> str:
    """Obtiene el contenido de una línea de código desde la pila de llamadas.

    Args:
        pattern: Patrón regex para extraer parte específica de la línea
        pila: Nivel de la pila a inspeccionar (por defecto 2)
        use_strip: Si aplicar strip() al contenido de la línea

    Returns:
        Contenido de la línea (opcionalmente filtrado por el patrón)

    Raises:
        SystemExit: Si la línea está vacía, no disponible o el contexto es None

    Examples:
        >>> resultado = get_line_name(r'\\w+\\s*=')  # Extrae "resultado ="
        "resultado ="

    Note:
        Útil para obtener nombres de variables o expresiones en tiempo de ejecución.
        Inspecciona el frame_info de la pila para acceder al código fuente.
    """
    frame_info: Optional[FrameInfo] = inspect.stack()[pila]
    if frame_info.code_context is None:
        raise SystemExit("No se pudo obtener el contexto de código fuente.")

    name: str = (
        frame_info.code_context[0].strip() if use_strip else frame_info.code_context[0]
    )
    return _validate_pattern(name, pattern)
