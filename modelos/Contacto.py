class Contacto(object):
    def __init__(self,nombre, apellido, direccionMail):
        #aplica al contacto el nombre ingresado por parametro
        self.nombre = nombre

        #aplica al contacto el apellido ingresado por parametro
        self.apellido = apellido

        # Inicializa las variables para validar el mail
        arroba = 0
        punto = False

        #valida el mail ingresado por parametro
        for i in (direccionMail):
            if i == "@":
                arroba += 1
            elif (i== ".") :
                punto = True

        if (arroba == 1 and punto):
            usuario, dominio = direccionMail.split("@")
            if usuario and dominio:
                #aplica al contacto el mail ingresado por parametro
                self.direccionMail = direccionMail
                return
    
        raise ValueError (f"El mail '{direccionMail}' no es valido")