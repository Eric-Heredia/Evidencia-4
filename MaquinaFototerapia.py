class MaquinaFototerapia:
    def __init__(self, id, potenciaMaxima):
        self._id = id
        self._potenciaMaxima = potenciaMaxima
        self._encendida = False
        self._intensidad = 0
        self._tiempoSesion = 0

    def encender(self):
        self._encendida = "ON"


    def apagar(self):
        self._encendida = "OFF"
        

    def ajustarIntensidad(self, nuevaIntensidad):
        if 0 <= nuevaIntensidad <= self._potenciaMaxima:
            self._intensidad = nuevaIntensidad
        else:
            raise ValueError("Intensidad fuera de rango.")

    def obtenerEstado(self):
        return {
            "encendida": self._encendida,
            "intensidad": self._intensidad,
            "potenciaMaxima": self._potenciaMaxima,
            "tiempoSesion": self._tiempoSesion,
        }

    def __str__(self):
        return f"Máquina de fototerapia {self._id} se encuentra {self._encendida}, su Intensidad es de: {self._intensidad}, y la Potencia máxima es: {self._potenciaMaxima}"

# Crear objetos
maquina1 = MaquinaFototerapia(1, 100)
maquina2 = MaquinaFototerapia(2, 150)
maquina3 = MaquinaFototerapia(3, 125)

maquina1.encender()
maquina2.encender()
maquina3.encender()
maquina1.ajustarIntensidad(80)
maquina2.ajustarIntensidad(120)
maquina3.ajustarIntensidad(100)

print(maquina1)
print(maquina2)
print(maquina3)