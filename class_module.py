import numpy as np
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    filename='debug_file.log',
    filemode='w'
)

class Nucleo():
    """A class used for each nuclei to identify
    
    ...

    Attributes
    ----------
    database_filename : str
        file type .csv that contain the list of coordinates per nuclei
    reference_point : str
        researcher chooses point, (options bregma or lambda)
    coordinate0 : float
        coordinates in AP, ML, DV axis belonging to the choosed reference point in the current mouse
    lambda_range : float
        accpetable range in mm for lambda coordinate (up to 90)
    bregma_range : float
        accpetable range in mm for bregma coordinate (up to 90)
    medio_range : float
        accpetable range in mm for medial coordinate (up to 90)
    lateral_range : float
        accpetable range in mm for lateral coordinate (up to 90)
    dorso_range : float
        accpetable range in mm for dorsal coordinate (up to 90)
    ventral_range : float
        accpetable range in mm for ventral coordinate (up to 90)
    n_points : float
        total row number in the datalist
    
    Methods
    -------
    read_list
        Reads the dataset with the coordinates list of the target nuclei, organizated as lambda, bregma, ML, DV. 
    create_point
        Calculates the central point of the target nuclei at the position of the biggest area.
    get_coordinates
        Gives the resultant coordinates to move on, based on the coordinate0 and the target nuclei.
    update_logbook
        Print the resultant coordinates and mouse characteristics to use as lab-book.
    """

    # Public atributes to the inputs.
    database_filename = "nombre del archivo"
    reference_point = None  # lambda o bregma
    coordinate0 = [0, 0, 0]

    # Public atributes. This variable contain the coordinates information.
    lambda_range = None
    bregma_range = None
    medio_range = None
    lateral_range = None
    dorso_range = None
    ventral_range = None
    n_points = 0

    def __init__(self, database_filename, reference_point, coordinate0):
        """
        Parameters
        ----------
        database_filename : str
            file type .csv that contain the list of coordinates per nuclei
        reference_point : str
            researcher chooses point, (options bregma or lambda)
        coordinate0 : List[float]
            coordinates in AP, ML, DV axis belonging to the choosed reference point in the current mouse
        """
        self.database_filename = database_filename
        self.reference_point = reference_point
        self.coordinate0 = coordinate0

        # Private atributes
        self.__xRange = None
        self.__yRange = None
        self.__area = None
        self.__cuadro_chido = 0

    def __find_cuadro_chido(self):
        """ Calculates the square with the biggest area whithin target nuclei

        Returns
        -------
        indx_max_area
            Index with the file of the square with max area in variables
        """
        max_area = 0
        indx_max_area = 0
        indx = 0
        for area in self.__area:
            if area > max_area:
                max_area = area
                indx_max_area = indx
            indx += 1
        return indx_max_area

    def read_list(self):
        """Reads the dataset with the coordinates list of the target nuclei, organizated as lambda, bregma, medial,
        lateral, dorsal, ventral
        """

        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(
            range(6)))  # Upload the .csv, omit the header and consider the 5 columns
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Eliminate the columns with NaNs
        # Upload the .csv, omit the header and consider the 5 columns
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(range(6)))
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Eliminate the columns with NaNs
        # Fill object variable with the table data
        self.lambda_range = dataset[:, 0]
        self.bregma_range = dataset[:, 1]
        self.lateral_range = dataset[:, 2]
        self.medio_range = dataset[:, 3]
        self.dorso_range = dataset[:, 4]
        self.ventral_range = dataset[:, 5]
        # number of total rows 
        self.n_points = self.bregma_range.size

    def create_point(self):
        """ Calculates the central point of the target nuclei at the position of the biggest area
        
        This function takes the medial value of the total length of the nuclei in each axis and calculates the area
        per each AP coordinate. Later on, selects the biggest area.
        """

        # To obtain the square from the database
        self.__xRange = self.medio_range - self.lateral_range
        self.__yRange = self.ventral_range - self.dorso_range
        # To obtain the area of the square and select the biggest one
        self.__area = abs(self.__xRange * self.__yRange)
        self.__cuadro_chido = self.__find_cuadro_chido()



    def get_coordinates(self):
        """Gives the resultant coordinates to move on, based on the entered coordinate0 and the choosed traget nuclei.
        test.

        Parameters
        ----------
        reference_point : str
            researcher chooses the started point, (options: bregma or lambda)
        coordinate0 : List[float]
            coordinates in AP, ML, DV axis belonging to the choosed reference point in the current mouse.
       
        Returns
        -------
        list : List[float]
            a list with the resultant coordinates [AP, ML, DV]
        """

        if self.reference_point == "lambda":
            ap = self.coordinate0[0] + self.lambda_range[self.__cuadro_chido]

        else:  # using the "bregma"
            ap = self.coordinate0[0] + self.bregma_range[self.__cuadro_chido]
        ml = self.coordinate0[1] + self.__xRange[self.__cuadro_chido] / 2
        vd = self.coordinate0[2] - (self.__yRange[self.__cuadro_chido] / 2 + self.dorso_range[self.__cuadro_chido])

        return [round(ap, 1), round(ml, 1), round(vd, 1)]

    def update_logbook(self, coordinates_result):
        """Print the resultant coordinates and mouse characteristics to use as lab-book"""
        logbook = open("logbook.txt", "w")
        logbook.write("Nucleus database used was: " + self.database_filename + "\n" +
                       "My reference point was: " + self.reference_point + "\n" +
                       "My initial coordinates were: " + str(self.coordinate0) + "\n" +
                       "My final coordinates to used are: " + str(coordinates_result) + "\n" +
                       str(datetime.now()) )

        logbook.close()

    def print_debugfile(self):
        """Save debuging messages at 'debug_file.log'"""
        logging.debug("Indice cuadro chido= " + str(self.__cuadro_chido))
        logging.debug("xRange=" + str(self.__xRange[self.__cuadro_chido]))
        logging.debug("yRange=" + str(self.__yRange[self.__cuadro_chido]))
        logging.debug("area=" + str(self.__area[self.__cuadro_chido]))

        logging.debug("lambda_range=" + str(self.lambda_range[self.__cuadro_chido]))
        logging.debug("x_range/2=" + str(self.__xRange[self.__cuadro_chido] / 2))
        logging.debug("y_range/2=" + str(self.__yRange[self.__cuadro_chido] / 2))