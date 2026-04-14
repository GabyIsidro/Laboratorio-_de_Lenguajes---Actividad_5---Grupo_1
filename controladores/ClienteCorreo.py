from modelos.cuenta import Cuenta # Importo la clase Cuenta
from modelos.contacto import Contacto # Importo la clase Contacto
from modelos.correo import Correo # Importo la clase Correo

# Clase ClienteCorreo
class ClienteCorreo(object):
    # Metodo constructor
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.contactos = []
        self.correosRecibidos = []
        self.correosEnviados = []

    # Metodo para agregar un contacto
    def agregarContacto(self, unContacto):
        self.contactos.append(unContacto)

    # Metodo para agregar un correo recibido
    def agregarCorreoRecibido(self, unCorreo):
        self.correosRecibidos.append(unCorreo)
    
    # Metodo para enviar un correo
    def enviarCorreo(self, unCorreo):
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
            if correoLeido == False:
                noLeidos += 1
        return noLeidos
    
    # Metodo para obtener la cantidad de contactos
    def cantidadContactos(self):
        return len(self.contactos)