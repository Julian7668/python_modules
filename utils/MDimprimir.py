"""Impresión formateada usando prompt_toolkit con estilos de questionary."""

from typing import Any
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_STYLE


def imprimir(
    *values: Any,
    style: Style = DEFAULT_STYLE,
    **kwargs: Any,
) -> None:
    """Imprime texto con formato y estilos usando prompt_toolkit.

    Args:
        *values: Valores a imprimir (acepta múltiples argumentos)
        style: Estilo de prompt_toolkit para el formato del texto
        **kwargs: Argumentos adicionales para print_formatted_text

    Examples:
        >>> imprimir("Hola mundo")
        Hola mundo
        >>> from prompt_toolkit.styles import Style
        >>> mi_estilo = Style.from_dict({'info': '#00aa00 bold'})
        >>> imprimir("Texto verde", style=mi_estilo)

    Note:
        Mantiene compatibilidad con la función print() estándar pero con estilos
    """
    print_formatted_text(*values, style=style, **kwargs)
