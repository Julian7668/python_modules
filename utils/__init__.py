"""
Utils - Utilidades generales para el proyecto.

Proporciona funciones para:
- Impresión formateada con estilos
- Finalización controlada del programa
- Introspección de líneas de código en tiempo de ejecución

Examples:
    >>> from utils import imprimir, finalized, get_line_name
    >>> imprimir("Mensaje con estilo")
    >>> linea = get_line_name()
    >>> finalized("Terminando programa")
"""

from .MDget_line_name import get_line_name
from .MDimprimir import imprimir
from .MDfinalized import finalized

__all__ = ["imprimir", "finalized", "get_line_name"]
