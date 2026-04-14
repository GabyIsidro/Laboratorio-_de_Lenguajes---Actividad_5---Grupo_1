class Contacto(object):
    def __init__(self,nombre, apellido, direccionMail):
        # Inicializa las variables para validar el mail
        arroba = 0
        punto = False

        #valida el mail ingresado por parametro
        for i in (direccionMail):
            if i == "@":
                arroba += 1
            elif (i== ".") :
                punto = True

        if (arroba != 1 or not punto):
            raise ValueError (f"El mail '{direccionMail}' no es valido")

        usuario, dominio = direccionMail.split("@")
        if not usuario or not dominio:
            raise ValueError (f"El mail '{direccionMail}' no es valido")
    
        # Atributos asignados
        self.nombre = nombre
        self.apellido = apellido
        self.direccionMail = direccionMail