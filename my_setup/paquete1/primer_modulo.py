class Cliente():

    def __init__(self,nombre,email,direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = []

    def datos_usuario(self):
        print(f"Nombre:{self.nombre}\nE-mail:{self.email}\nDireccion:{self.direccion}")

    def realizar_pedido(self,producto,cantidad):
        if producto == "computadora" or producto == "telefono" or producto == "tablet":
            self.carrito.append((producto,cantidad))
            print(f"Se ha agregado al carrito la cantidad total de:{cantidad},del siguiente producto:{producto}.El mismo sera enviado a:{self.direccion}.\nLa factura correspondiente fue enviada a {self.email}")
        else:
            print("Recuerda seleccionar solo uno de los 3 productos disponibles.")

    def mostrar_pedido(self):
        for producto,cantidad in self.carrito:
            print(f"Productos en carrito:{producto}\nCantidad:{cantidad}")
    def main(self):
        while True:
            print("Bienvenido!!\nPodras realizar un pedido opcion (1)\nver el pedido realizado opcion (2)\nver tus datos de usuario(3)\nsalir del programa(4)")

            opcion = input("Selecciona opcion 1,2,3,4")
            if opcion == "1":
                print("Productos disponibles: computadora,telefono,tablet.(elige uno de ellos).\nTambien puede elegir la cantidad que desees.")
                producto = input("Nombre del producto")
                cantidad = input("Ingresa la cantidad deseada:")
                self.realizar_pedido(producto,cantidad)
            elif opcion == "2":
                self.mostrar_pedido()
            elif opcion == "3":
                self.datos_usuario()
            elif opcion == "4":
                print("Gracias por probar el programa")
                break
            else:
                print("Opcion invalida,intentelo nuevamente")

    def __str__(self):
        return f"Nombre:{self.nombre}\nE-mail:{self.email}\nDireccion:{self.direccion}Producto:{self.producto}"