
def test_referece_point(reference_point):
    if type(reference_point) == str:
        if reference_point == "bregma" or reference_point == "lambda":
            return True
        else:
            raise("Texto para punto de referencia Incorrecto. Inserte 'bregma' o 'lambda'")

    else:
        raise ("Texto para punto de referencia Incorrecto. Inserte 'bregma' o 'lambda'")

def 