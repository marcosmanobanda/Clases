class Vehiculo:
    # Creación de la clase Vehiculo como se vio en clases.

    class Vehiculo:
        def __init__(self, color, modelo, placa, valor, cilindraje, anio, tipo_puertas,
                     combustible, kilometraje, caja_cambios, seguro, gama, chasis,
                     pais_origen, marca, llanta_emergencia, numero_puertas):
            self.color = color
            self.modelo = modelo
            self.placa = placa
            self.valor = valor
            self.cilindraje = cilindraje
            self.anio = anio
            self.tipo_puertas = tipo_puertas
            self.combustible = combustible
            self.kilometraje = kilometraje
            self.caja_cambios = caja_cambios
            self.seguro = seguro
            self.gama = gama
            self.chasis = chasis
            self.pais_origen = pais_origen
            self.marca = marca
            self.llanta_emergencia = llanta_emergencia
            self.numero_puertas = numero_puertas

        # Métodos
        def vender(self):
            print("Vehículo vendido.")

        def acelerar(self):
            print("El vehículo está acelerando.")

        def frenar(self):
            print("El vehículo está frenando.")

        def girar(self):
            print("El vehículo está girando.")

        def encender(self):
            print("El vehículo ha sido encendido.")

        def apagar(self):
            print("El vehículo ha sido apagado.")

        def __str__(self):
            return f'Vehiculo: {self.__dict__}'
