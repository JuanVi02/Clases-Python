_author_ = "Juan Vicente"

print("=" * 60)
print("Primer Pre Entrega")
print("=" * 60)

usuarios = {}

def registrar_usuario():
    while True:
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("El nombre de usuario ya existe. Intente nuevamente.")
            continue

        contrasena = input("Ingrese una contraseña: ")
        usuarios[nombre_usuario] = contrasena
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        break

def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario, contrasena in usuarios.items():
            print(f"- Usuario: {usuario}, Contraseña: {contrasena}")

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("El usuario no existe.")
        return
    contrasena = input("Ingrese su contraseña: ")
    if usuarios[nombre_usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")

def menu_principal():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            iniciar_sesion()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "_main_":
    menu_principal()