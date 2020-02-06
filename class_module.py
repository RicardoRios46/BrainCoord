import numpy as np


class Nucleo():
    """A class used for each nuclei to identify.
    
    ...
    
    
    Atributes
    ---------
    database_filename : str
        file type .csv that contain the list of coordinates per nuclei
    reference_point : str
        reseracher choose point, (options bregma or lambda)
     coordinate0 : float
         coordinates in AP, ML, DV axis belonging to the choosed reference point in the current mouse
    
    Methods
    -------
    read_list(.csv file)
        Reads the dataset with the coordinates list of the target nuclei, organizated as lambda, bregmba, ML, DV. 
    create_point
        Calculates the central point of the target nuclei at the position of the biggest area.
    get_coordinates
        Gives the resultant coordinates to move on, based on the coordinate0 and the traget nuclei.
    def update_bitacore 
        Print the resultant coordinates and mouse characteristics to use as lab-book.
   """
    
    # Atributos públicos de los inputs.
    database_filename = "nombre del archivo"
    reference_point = None  # lambda o bregma
    coordinate0 = [0, 0, 0]

    # Atributos públicos. Estas variables contendran columnas con la info de las coordenadas
    lambda_range = None
    bregma_range = None
    medio_range = None
    lateral_range = None
    dorso_range = None
    ventral_range = None
    n_points = 0

    def __init__(self, database_filename, reference_point, coordinate0):
        self.database_filename = database_filename
        self.reference_point = reference_point
        self.coordinate0 = coordinate0

        # Atributos privados
        self.__xRange = None
        self.__yRange = None
        self.__area = None
        self.__cuadro_chido = 0

    def __find_cuadro_chido(self):
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

        """ Docummenting function blah blah blah"""
        # ToDo revisar el caso cuando solo hay una fila
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(
            range(6)))  # Cargamos el .csv, no tomamos el header y solo carmaos las primeras 5 columnas
        dataset = dataset[~np.isnan(dataset).any(axis=1)]  # Eliminamos las filas con NaNs
        print(dataset[3,:])
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(range(6))) # Cargamos el .csv, no tomamos el header y solo cargamos las primeras 5 columnas
        dataset = dataset[~np.isnan(dataset).any(axis=1)] # Eliminamos las filas con NaNs
        # Rellenamos las variables del objeto con la informción de la tabla
        self.lambda_range = dataset[:, 0]
        self.bregma_range = dataset[:, 1]
        self.lateral_range = dataset[:, 2]
        self.medio_range = dataset[:, 3]
        self.dorso_range = dataset[:, 4]
        self.ventral_range = dataset[:, 5]
        # El número total de filas
        self.n_points = self.bregma_range.size

    def create_point(self):
        # Obtenemos las distancias de los cuadrados en la base de datos
        self.__xRange = self.medio_range - self.lateral_range
        self.__yRange = self.ventral_range - self.dorso_range
        # Obtenemos el area de los cuadrados en la base de datos
        self.__area = abs(self.__xRange * self.__yRange)
        self.__cuadro_chido = self.__find_cuadro_chido()

        # Prints para debuug
        print("indice cuadro chido= ", self.__cuadro_chido)
        print("xRange=", self.__xRange[self.__cuadro_chido])
        print("yRange=",self.__yRange[self.__cuadro_chido])
        print("area=" + str(self.__area[self.__cuadro_chido]))

    def get_coordinates(self):
        if self.reference_point == "lambda":
            ap = self.coordinate0[0] + self.lambda_range[self.__cuadro_chido]

        else: # Estamos en "bregma"
            ap = self.coordinate0[0] + self.bregma_range[self.__cuadro_chido]
        ml = self.coordinate0[1] + self.__xRange[self.__cuadro_chido] / 2
        vd = self.coordinate0[2] - (self.__yRange[self.__cuadro_chido] / 2 + self.dorso_range[self.__cuadro_chido])

        # Prints para debug ToDo ponerlos para logging
        print("lambda_range=", self.lambda_range[self.__cuadro_chido])
        print("x_range/2=", self.__xRange[self.__cuadro_chido] / 2)
        print("y_range/2=", self.__yRange[self.__cuadro_chido] / 2)

        return [round(ap,1), round(ml,1), round(vd,1)]

    # ToDo Implementar una bitacora
    def update_bitacore(self):
        print("Actualizar e impimir bitacora")
