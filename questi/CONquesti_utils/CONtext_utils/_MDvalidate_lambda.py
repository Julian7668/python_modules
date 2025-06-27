"""Validaciones de entrada para questionary con soporte de rangos numéricos."""

from typing import Callable


def __validate_int(
    x_raw: str,
    inicio_rango: float,
    fin_rango: float,
    inclusive_inicio: bool,
    inclusive_fin: bool,
) -> bool:
    """Valida si una cadena representa un entero válido dentro del rango especificado.

    Args:
        x_raw: Cadena de texto a validar
        inicio_rango: Límite inferior del rango permitido
        fin_rango: Límite superior del rango permitido
        inclusive_inicio: Si incluir el límite inferior en la validación
        inclusive_fin: Si incluir el límite superior en la validación

    Returns:
        True si la cadena es un entero válido dentro del rango, False en caso contrario

    Examples:
        >>> __validate_int("5", 0, 10, True, True)
        True
        >>> __validate_int("-3", 0, 10, True, True)
        False
    """
    x = x_raw.strip()

    # Verificar formato de número entero (incluyendo negativos)
    if x.startswith("-"):
        if not x[1:].isdigit():
            return False
    elif not x.isdigit():
        return False

    # Verificar que solo tenga un signo negativo al inicio
    if x.count("-") > 1 or (x.find("-") not in [0, -1]):
        return False

    # Convertir a entero y verificar rango
    x = int(x)
    if inclusive_inicio and inclusive_fin:
        return inicio_rango <= x <= fin_rango
    if inclusive_inicio:
        return inicio_rango <= x < fin_rango
    if inclusive_fin:
        return inicio_rango < x <= fin_rango
    return inicio_rango < x < fin_rango


def __validate_float(
    x_raw: str,
    inicio_rango: float,
    fin_rango: float,
    inclusive_inicio: bool,
    inclusive_fin: bool,
) -> bool:
    """Valida si una cadena representa un flotante válido dentro del rango especificado.

    Args:
        x_raw: Cadena de texto a validar
        inicio_rango: Límite inferior del rango permitido
        fin_rango: Límite superior del rango permitido
        inclusive_inicio: Si incluir el límite inferior en la validación
        inclusive_fin: Si incluir el límite superior en la validación

    Returns:
        True si la cadena es un flotante válido dentro del rango, False en caso contrario

    Examples:
        >>> __validate_float("3.14", 0.0, 5.0, True, True)
        True
        >>> __validate_float("6.28", 0.0, 5.0, True, True)
        False
    """
    x = x_raw.strip()

    # Verificar formato de número decimal (incluyendo negativos)
    if x.startswith("-"):
        if not x[1:].replace(".", "", 1).isdigit():
            return False
    elif not x.replace(".", "", 1).isdigit():
        return False

    # Verificar que solo tenga un punto decimal y un signo negativo
    if x.count(".") > 1 or x.count("-") > 1 or (x.find("-") not in [0, -1]):
        return False

    # Convertir a float y verificar rango
    x = float(x)
    if inclusive_inicio and inclusive_fin:
        return inicio_rango <= x <= fin_rango
    if inclusive_inicio:
        return inicio_rango <= x < fin_rango
    if inclusive_fin:
        return inicio_rango < x <= fin_rango
    return inicio_rango < x < fin_rango


def _validate_lambda(
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
        >>> validator = _validate_lambda(int, 1, 100, True, True, True)
        >>> validator("50")
        True
    """
    if return_type is int or return_type is float:
        arguments_validates = {
            "inicio_rango": inicio_rango,
            "fin_rango": fin_rango,
            "inclusive_inicio": inclusive_inicio,
            "inclusive_fin": inclusive_fin,
        }
        return lambda x: (
            __validate_int(x, **arguments_validates)
            if return_type is int
            else __validate_float(x, **arguments_validates)
        )

    return lambda x: (
        True if return_type is bool or not use_strip else (x.strip() != "")
    )
