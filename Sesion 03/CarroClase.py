class Carro:
    ruedas = 4

    def __init__(self,color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 200
        self.nacionalidad = ""


    # Metodos
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad


class CarroVolador(Carro):
    ruedas = 6
    def __init__(self,color,aceleracion,estadoVolando = False):
        super().__init__(color,aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro1 = Carro('rojo',45);


carroVol = CarroVolador('rojo',55)


print(carroVol.estadoVolando)

