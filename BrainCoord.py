import class_module
import numpy as np

# ToDo ESta funcion hara testing del formato de los inputs. Va a estar decorada con Click para las entradas desde terminal
def test_inputs(database_filename, reference_point, coordinate0):
    #database_filename = "nombre del archivo"
    #reference_point = None  # lambda o bregma
    #coordinate0 = 0

    print("hace testing de los inputs")


# Inicia la funcion principal

# Inputs de prueba
database_filename = "medial_der.csv"
reference_point = "lambda"
coordinate0 = [33, 15, 63.7]

print(coordinate0)
test_inputs(database_filename, reference_point, coordinate0)

nucleo = class_module.Nucleo(database_filename, reference_point, coordinate0)

nucleo.read_list()
nucleo.create_point()

coordinates_result = nucleo.get_coordinates()

print(coordinates_result)
