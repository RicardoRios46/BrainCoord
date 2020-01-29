import numpy as np


class Nucleo:
    database_filename = "nombre del archivo"
    reference_point = None  # lambda o bregma
    n_points = 1
    coordinate0 = [0, 0, 0]

    lambda_range = np.zeros((n_points, 1))
    bregma_range = np.zeros((n_points, 1))
    medioLateral_range = np.zeros((n_points, 2))
    dorsoVentral_range = np.zeros((n_points, 2))

    def read_list(self):
        print("carga la lista")

    def create_point(self):
        print("crea el punto intermedio a paritr de la lista")

    def get_coordinates(self):
        print("")
        return [0, 0, 0]

    def update_bitacore(self):
        print("Actualizar e impimir bitacora")
