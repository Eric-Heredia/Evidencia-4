import pytest
from MaquinaFototerapia import MaquinaFototerapia

def test_encender_apagar():
    maquina = MaquinaFototerapia(100)
    assert maquina.encendida == False  # Inicialmente apagada
    maquina.encender()
    assert maquina.encendida == True
    maquina.apagar()
    assert maquina.encendida == False

def test_ajustar_intensidad_limites():
    maquina = MaquinaFototerapia(100)
    maquina.ajustar_intensidad(0)
    assert maquina.intensidad == 0
    maquina.ajustar_intensidad(100)
    assert maquina.intensidad == 100
    with pytest.raises(ValueError):
        maquina.ajustar_intensidad(101)
    with pytest.raises(ValueError):
        maquina.ajustar_intensidad(-1)
