


class Producto():

    def __init__(self, nombre: str, precio: float, cantidad_productos: int):

        self.nombre=nombre
        self.precio=precio
        self.cantidad_disponible=cantidad_productos

    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_cantidad_disponible(self):
        return self.cantidad_disponible


    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_precio(self,precio):
        self.precio = precio
    def set_cantidad_disponible(self,cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible



    def info_producto(self):
        return f'{self.get_nombre()}, {self.get_precio()}, {self.get_cantidad_disponible()}'
    
    def restar_cantidad(self,cantidad):
        resta=self.get_cantidad_disponible()-cantidad
        if self.verificar_disponibilidad():
            self.set_cantidad_disponible(resta)
            return True
        return False
    
    def verificar_disponibilidad (self):
        if  self.cantidad_disponible > 0:
            return True
        return False
        

        
class snack(Producto):

    def __init__(self, nombre: str, precio: float, cantidad_productos: int, tipo:str):
        super().__init__(nombre, precio, cantidad_productos )

        self._tipo=tipo

    def get_tipo(self):
        return self._tipo  
    
    def set_tipo(self,tipo):
        self._tipo = tipo

    def info_producto(self):
        return f'{super().info_producto()}, {self.get_tipo()}, {self.verificar_disponibilidad()}'

class bebida(Producto):

    def __init__(self, nombre: str, precio: float, cantidad_productos: int, clase:str,  tamaño:str):
        super().__init__(nombre, precio, cantidad_productos )

        self._clase=clase
        self._tamaño=tamaño

    def get_clase(self):
        return self._clase
    def get_tamaño(self):
        return self._tamaño
    
    def set_clase(self, clase):
        self._clase = clase
    def set_tamaño(self,tamaño):
        self._tamaño = tamaño

    def info_producto(self):
        return f'{super().info_producto()}, {self.get_clase()}, {self.get_tamaño()}, {self.verificar_disponibilidad()}'

    
class dispensadora(Producto):

    def __init__(self, lista:list, Tventas: float):

        self.producto=[]
        self.total_ventas=Tventas

    def get_producto(self):
        return self.producto
    def get_total_ventas(self):
        return self.total_ventas
    
    def set_producto(self, producto):
        self.producto.append(producto)
    def set_total_ventas(self, Tventas):
        self.total_ventas=Tventas

    def agregar_producto(self):           
            
            tipo_producto = input('Ingrese el tipo de producto (snack/bebida): ')
            
            if tipo_producto.lower() == 'snack':
                nombre_producto = input('Ingrese el nombre del producto: ')
                precio = float(input('Ingrese el precio del producto: '))
                cantidad = int(input('Ingrese la cantidad de productos: '))
                tipo_snack = input('Ingrese el tipo de snack: ')
                nuevo_producto = snack(nombre_producto, precio, cantidad, tipo_snack)
                self.set_producto(nuevo_producto)
                print('Nuevo producto agregado.\n')
            elif tipo_producto.lower() == 'bebida':
                nombre_producto = input('Ingrese el nombre del producto: ')
                precio = float(input('Ingrese el precio del producto: '))
                cantidad = int(input('Ingrese la cantidad de productos: '))
                clase_bebida = input('Ingrese la clase de la bebida: ')
                tamaño_bebida = input('Ingrese el tamaño de la bebida: ')
                nuevo_producto = bebida(nombre_producto, precio, cantidad, clase_bebida, tamaño_bebida)
                self.set_producto(nuevo_producto)
                print('Nuevo producto agregado.\n')
            else:
                print('Tipo de producto no reconocido. Solo se permiten "snack" o "bebida".')
            

    def realizar_venta(self):
                
                if len(self.producto) > 0:
                    print('Lista de productos disponibles:')
                    for valor, producto in enumerate(self.producto):
                        print(f'{valor}. {producto.nombre}')
                    
                    opcion_producto = int(input('Ingrese el numero del producto que desea comprar: '))
                    
                    if 0 <= opcion_producto < len(self.producto):
                        cantidad_a_comprar = int(input('Ingrese la cantidad a comprar: '))
                        if self.producto[opcion_producto].restar_cantidad(cantidad_a_comprar):
                            print('Compra realizada con exito.')           
                        else:
                            print('No hay suficientes productos disponibles. ')
                    else:
                        print('Numero de producto no valido.\n')
                else:
                    print('No hay productos disponibles para comprar.\n')

    def obtener_total_ventas(self):
        total_ventas=0       
        if len(self.producto) > 0:
                if len(self.producto) > 0:
                    for valor in self.producto:
                        valor_lista=valor.info_producto().split(',')
                        costo_producto = float(valor_lista[1])
                        cantidad_vendida = int(valor_lista[2])
                        costo_total_producto = costo_producto *  cantidad_vendida
                        total_ventas += costo_total_producto
                        print(f'Total a pagar: {total_ventas}')
        else:
            print('No hay productos disponibles para mostrar.')

def inicio():
    dispensadora_instancia = dispensadora([], 0)
    while True:
        print('\n\n1. Agregar nuevo producto\n'
              '2. Comprar producto\n'
              '3. Informacion del producto\n'
              '4. Informacion de sus productos\n'
              '5. Total\n'
              '6. Exit\n')
        opcion = int(input('Ingrese #opcion: '))
        if opcion == 1:
            while True:
                opc1=input('¿Va agregar un producto?(y/n): ')
                if opc1=='y':
                    dispensadora_instancia.agregar_producto()
                elif opc1=='n':
                    break
                else:
                    print('Respuesta invalida')        
        elif opcion == 2:
            while True:
                opc2=input('¿Va comprar un producto?(y/n): ')
                if opc2=='y':
                    dispensadora_instancia.realizar_venta()
                elif opc2=='n':
                    break
                else:
                    print('Respuesta invalida')  
        elif opcion == 3:
            if len(dispensadora_instancia.producto) > 0:
                    print('Lista de productos disponibles:')
                    for valor, producto in enumerate(dispensadora_instancia.producto):
                        print(f'{valor}. {producto.nombre}')
                    
                    opcion_info= int(input('Ingrese el numero del producto que desea comprar: '))
                    
                    if 0 <= opcion_info < len(dispensadora_instancia.producto):
                        print(dispensadora_instancia.producto[opcion_info].info_producto())
                    else:
                      print('Número de producto no válido.')
        elif opcion == 4:
            pass         
        elif opcion == 5:
            dispensadora_instancia.obtener_total_ventas()
            break 
        elif opcion == 6:
            break
            






if __name__=='__main__':
    inicio()