"""Finalización controlada del programa con mensajes y códigos de salida."""

import sys
import time
from typing import NoReturn

from utils import imprimir


def finalized(
    message: str = "",
    success: bool = True,
    time1: float = 1.0,
    time2: float = 1.0,
) -> NoReturn:
    """Termina la ejecución del programa de forma controlada.

    Args:
        message: Mensaje personalizado a mostrar antes de salir
        success: Si la finalización es exitosa (afecta el código de salida)
        time1: Tiempo de espera inicial en segundos
        time2: Tiempo de espera antes de salir en segundos

    Raises:
        SystemExit: Siempre termina el programa (código 0 si success=True, 1 si False)

    Examples:
        >>> finalized("Proceso completado exitosamente")
        # Imprime mensaje y sale con código 0
        >>> finalized("Error crítico", success=False)
        # Imprime mensaje y sale con código 1

    Note:
        Esta función nunca retorna, siempre termina el programa
    """
    time.sleep(time1)
    mensaje_final = "¡Gracias por usar!"
    mensaje_error_final = "¡Algo salió mal!"
    final_message = (
        message if message else (mensaje_final if success else mensaje_error_final)
    )

    imprimir(final_message)
    time.sleep(time2)
    sys.exit(0 if success else 1)
