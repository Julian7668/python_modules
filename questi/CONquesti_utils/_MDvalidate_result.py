"""Validación y conversión de resultados de questionary."""

from typing import Any, Optional

from utils import finalized


def validate_result(
    # argumento de text select y confirm
    result: Optional[str | bool],
    # argumentos de text y select
    return_type: type = str,
    use_strip: bool = True,
    # argumento de select
    indice: Optional[slice] = None,
) -> Any:
    """Procesa y convierte el resultado obtenido de questionary.

    Args:
        result: Resultado crudo de questionary (puede ser None si se canceló)
        return_type: Tipo al que convertir el resultado
        use_strip: Si aplicar strip() a strings antes de convertir
        exit_callback: Función a ejecutar si el usuario canceló la operación
        indice: Slice para extraer parte específica del resultado

    Returns:
        Resultado convertido al tipo especificado

    Raises:
        SystemExit: Si el usuario cancela y no hay exit_callback definido
    """
    if result is None:
        return finalized()
    if isinstance(result, bool):
        return bool(result)

    result = result if return_type is bool or not use_strip else result.strip()
    return return_type(result) if not indice else return_type(result[indice])
