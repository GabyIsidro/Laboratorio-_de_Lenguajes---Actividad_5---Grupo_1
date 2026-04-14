from modelos.cuenta import Cuenta # Importo la clase Cuenta
from modelos.contacto import Contacto # Importo la clase Contacto
from modelos.correo import Correo # Importo la clase Correo

# Clase ClienteCorreo
class ClienteCorreo(object):
    # Metodo constructor
    def __init__(self, cuenta):
        #Validacion
        if not isinstance(cuenta, Cuenta):
            raise TypeError("El usuario debe ser un objeto de la clase Cuenta.")
        
        # Atributos asignados
        self.cuenta = cuenta
        self.contactos = []
        self.correosRecibidos = []
        self.correosEnviados = []

    # Metodo para agregar un contacto
    def agregarContacto(self, unContacto):
        #Validacion
        if not isinstance(unContacto, Contacto):
            raise TypeError("El contacto debe ser un objeto de la clase Contacto.")
        #Busca si el contacto ya existe
        for contactoGuardado in self.contactos:
            if contactoGuardado.direccionMail == unContacto.direccionMail:
                raise ValueError("El contacto ya existe.")
        self.contactos.append(unContacto)

    # Metodo para agregar un correo recibido
    def agregarCorreoRecibido(self, unCorreo):
        #Validacion
        if not isinstance(unCorreo, Correo):
            raise TypeError("El correo debe ser un objeto de la clase Correo.")
        self.correosRecibidos.append(unCorreo)
    
    # Metodo para enviar un correo
    def enviarCorreo(self, unCorreo):
        #Validacion
        if not isinstance(unCorreo, Correo):
            raise TypeError("El correo debe ser un objeto de la clase Correo.")
        self.correosEnviados.append(unCorreo)

    # Metodo para obtener la cantidad de correos
    def cantidadCorreos(self):
        return len(self.correosRecibidos) + len(self.correosEnviados)
    
    # Metodo para obtener la cantidad de correos recibidos
    def cantidadCorreosRecibidos(self):
        return len(self.correosRecibidos)

    # Metodo para obtener la cantidad de correos enviados
    def cantidadCorreosEnviados(self):
        return len(self.correosEnviados)

    # Metodo para obtener la cantidad de correos no leidos
    def cantidadCorreosNoLeidos(self):
        noLeidos = 0
        for correo in self.correosRecibidos:
            if correo.leido == False:
                noLeidos += 1
        return noLeidos
    
    # Metodo para obtener la cantidad de contactos
    def cantidadContactos(self):
        return len(self.contactos)