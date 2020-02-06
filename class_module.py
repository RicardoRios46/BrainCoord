import numpy as np


class Nucleo():
    """A class used for each nuclei to identify.
    
    ...
    
    
    Atributes
    ---------
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
    read_list(.csv file)
        Reads the dataset with the coordinates list of the target nuclei, organizated as lambda, bregma, ML, DV. 
    create_point
        Calculates the central point of the target nuclei at the position of the biggest area.
    get_coordinates
        Gives the resultant coordinates to move on, based on the coordinate0 and the traget nuclei.
    def update_bitacore 
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
        coordinate0 : float
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
        """ Calculates the AP coordinate with the biggest area of the target nuclei."""
        
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
        """Reads the dataset with the coordinates list of the target nuclei, organizated as lambda, bregma, medial,                 lateral, dorsal, ventral.
        
        ----------
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
        """
       
        # ToDo: check the case in which just one raw is entered.
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(
            range(6)))  # Upload the .csv, omit the header and consider the 5 columns
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Eliminate the columns with NaNs
        print(dataset[3,:])
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(range(6))) # Upload the             .csv, omit the header and consider the 5 columns
        dataset = dataset[~np.isnan(dataset).any(axis=1)] # Eliminate the columns with NaNs
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
        
        This function takes the medial value of the total longitud of the nuclei in each axis and calculates the area per           each AP coordinate. Later on, selects the biggest area. 
        """
        
        # To obtain the square from the database
        self.__xRange = self.medio_range - self.lateral_range
        self.__yRange = self.ventral_range - self.dorso_range
        # To obtain the area of the square and select the biggest one
        self.__area = abs(self.__xRange * self.__yRange)
        self.__cuadro_chido = self.__find_cuadrochido()

        # Prints for debuug
        print("indice cuadro chido= ", self.__cuadro_chido)
        print("xRange=", self.__xRange[self.__cuadro_chido])
        print("yRange=",self.__yRange[self.__cuadro_chido])
        print("area=" + str(self.__area[self.__cuadro_chido]))

    def get_coordinates(self):
        """Gives the resultant coordinates to move on, based on the entered coordinate0 and the choosed traget nuclei.
        
        Parameters
        ----------
        reference_point : str
            researcher chooses the started point, (options: bregma or lambda)
        coordinate0 : float
            coordinates in AP, ML, DV axis belonging to the choosed reference point in the current mouse.
       
        Returns
        -------
        list
            a list with the resultant coordinates [AP, ML, VD] 
        """
        
        if self.reference_point == "lambda":
            ap = self.coordinate0[0] + self.lambda_range[self.__cuadro_chido]

        else: # using the "bregma"
            ap = self.coordinate0[0] + self.bregma_range[self.__cuadro_chido]
        ml = self.coordinate0[1] + self.__xRange[self.__cuadro_chido] / 2
        vd = self.coordinate0[2] - (self.__yRange[self.__cuadro_chido] / 2 + self.dorso_range[self.__cuadro_chido])

        # Prints for debug
        print("lambda_range=", self.lambda_range[self.__cuadro_chido])
        print("x_range/2=", self.__xRange[self.__cuadro_chido] / 2)
        print("y_range/2=", self.__yRange[self.__cuadro_chido] / 2)

        return [round(ap,1), round(ml,1), round(vd,1)]

   
    def update_bitacore(self):
        """Print the resultant coordinates and mouse characteristics to use as lab-book"""
        
        print("Actualizar e impimir bitacora")
