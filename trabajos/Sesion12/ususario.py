
class ciudadano():
    def __init__(self):

        self.__Nombre=None
        self.__Apellido=None
        self.__Edad=None
        self.__Documento=None

 #-----------------GET---------------#
    def get_Nombre(self):
        return self.__Nombre
    
    def get_Apellido(self):
        return self.__Apellido
    
    def get_Edad(self):
        return self.__Edad
    
    def get_Documento(self):
        return self.__Documento

 #-------------------SET-------------#

    def set_Nombre(self, Nombre):
        self.__Nombre=Nombre

    def set_Apellido(self, Apellido):
        self.__Apellido=Apellido

    def set_Edad(self, Edad):
        self.__Edad=int(Edad)

    def set_Documento(self, Valor_Documento):
        if len(Valor_Documento) >= 8 and len(Valor_Documento) <= 12:
            self.__Documento = Valor_Documento
        else:
            self.__Documento=None
            print('-----------Documento no válido--------------')


    def Mayor_Edad(self):
        if self.__Edad >= 18:
            print('----------- Eres legal-----------\n')
        else:
            print('-----------Eres ilegal------------\n')

    
    def Sobrecarga(self):
        print(f'es un buen ciudadano')




        

class policia(ciudadano):
    
    def _init_(self):
        ciudadano().__init__()
        self.Nplaca=None
        self.rango=None

    def get_Nplaca(self):
        return self.Nplaca
    
    def set_Nplaca(self, placa):
        if len(placa) >= 3 and len(placa) <= 6:
            self.Nplaca = placa
        else:
            self.Nplaca=None
            print('-----------NO es un policia!!!--------------')

    def get_rango(self):
        return self.rango
    
    def set_rango(self, rango):
        self.rango=rango

    def Sobrecarga(self):
        print(f'{self.get_Nombre()}  {self.get_Apellido()} es un gran policia')






class psicologia(ciudadano):
    
    def __init__(self):
        ciudadano().__init__()
        self.licencia=None
        self.especialidad=None

    def get_licencia(self):
        return self.licencia
    
    def set_licencia(self, licencia):
        if len(licencia) >= 4 and len(licencia) <= 8:
            self.licencia = licencia
        else:
            self.licencia = None
            print('-----------El psicologo no tiene licencia--------------')

    def get_especialidad(self):
        return self.especialidad
    
    def set_especialidad(self, especialidad):
        self.especialidad=especialidad

            





        

class profesor(ciudadano):

    def __init__(self):
        ciudadano().__init__()
        self.Nclase=None
        self.materia=None

    def get_Nclase(self):
        return self.Nclase
    
    def set_Nclase(self, Nclase):
        if len(Nclase) >= 0 and len(Nclase) <= 4:
            self.Nclase = Nclase
        else:
            self.Nclase = None
            print('-----------El numero de clase no existe--------------')

    def get_materia(self):
        return self.materia
    
    def set_materia(self, materia):
        self.materia=materia

 













            
        
             
def inicio():
    Persona=ciudadano()
    hijo1=policia()
    hijo2=psicologia()
    hijo3=profesor()


    while True:
        

        print('--------------------policia-----------------')
        hijo1.set_Nombre(input('Nombre: '))
        hijo1.set_Apellido(input('Apellido: '))
        hijo1.set_Edad(input('Edad: '))
        hijo1.set_Documento(input('Documento: '))
        hijo1.set_Nplaca(input('Ingrese se #placa: '))
        hijo1.set_rango(input('Rango: '))
        

        print('--------------------psicologia--------------------')
        hijo2.set_Nombre(input('Nombre: '))
        hijo2.set_Apellido(input('Apellido: '))
        hijo2.set_Edad(input('Edad: '))
        hijo2.set_Documento(input('Documento: '))
        hijo2.set_licencia(input('licencia: '))
        hijo2.set_especialidad(input('especialidad: '))
        

        print('----------------------profesor---------------------')
        hijo3.set_Nombre(input('Nombre: '))
        hijo3.set_Apellido(input('Apellido: '))
        hijo3.set_Edad(input('Edad: '))
        hijo3.set_Documento(input('Documento: '))
        hijo3.set_Nclase(input('Ingrese #clase: '))
        hijo3.set_materia(input('materia: '))


        print('\n\n\n\n\n________________________________________________________________________________________________\n')
        
        print('--------------------policia-----------------')
        print(f'Nombre: {hijo1.get_Nombre()}')
        print(f'Apellido: {hijo1.get_Apellido()}')
        print(f'Edad: {hijo1.get_Edad()}')
        print(f'Documneto: {hijo1.get_Documento()}')
        print(f'#placa: {hijo1.get_Nplaca()}')
        print(f'rango: {hijo1.get_rango()}')
        hijo1.Mayor_Edad()
    
        print('\n--------------------psicologia--------------------')
        print(f'Nombre: {hijo2.get_Nombre()}')
        print(f'Apellido: {hijo2.get_Apellido()}')
        print(f'Edad: {hijo2.get_Edad()}')
        print(f'Documneto: {hijo2.get_Documento()}')
        print(f'licencia: {hijo2.get_licencia()}')
        print(f'especialidad: {hijo2.get_especialidad()}')
        hijo2.Mayor_Edad()
        print('\n----------------------profesor---------------------')
        print(f'Nombre: {hijo3.get_Nombre()}')
        print(f'Apellido: {hijo3.get_Apellido()}')
        print(f'Edad: {hijo3.get_Edad()}')
        print(f'Documneto: {hijo3.get_Documento()}')
        print(f'#clase: {hijo3.get_Nclase()}')
        print(f'materia: {hijo3.get_materia()}')
        hijo3.Mayor_Edad()

        
        print(f'{hijo1.Sobrecarga()}\n\n\n\n\n')

        

        


if __name__=='__main__':
    inicio()
