import numpy as np

class InadequateFormatException(Exception):
    def __init__(self, *args, **kwargs):  # inicializamos la clase con los argumentos que recibimos por default
        Exception.__init__(self, "Texto para punto de referencia Incorrecto. Inserte 'bregma' o 'lambda'")


def checkFormat_referece_point(reference_point):
    if type(reference_point) == str:
        if reference_point == "bregma" or reference_point == "lambda":
            return True
        else:
            raise InadequateFormatException()

    else:
        raise InadequateFormatException()


def checkFormat_coordinate0(coordinate0):
    """Checa la coordenadas es una lista valida con numeros"""
    if type(coordinate0) == list:
        if len(coordinate0) == 3:
            for elem in coordinate0:
                try:
                    float(elem)
                except Exception as e: # ToDo checar por que es una except solo
                    raise Exception("La coordenada '" + str(elem) + "' no es un numero")

        else:
            raise Exception("Faltan coordenadas, solo habia: {}".format(len(coordinate0)))
    else:
        raise Exception("Formato de coordenadas incorrecto. Debe ser una lista con 3 coordenadas.")

    return True


def checkValues_coordinate0(coordinate0, reference_point):
    """Checa los elementos de la lista de coordenada estan en el rango correcto"""

    # AP
    if 90 > coordinate0[0] > -90:
        pass  # Entrada en rango correcto
    else:
        raise Exception(
            "Coordenada AP ({}) fuera de rango para lambda, deberia estar entre -90mm y 90mm: "
            .format(len(coordinate0)))
    # ML
    if 90 > coordinate0[1] > -90:
        pass  # Entrada en rango correcto
    else:
        raise Exception(
            "Coordenada ML ({}) fuera de rango, deberia estar entre -90mm y 90mm: "
            .format(len(coordinate0)))

    # DV
    if 90 > coordinate0[2] > -90:
        pass  # Entrada en rango correcto
    else:
        raise Exception(
            "Coordenada DV ({}) fuera de rango, deberia estar entre -90mm y 90mm: "
            .format(len(coordinate0)))

    return True


def checkExistence_file(database_filename):
    try:
        with open(database_filename) as file:
            read_data = file.read()
    except Exception as e:
        raise Exception("No pude abrir el archivo '" + database_filename + "'")
    return True

# ToDo Esta funcion podria ser mas robusta al formato de la tabla pero en general hace buen trabajo
def checkFormat_file(database_filename):
    try:
        # Lee el archivo usando numpy, si hay algo mal Numpy arroja la excepcion
        dataset = np.genfromtxt(database_filename, skip_header=1, delimiter=",", usecols=(
            range(6)), loose = False, invalid_raise = True)
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Eliminamos las filas con NaNs
    except Exception as e:
        raise Exception("Archivo '" + database_filename + "' tiene un formato de tabla incorrecto. Revisar documentacion.")
    return True
