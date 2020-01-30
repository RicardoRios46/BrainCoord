import numpy as np


class Nucleo():
    database_filename = "nombre del archivo"
    reference_point = None  # lambda o bregma
    n_points = 0
    coordinate0 = [0, 0, 0]

    # Estas variables contendran columnas con la info de las coordenadas
    lambda_range = None
    bregma_range = None
    medioLateral_range = None
    dorsoVentral_range = None

    def __init__(self, database_filename):
        self.database_filename = database_filename

    def read_list(self):
        dataset = np.genfromtxt(self.database_filename, skip_header=1, delimiter=",", usecols=(range(6))) # Cargamos el .csv, no tomamos el header y solo carmaos las primeras 5 columnas
        dataset = dataset[~np.isnan(dataset).any(axis=1)] # Eliminamos las filas con NaNs
        # Rellenamos las variables del objeto con la info de la tabla
        self.lambda_range = dataset[:,0]
        self.bregma_range = dataset[:,1]
        self.medioLateral_range = dataset[:,2:4]
        self.dorsoVentral_range = dataset[:,4:6]
        # El numero total de filas
        self.n_points = self.bregma_range.size

        print("carga la lista")

    def create_point(self):
        print("crea el punto intermedio a paritr de la lista")

    def get_coordinates(self):
        print("")
        return [0, 0, 0]

    def update_bitacore(self):
        print("Actualizar e impimir bitacora")
