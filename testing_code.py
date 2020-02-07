import numpy as np

class InadequateFormatException(Exception):
    """ This class derivaded from Exception that raise the message error"""
    def __init__(self, *args, **kwargs):  # start the class with the default arguments
        Exception.__init__(self, "Incorrect reference point text. Insert 'bregma' or 'lambda'")


def checkFormat_referece_point(reference_point):
    """"This funcion check if the reference point is writting correctly 'bregma' or 'lambda' """
    if type(reference_point) == str:
        if reference_point == "bregma" or reference_point == "lambda":
            return True
        else:
            raise InadequateFormatException()

    else:
        raise InadequateFormatException()


def checkFormat_coordinate0(coordinate0):
    """Function that probe the coordinates are in a number list"""
    if type(coordinate0) == list:
        if len(coordinate0) == 3:
            for elem in coordinate0:
                try:
                    float(elem)
                except Exception as e:
                    raise Exception("The coordinate '" + str(elem) + "' is not a number")

        else:
            raise Exception("Missing coordinates, there is only: {}".format(len(coordinate0)))
    else:
        raise Exception("Incorrect coordinate format. Most be a list with 3 coordinate.")

    return True


def checkValues_coordinate0(coordinate0, reference_point):
    """Function that check the range of the input coordinates to be rigth"""

    # AP
    if 90 > coordinate0[0] > -90:
        pass  # Entry in correct range
    else:
        raise Exception(
            "Coordinate AP ({}) out of range for lambda, should be between -90mm and 90mm: "
            .format(len(coordinate0)))
    # ML
    if 90 > coordinate0[1] > -90:
        pass  # Entry in correct range
    else:
        raise Exception(
            "Coordinate ML ({}) out of range, should be between -90mm and 90mm: "
            .format(len(coordinate0)))

    # DV
    if 90 > coordinate0[2] > -90:
        pass  # Entry in correct range
    else:
        raise Exception(
            "Coordinate DV ({}) out of range, should be between -90mm and 90mm: "
            .format(len(coordinate0)))

    return True


def checkExistence_file(database_filename):
    """Function that check if the db file can be opened"""
    try:
        with open(database_filename) as file:
            read_data = file.read()
    except Exception as e:
        raise Exception("Could not opened the file '" + str(database_filename) + "'")
    return True

# Funtion used to check the format file
def checkFormat_file(database_filename):
    """Function that check is the file formart is csv"""
    try:
        # Read the file using numpy, if there is something wrong numpy thrown the excepcion
        dataset = np.genfromtxt(database_filename, skip_header=1, delimiter=",", usecols=(
            range(6)), loose = False, invalid_raise = True)
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Delate rows with NaNs
    except Exception as e:
        raise Exception("File '" + database_filename + "' has to be a csv file. Go to documentation.")
    return True
