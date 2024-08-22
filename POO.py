class Automovil:
    def tipo_color(self, inColor, inRed, inBlue, inGreen):
        print(f"El color del auto es: {inColor}")
        print(f"Valor del rojo: {inRed}")
        print(f"Valor del azul: {inBlue}")
        print(f"Valor del verde: {inGreen}")

# Crear una instancia de Automovil y llamar al método tipo_color

Spark = Automovil()
Aveo = Automovil()
Bmw = Automovil()

Spark.tipo_color(inColor="Blue", inRed="0", inBlue="255", inGreen="0")
Aveo.tipo_color(inColor="Blue", inRed="0", inBlue="255", inGreen="0")
Bmw.tipo_color(inColor="Blue", inRed="0", inBlue="255", inGreen="0")
