import class_module as cm
import numpy as np

# ESta funcion esta decorada con Click para las entradas
def test_imputs():
    #database_filename = "nombre del archivo"
    #reference_point = None  # lambda o bregma
    #n_points = 1
    #coordinate0 = [0, 0, 0]

    print("hace testing de los inputs")


# Inicia la funcion principal
database_filename = "datatest.csv"

test_imputs()

nucleo = cm.Nucleo(database_filename)

nucleo.read_list()
nucleo.create_point()

coordinates_result = nucleo.get_coordinates()

print(coordinates_result)