class Contacto:
    def __init__(self,nombre, apellido, mail):
        #aplica al contacto el nombre ingresado por parametro
        self.nombre = nombre

        #aplica al contacto el apellido ingresado por parametro
        self.apellido = apellido

        #valida el mail ingresado por parametro
        for i in (mail):
            if i == "@":
                arroba += 1
            elif (i== ".") :
                punto = True
        if (arroba == 1 and punto) :
            usuario, dominio = mail.split("@")
            if usuario and dominio:
                #aplica al contacto el mail ingresado por parametro
                self.mail = mail
        raise ValueError ("el mail no es valido")
        
