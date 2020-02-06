import class_module
import checkInputs as chI
import click


@click.command()
@click.option('--database_filename', prompt = 'Introduce your text file name within the extention')
@click.option('--reference_point',  prompt = 'Introduce you reference point (bregma or lambda)')
@click.option('--AP', prompt = 'Introduce AP coordinate')
@click.option('--ML', prompt = 'Introduce ML coordinate')
@click.option('--DV', prompt = 'Introduce DV coordinate')
def getCheck_inputs(database_filename, reference_point, AP, ML, DV):
    coordinate0 = [AP, ML, DV]
    chI.checkFormat_referece_point(reference_point)
    chI.checkFormat_coordinate0(coordinate0)
    chI.checkValues_coordinate0(coordinate0, reference_point)
    chI.checkExistence_file(database_filename)
    chI.checkFormat_file(database_filename)

    return [database_filename, reference_point, coordinate0]

def test_inputs(database_filename, reference_point, coordinate0):
    click.echo("Your inputs are: " + database_filename + " " + reference_point +  " " +coordinate0)



if __name__ == '__main__':
    #test_inputs()
    # Inputs de prueba
    inputs = getCheck_inputs()
    #database_filename = "medial_der.csv"
    #reference_point = "lambda"
    #coordinate0 = [33, 15, 63.7]
    database_filename = inputs[0]
    reference_point = inputs[1]
    coordinate0 = inputs[2]
    print(coordinate0)
    #test_inputs(database_filename, reference_point, coordinate0)

    nucleo = class_module.Nucleo(database_filename, reference_point, coordinate0)

    nucleo.read_list()
    nucleo.create_point()

    coordinates_result = nucleo.get_coordinates()

    print(coordinates_result)
