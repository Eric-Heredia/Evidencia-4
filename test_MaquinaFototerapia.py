import pytest
from MaquinaFototerapia import MaquinaFototerapia

@pytest.mark.parametrize("id, potenciaMaxima, estadoInicial, intensidadFinal", [
    (1, 100, "OFF", 50),
    (2, 150, "ON", 120),
    (3, 50, "OFF", 50),
])

def test_maquina_fototerapia(id, potenciaMaxima, estadoInicial, intensidadFinal):
    maquina = MaquinaFototerapia(id, potenciaMaxima)
    maquina.encender() if estadoInicial == "ON" else maquina.apagar()
    maquina.ajustarIntensidad(intensidadFinal)
    assert maquina._id == id
    assert maquina._encendida == estadoInicial
    assert maquina._intensidad == intensidadFinal
    assert maquina._potenciaMaxima == potenciaMaxima
