class MaquinaFototerapia:
    def __init__(self, potencia_maxima):
        self.encendida = False
        self.intensidad = 0
        self.potencia_maxima = potencia_maxima
        self.tiempo_sesion = 0

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def ajustar_intensidad(self, nueva_intensidad):
        if 0 <= nueva_intensidad <= self.potencia_maxima:
            self.intensidad = nueva_intensidad
        else:
            raise ValueError("Intensidad fuera de rango.")

    def obtener_estado(self):
        return {
            "encendida": self.encendida,
            "intensidad": self.intensidad,
            "potencia_maxima": self.potencia_maxima,
            "tiempo_sesion": self.tiempo_sesion,
        }

    def __str__(self):
        return f"Máquina de fototerapia: Encendida: {self.encendida}, su Intensidad es: {self.intensidad}, y la Potencia máxima: {self.potencia_maxima}"
