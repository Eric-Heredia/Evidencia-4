class MaquinaFototerapia:
    def __init__(self, potencia_maxima):
        self.encendida = False
        self.intensidad = 0
        self.potencia_maxima = potencia_maxima
        self.tiempo_sesion = 0
        self.usuario_actual = None

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def ajustar_intensidad(self, nueva_intensidad):
        if 0 <= nueva_intensidad <= self.potencia_maxima:
            self.intensidad = nueva_intensidad
        else:
            print("Intensidad fuera de rango.")

    def iniciar_sesion(self, usuario):
        # Simulación básica de autenticación
        usuarios_validos = {"usuario1": "contraseña1", "usuario2": "contraseña2"}
        if usuario in usuarios_validos:
            self.usuario_actual = usuario
            print(f"Usuario {usuario} inició sesión.")
        else:
            print("Usuario o contraseña incorrectos.")

    def obtener_estado(self):
        return {
            "encendida": self.encendida,
            "intensidad": self.intensidad,
            "potencia_maxima": self.potencia_maxima,
            "tiempo_sesion": self.tiempo_sesion,
            "usuario_actual": self.usuario_actual
        }

    def __str__(self):
        return f"Máquina de fototerapia: Encendida: {self.encendida}, Intensidad: {self.intensidad}, Potencia máxima: {self.potencia_maxima}, Usuario actual: {self.usuario_actual}"
