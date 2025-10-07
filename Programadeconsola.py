import csv
import os
import csv
import os

# Ruta del archivo CSV donde se guardarán los contactos
archivo_contactos = 'contactos.csv'

# Función para cargar los contactos desde el archivo CSV
def cargar_contactos():
    if not os.path.exists(archivo_contactos):
        return []
    with open(archivo_contactos, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return [fila for fila in lector]

# Función para guardar los contactos en el archivo CSV
def guardar_contactos(contactos):
    with open(archivo_contactos, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'telefono', 'correo', 'cargo']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(contactos)

# Función para registrar un nuevo contacto
def registrar_contacto(contactos):
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    
    # Validar que no se repita el correo electrónico
    if any(c['correo'] == correo for c in contactos):
        print("Error: El correo electrónico ya está registrado.")
        return contactos
    
    cargo = input("Cargo dentro de la empresa: ")
    
    # Agregar el nuevo contacto
    contactos.append({'nombre': nombre, 'telefono': telefono, 'correo': correo, 'cargo': cargo})
    print(f"Contacto {nombre} registrado exitosamente.")
    return contactos

# Función para buscar un contacto por nombre o correo
def buscar_contacto(contactos):
    busqueda = input("Ingrese el nombre o correo del contacto a buscar: ")
    resultados = [c for c in contactos if busqueda.lower() in c['nombre'].lower() or busqueda.lower() in c['correo'].lower()]
    
    if not resultados:
        print("No se encontraron contactos.")
    else:
        for contacto in resultados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}, Cargo: {contacto['cargo']}")
    
# Función para listar todos los contactos
def listar_contactos(contactos):
    if not contactos:
        print("No hay contactos registrados.")
    else:
        for contacto in contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}, Cargo: {contacto['cargo']}")

# Función para eliminar un contacto
def eliminar_contacto(contactos):
    correo = input("Ingrese el correo electrónico del contacto a eliminar: ")
    contacto_eliminar = next((c for c in contactos if c['correo'] == correo), None)
    
    if contacto_eliminar:
        contactos.remove(contacto_eliminar)
        print(f"Contacto con correo {correo} eliminado exitosamente.")
    else:
        print("No se encontró el contacto con ese correo.")

# Función principal que muestra el menú
def mostrar_menu():
    contactos = cargar_contactos()
    
    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Registrar un nuevo contacto")
        print("2. Buscar un contacto")
        print("3. Listar todos los contactos")
        print("4. Eliminar un contacto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            contactos = registrar_contacto(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            listar_contactos(contactos)
        elif opcion == '4':
            eliminar_contacto(contactos)
        elif opcion == '5':
            guardar_contactos(contactos)
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el programa
if __name__ == "__main__":
    mostrar_menu()
