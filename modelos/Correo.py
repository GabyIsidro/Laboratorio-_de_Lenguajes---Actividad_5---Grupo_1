class Correo(object):
    def __init__(self, asunto, mensaje, remitente, destinatarios):
        # Validaciones
        if not asunto:
            raise ValueError("El asunto no puede estar vacío.") 
        if not mensaje:
            raise ValueError("El mensaje no puede estar vacío.")
        if "@" not in remitente or "." not in remitente:
            raise ValueError("El remitente no es un correo válido.")
        if not destinatarios:
            raise ValueError("Debe haber al menos un destinatario.")
        for d in destinatarios:
            if "@" not in d or "." not in d:
                raise ValueError(f"El destinatario '{d}' no es válido.")

        # Atributos
        self.asunto = asunto
        self.mensaje = mensaje
        self.remitente = remitente
        self.destinatarios = destinatarios
        self.leido = False

    # Método
    def marcarLeido(self):
        self.leido = True
