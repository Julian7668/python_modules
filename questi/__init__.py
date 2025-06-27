"""
Questi - Wrapper simplificado para questionary con validaciones automáticas.

Este paquete proporciona funciones de entrada de usuario con validación
automática basada en tipos y rangos, simplificando el uso de questionary.

Examples:
    >>> import questi
    >>> edad = questi.text("¿Cuál es tu edad?", int, 0, 120)
    >>> confirmado = questi.confirm("¿Continuar?")
    >>> opcion = questi.select("Elige:", ["A", "B", "C"])
"""

from .MDtext import text
from .MDselect import select
from .MDconfirm import confirm

__all__ = ["text", "select", "confirm"]
