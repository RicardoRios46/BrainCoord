import class_module
import numpy as np
import click
import re

bitacora = open("bitacora.txt", "w")

# ToDo ESta funcion hara testing del formato de los inputs. Va a estar decorada con Click para las entradas desde terminal
@click.command()
@click.option('--database_filename', prompt = 'Introduce your text file name within the extention')
@click.option('--reference_point',  prompt = 'Introduce you reference point (bregma or lambda)')
@click.option('--coordinate0', prompt = 'Introduce your cero coordinates')

def test_inputs(database_filename, reference_point, coordinate0):
    click.echo("Your inputs are: " + database_filename + " " + reference_point +  " " +coordinate0)
    #database_filename = "nombre del archivo"
    #reference_point = None  # lambda o bregma
    #coordinate0 = 0
    #print("hace testing de los inputs")


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

bitacora.write("My db used was: " +database_filename+ "\n" + /
"My reference point was: " + reference_point+ "\n" + /
"My initial coordinates were: " + coordinate0 + "\n" + /
"my final coordinates to used are: " + coordinates_result)

if __name__ == '__main__':
    test_inputs()
