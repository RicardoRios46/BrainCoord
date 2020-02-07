"""BrainCoord 

It was built in reference to the coronal plates from the Mouse Brain Paxinos Atlas. This script allows to calculate the optimal coordinates to reach any brain nucleus in the mouse, giving the resultant coordinates points (AP, ML, DV) from a coordenate 0 (bregma or lambda), previously entered by the user. In addition this script is open to import datbase of any particular nucleus. The actual version 0.1 includes the cerebellar nuclei: medial (MN), lateral vestibular (LVe), medial vestibular parvocelular (MVePc) and anterior Interpositus (IntA).

This tool accepts .cvs files which requires to contain the following ordered coordinates (in mm), per each imported nucleus: 
    * point reference bregma
    * point reference lambda
    * lateral limit 
    * medial limit
    * dorsal limit
    * vetral limit
    
This script requires that `NumPy` be installed within the actual Python environment.

"""

import class_module
import checkInputs as chI
import click


@click.command()
@click.option('--database_filename', prompt='Select your nucleus')
@click.option('--reference_point', prompt='Introduce you reference point (bregma or lambda)')
@click.option('--ap', prompt='Introduce AP coordinate', type=float)
@click.option('--ml', prompt='Introduce ML coordinate', type=float)
@click.option('--dv', prompt='Introduce DV coordinate', type=float)
@click.option('--logbook', default=False, help='Save results at "logbook.txt"')
@click.option('--debug', default=False, help='Save debuging messages at "debug_file.log"')
def brain_coord(database_filename, reference_point, ap, ml, dv, logbook, debug):
    """Input data with the nucleus to reach and the started coordinates took from the mouse.

    Atributes
    ---------
    database_filename : str
        file with the target nuclei database
    reference_point : str 
        craneal point, options bregma or lambda
    ap : float
        anter-posterior coordinate
    ml : float
        medio-lateral coordinate
    dv : float
        dorso-ventral coordinate
    """

    print("Your inputs introduced are: " + database_filename + ", " + reference_point + ", AP coord: " + str(ap) +
          ", ML coord: " + str(ml) + ", DV coord: " + str(dv))
    coordinate0 = [ap, ml, dv]
    database_filename = database_filename + ".csv"

    chI.checkFormat_referece_point(reference_point)
    chI.checkFormat_coordinate0(coordinate0)
    chI.checkValues_coordinate0(coordinate0, reference_point)
    chI.checkExistence_file(database_filename)
    chI.checkFormat_file(database_filename)

    # breakpoint()
    nucleo = class_module.Nucleo(database_filename, reference_point, coordinate0)

    # breakpoint()
    nucleo.read_list()
    # breakpoint()
    nucleo.create_point()
    # breakpoint()
    coordinates_result = nucleo.get_coordinates()

    if debug:
        nucleo.print_debugfile()

    # Esta bandera imprime la logbook en un archivo
    if logbook:
        nucleo.update_logbook(coordinates_result)

    # Imprime los resultados en pantalla
    print("The resultantes coordinates to used are: " + str(coordinates_result) + " AP, ML, DV")


if __name__ == '__main__':
    brain_coord()
