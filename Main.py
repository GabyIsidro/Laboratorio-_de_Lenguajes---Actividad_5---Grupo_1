import os
from modelos.Cuenta import Cuenta
from modelos.Contacto import Contacto
from modelos.Correo import Correo
from controladores.ClienteCorreo import ClienteCorreo

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def seleccionar_contacto(cliente, titulo):
    """Función auxiliar para elegir un contacto de la lista."""
    if not cliente.contactos:
        print("\n[!] La agenda está vacía. Ingrese el mail manualmente.")
        return input("Ingrese dirección de mail: ")
    
    print(f"\n--- {titulo} ---")
    for i, c in enumerate(cliente.contactos):
        print(f"{i+1}. {c.nombre} {c.apellido} ({c.direccionMail})")
    print(f"{len(cliente.contactos)+1}. Escribir mail manualmente")
    
    opc = int(input("\nSeleccione una opción: "))
    if 1 <= opc <= len(cliente.contactos):
        return cliente.contactos[opc-1].direccionMail
    else:
        return input("Ingrese dirección de mail: ")

def main():
    mi_cuenta = Cuenta("User", "testuser@unsada.edu.ar", "pop.unsada.edu", "smtp.unsada.edu")
    cliente = ClienteCorreo(mi_cuenta)

    while True:
        print("\n" + "="*30)
        print(f" CLIENTE DE CORREO - {mi_cuenta.direccionMail}")
        print("="*30)
        print("1. Agregar Contacto")
        print("2. Ver Agenda de Contactos")
        print("3. Simular Recepción de Correo (Usar Contacto)")
        print("4. Enviar un Correo (A un Contacto)")
        print("5. Leer Correos Recibidos")
        print("6. Ver Estadísticas")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                mail = input("Email: ")
                cliente.agregarContacto(Contacto(nombre, apellido, mail))
                print("¡Contacto guardado!")

            elif opcion == "2":
                print("\n--- AGENDA ---")
                # SE AGREGA LA CANTIDAD TOTAL DE CONTACTOS AL PRINCIPIO
                print(f"TOTAL: {cliente.cantidadContactos()} contacto(s) guardado(s).") 
                for c in cliente.contactos:
                    print(f"- {c.nombre} {c.apellido} ({c.direccionMail})")
                if not cliente.contactos: print("Vacía.")

            elif opcion == "3":
                remitente = seleccionar_contacto(cliente, "SELECCIONAR REMITENTE")
                asunto = input("Asunto: ")
                mensaje = input("Mensaje: ")
                cliente.agregarCorreoRecibido(Correo(asunto, mensaje, remitente, [mi_cuenta.direccionMail]))
                print("¡Correo recibido!")

            elif opcion == "4":
                destinatario = seleccionar_contacto(cliente, "SELECCIONAR DESTINATARIO")
                asunto = input("Asunto: ")
                mensaje = input("Mensaje: ")
                cliente.enviarCorreo(Correo(asunto, mensaje, mi_cuenta.direccionMail, [destinatario]))
                print("¡Correo enviado!")

            elif opcion == "5":
                if not cliente.correosRecibidos:
                    print("Bandeja vacía.")
                else:
                    print("\n--- BANDEJA DE ENTRADA ---")
                    for i, cor in enumerate(cliente.correosRecibidos):
                        tag = "[NUEVO]" if not cor.leido else "[LEÍDO]"
                        print(f"{i+1}. {tag} {cor.asunto} (De: {cor.remitente})")
                    
                    idx = int(input("\nVer correo nro: ")) - 1
                    if 0 <= idx < len(cliente.correosRecibidos):
                        correo = cliente.correosRecibidos[idx]
                        print(f"\nDe: {correo.remitente}\nAsunto: {correo.asunto}\n{'-'*20}\n{correo.mensaje}\n{'-'*20}")
                        
                        if not correo.leido:
                            confirmar = input("¿Marcar como leído? (s/n): ")
                            if confirmar.lower() == 's':
                                correo.marcarLeido()
                    else:
                        print("Opción inválida.")
                        
            elif opcion == "6":
                print("\n--- ESTADÍSTICAS ---")
                # SE AGREGA LA CANTIDAD TOTAL DE CORREOS PRIMERO
                print(f"Cantidad total de correos (Recibidos + Enviados): {cliente.cantidadCorreos()}")
                # SE MUESTRAN LOS DESGLOSES
                print(f"Recibidos: {cliente.cantidadCorreosRecibidos()} | Enviados: {cliente.cantidadCorreosEnviados()}")
                print(f"Sin leer: {cliente.cantidadCorreosNoLeidos()}")
                # SE AGREGA LA CANTIDAD DE CONTACTOS EN ESTADÍSTICAS
                print(f"Cantidad total de contactos: {cliente.cantidadContactos()}")

            elif opcion == "0": 
                break
        except Exception as e:
            print(f"\n[!] Error: {e}")

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()