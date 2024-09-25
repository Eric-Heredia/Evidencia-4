import pytest
from MaquinaFototerapia import MaquinaFototerapia

@pytest.mark.parametrize("id, potencia, tiempoSesion", [
    (1, 100, 30),
    ("A123", 150, 45),
    (456, 0, 60),  # Potencia mínima
])

def test_creacion_maquina(id, potencia, tiempoSesion):
    maquina = MaquinaFototerapia(id, potencia, tiempoSesion)
    assert maquina._id == id
    assert maquina._potencia == potencia
    assert maquina._tiempoSesion == tiempoSesion
    assert not maquina._encendida


def test_encender_apagar():
    maquina = MaquinaFototerapia(1, 100, 30)
    maquina.encender()
    assert maquina._encendida
    maquina.apagar()
    assert not maquina._encendida

def test_obtener_estado():
    maquina = MaquinaFototerapia(1, 100, 30)
    maquina.encender()
    estado = maquina.obtenerEstado()
    assert estado == {"encendida": True, "potencia": 100, "tiempoSesion": 30}

def test_str_representation():
    maquina = MaquinaFototerapia(1, 100, 30)
    maquina.encender()
    assert str(maquina) == "Máquina de fototerapia 1 se encuentra ON, su Potencia es de 100 nm, y el tiempo de la Sesión es de 30 min."
    maquina.apagar()
    assert str(maquina) == "Máquina de fototerapia 1 se encuentra OFF."
