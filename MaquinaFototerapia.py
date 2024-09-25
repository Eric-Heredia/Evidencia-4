class MaquinaFototerapia:
    def __init__(self, id, potencia, tiempoSesion):
        self._id = id
        self._potencia = potencia
        self._encendida = False
        self._tiempoSesion = tiempoSesion

    def encender(self):
        self._encendida = True


    def apagar(self):
        self._encendida = False
        

    def ajustarPotencia(self, nuevaPotencia):
        if not 0 <= nuevaPotencia <= self._potencia:
            raise ValueError("Intensidad fuera de rango")
        self._Potencia = nuevaPotencia


    def obtenerEstado(self):
        return {
            "encendida": self._encendida,
            "potencia": self._potencia,
            "tiempoSesion": self._tiempoSesion,
        }


    def __str__(self):
        if self._encendida:
            return f"Máquina de fototerapia {self._id} se encuentra ON, su Potencia es de {self._potencia} nm, y el tiempo de la Sesión es de {self._tiempoSesion} min."
        else:
            return f"Máquina de fototerapia {self._id} se encuentra OFF."


maquina1 = MaquinaFototerapia(1, 100, 25)
maquina2 = MaquinaFototerapia(2, 150, 30)
maquina3 = MaquinaFototerapia(3, 125, 45)

maquina1.encender()
maquina2.encender()
maquina3.encender()

maquina1.ajustarPotencia(80)
maquina2.ajustarPotencia(120)
maquina3.ajustarPotencia(100)


print(maquina1)
print(maquina2)
print(maquina3)

maquina2.apagar()

print(maquina2)