"""BrainCoord 

It was built in reference to the Mouse Brain Paxinos Atlas. This script allows to calculate the optimal coordinates to reach any brain nucleus in the mouse, giving the resultant coordinates points (AP, ML, DV) from a coordenate 0 (bregma or lambda), previously entered by the user. In addition this script is open to import datbase of any particular nucleus. The actual version 0.1 includes  

This tool accepts .cvs files. Which requires to contain the following ordered coordinates (in mm), per each imported nucleus: 
    * point reference bregma
    * point reference lambda
    * lateral limit 
    * medial limit
    * dorsal limit
    * vetral limit
    
This script requires that `NumPy` be installed within the actual Python environment.

"""


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
