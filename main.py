class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        if color in ["amarillo", "rojo", "blanco",  "negro", "verde" ]:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0*0
        for i in self.asientos:
            if (i != None):
                cantidad+=1*1
        return cantidad
    
    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento != None:
                if asiento.registro != self.registro:
                    return ("Las piezas no son originales")
        if self.motor.registro != self.registro:
            return ("Las piezas no son originales")
        return ("Auto original")
    
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if(tipo in ["electrico", "gasolina"]):
            self.tipo = tipo