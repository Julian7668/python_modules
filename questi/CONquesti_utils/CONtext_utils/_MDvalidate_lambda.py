"""Validaciones de entrada para questionary con soporte de rangos numéricos."""

from typing import Callable, Dict, Any, Type, Union


def _validate_lambda(
    x_raw: str,
    return_type: Union[Type[int], Type[float]],
    inicio_rango: float,
    fin_rango: float,
    inclusive_inicio: bool,
    inclusive_fin: bool,
) -> bool:
    """Valida si una cadena representa un número válido dentro del rango especificado.

    Args:
        x_raw: Cadena de texto a validar
        return_type: Tipo de dato esperado (int o float)
        inicio_rango: Límite inferior del rango permitido
        fin_rango: Límite superior del rango permitido
        inclusive_inicio: Si incluir el límite inferior en la validación
        inclusive_fin: Si incluir el límite superior en la validación

    Returns:
        True si la cadena es un número válido dentro del rango, False en caso contrario

    Examples:
        >>> _validate_lambda("5", int, 0, 10, True, True)
        True
        >>> _validate_lambda("-3", int, 0, 10, True, True)
        False
        >>> _validate_lambda("+7", int, 0, 10, True, True)
        True
        >>> _validate_lambda("3.14", float, 0.0, 5.0, True, True)
        True
        >>> _validate_lambda("+2.71", float, 0.0, 5.0, True, True)
        True
    """
    # Remover espacios en blanco al inicio y final
    x = x_raw.strip()

    # Verificar que solo tenga un signo y que solo pueda estar al inicio
    if (x.count("-") + x.count("+")) > 1 or (
        x.find("-") not in [0, -1] and x.find("+") not in [0, -1]
    ):
        return False

    # Remover el signo para las validaciones de formato numérico
    if x.count("-") or x.count("+"):
        x = x[1:]

    # Validar formato según el tipo de dato esperado
    if return_type is float:
        # Para floats: verificar formato válido (máximo un punto decimal)
        if not x.replace(".", "", 1).isdigit():
            return False
    else:
        # Para enteros: solo se permiten dígitos (sin puntos decimales)
        if not x.isdigit():
            return False

    # Convertir al tipo deseado
    x = return_type(x)

    # Verificar rango según los parámetros de inclusividad
    return (x >= inicio_rango if inclusive_inicio else x > inicio_rango) and (
        x <= fin_rango if inclusive_fin else x < fin_rango
    )


def validate_factory(
    return_type: type,
    inicio_rango: float,
    fin_rango: float,
    inclusive_inicio: bool,
    inclusive_fin: bool,
    use_strip: bool,
) -> Callable[[str], bool]:
    """Genera una función de validación personalizada para questionary.

    Args:
        return_type: Tipo de dato esperado (int, float, str, bool)
        inicio_rango: Límite inferior del rango para tipos numéricos
        fin_rango: Límite superior del rango para tipos numéricos
        inclusive_inicio: Si incluir el límite inferior
        inclusive_fin: Si incluir el límite superior
        use_strip: Si aplicar strip() antes de validar strings

    Returns:
        Función de validación lista para usar con questionary

    Examples:
        >>> validator = validate_factory(int, 1, 100, True, True, True)
        >>> validator("50")
        True
    """
    if return_type is int or return_type is float:
        validates_lambda: Dict[str, Any] = {
            "return_type": return_type,
            "inicio_rango": inicio_rango,
            "fin_rango": fin_rango,
            "inclusive_inicio": inclusive_inicio,
            "inclusive_fin": inclusive_fin,
        }
        return lambda x: _validate_lambda(x, **validates_lambda)

    return lambda x: (
        True if return_type is bool or not use_strip else (x.strip() != "")
    )
