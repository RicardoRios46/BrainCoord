import class_module
import checkInputs as chI
import click


@click.command()
@click.option('--database_filename', prompt = 'Introduce your text file name within the extention')
@click.option('--reference_point',  prompt = 'Introduce you reference point (bregma or lambda)')
@click.option('--ap', prompt = 'Introduce AP coordinate',type=float)
@click.option('--ml', prompt = 'Introduce ML coordinate',type=float)
@click.option('--dv', prompt = 'Introduce DV coordinate',type=float)
def brain_coord(database_filename, reference_point, ap, ml, dv):
    coordinate0 = [ap, ml, dv]

    chI.checkFormat_referece_point(reference_point)
    chI.checkFormat_coordinate0(coordinate0)
    chI.checkValues_coordinate0(coordinate0, reference_point)
    chI.checkExistence_file(database_filename)
    chI.checkFormat_file(database_filename)

    #database_filename = "medial_der.csv"
    #reference_point = "lambda"
    #coordinate0 = [33, 15, 63.7]
    print(coordinate0)
    #test_inputs(database_filename, reference_point, coordinate0)

    nucleo = class_module.Nucleo(database_filename, reference_point, coordinate0)

    nucleo.read_list()
    nucleo.create_point()

    coordinates_result = nucleo.get_coordinates()

    print(coordinates_result)


if __name__ == '__main__':
    brain_coord()

