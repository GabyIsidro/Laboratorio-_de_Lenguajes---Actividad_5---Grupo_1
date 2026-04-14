class Cuenta(object):
  def __init__(self, nombreUsuario, direccionMail, entrada, salida):
    # Validaciones
    if not nombreUsuario:
      raise ValueError("El nombre de usuario no puede estar vacio.")
    
    if "@" not in direccionMail or "." not in direccionMail:
      raise ValueError("La direccion de la mail de la cuenta no es valida.")

    if not entrada or not salida:
      raise ValueError("Los servidores de entrada y salida no pueden estar vacios.")
    
    # Atributos
    self.nombreUsuario = nombreUsuario
    self.direccionMail = direccionMail
    self.entrada = entrada
    self.salida = salida
