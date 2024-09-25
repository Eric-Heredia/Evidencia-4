import pytest
from MaquinaFototerapia import MaquinaFototerapia


@pytest.mark.parametrize("id, potenciaMaxima, estadoInicial, intensidadFinal", [
    # valores aceptables
    (1, 100, False, 50),
    (2, 150, True, 120),
    (3, 50, False, 50),

    # valores fuera de rango
    (4, 100, True, -10),  # Intensidad negativa
    (5, 100, True, 110),  # Intensidad mayor a la potencia máxima

    # Valores límite
    (6, 100, True, 0),
    (7, 100, True, 100),

    # Cambiar la intensidad cuando está apagada
    (8, 100, False, 50),

    
    # Potencia máxima muy pequeña
    (9, 1, True, 1),

    # Potencia máxima muy grande
    (10, 1000, True, 500),

    # Diferentes tipos de ID
    (11, 100, True, 50),  # Entero
    ("12", 100, True, 50),  # Cadena

])

def test_maquina_fototerapia(id, potenciaMaxima, estadoInicial, intensidadFinal, expected_error):
    maquina = MaquinaFototerapia(id, potenciaMaxima)
    maquina.encender() if estadoInicial else maquina.apagar()

    if expected_error:
        with pytest.raises(ValueError) as excinfo:
            maquina.ajustarIntensidad(intensidadFinal)
        assert str(excinfo.value) == expected_error
    else:
        maquina.ajustarIntensidad(intensidadFinal)
        # Afirmaciones sobre el estado de la máquina
        assert maquina._id == id
        assert maquina._potenciaMaxima == potenciaMaxima
        assert maquina._encendida == estadoInicial
        assert maquina._intensidad == intensidadFinal



# Test para apagar la máquina
def test_apagar():
    maquina = MaquinaFototerapia(1, 100)
    maquina.encender()
    maquina.apagar()
    assert maquina._encendida is False
    assert maquina._intensidad == 0

# Test para cambiar la intensidad cuando la máquina está apagada
def test_ajustar_intensidad_apagada():
    maquina = MaquinaFototerapia(1, 100)
    maquina.ajustarIntensidad(50)
    assert maquina._intensidad == 50

def test_ajustar_intensidad_fuera_de_rango():
    maquina = MaquinaFototerapia(1, 100)
    maquina.encender()
    with pytest.raises(ValueError):
        maquina.ajustarIntensidad(-10)
    with pytest.raises(ValueError):
        maquina.ajustarIntensidad(110)
