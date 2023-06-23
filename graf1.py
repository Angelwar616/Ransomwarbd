import tkinter as tk#se importa la interfaz grafica
from tkinter import messagebox, filedialog#se importa una caja de dialogo
from cryptography.fernet import Fernet#Se importa la libreria que implementara datos de cifrado simetrico que usa el algoritmo AES
import os#Modulo que permite la interaccion con el sistema operativo


class App:
    def __init__(self):#se utiliza una instancia de la ventana principal utilizando la libreria ktinker
        self.ventana = tk.Tk()

        self.Llave_desc = ""
        self.directorio = 'D:\\8vo semestre\\Seguridad\\EncripPb'#usa el directorio
        #imprime en una interfaz grafica
        self.lblrt = tk.Label(self.ventana, text="Busque el archivo para el desencriptado:")
        self.lblrt.pack()

        self.dir_archivo = tk.Text(self.ventana, height=1, width=50)
        self.dir_archivo.pack()

        self.btnbsc = tk.Button(self.ventana, text="Buscar", command=self.seleccionar_archivo)
        self.btnbsc.pack()

        self.BtnDsc = tk.Button(self.ventana, text="Desencriptar!", command=self.desencriptar_archivos,
                                            state=tk.DISABLED)
        self.BtnDsc.pack()

        self.ventana.mainloop()#bucle para que la ventana sea visible y responda a modificaciones
        
    def remover_readme(self):#encargado de eliminar el archivo generado al encriptar readme.txt
        Ruta = os.path.join(self.directorio, "readme.txt")
        if os.path.isfile(Ruta):
            os.remove(Ruta)
            messagebox.showinfo("Archivo eliminado", "¡El archivo readme.txt ha sido removido exitosamente!")
        else:
            messagebox.showwarning("Archivo no encontrado", "El archivo readme.txt no existe en la carpeta.")
            
    def seleccionar_archivo(self):#al momento de hacer la navegacion abre una ventana para buscar el archivo
        self.Llave_desc = filedialog.askopenfilename()#guarda lo seleccionado
        self.dir_archivo.delete("1.0", tk.END)
        self.dir_archivo.insert(tk.END, self.Llave_desc)#actualiza el contenido
        self.BtnDsc.config(state=tk.NORMAL)#con la ruta seleccionada habilita el boton desencriptar

    def desencriptar_archivos(self):#se ejecuta cuando se activa el boton desencriptar
        if self.Llave_desc:
            self.remover_readme()       #llama a la instancia remover     
            with open(self.Llave_desc, "r") as file:# Lee la clave de desencriptación desde el archivo de rescate
                clave = file.read().strip()

            # Desencriptar archivos
            self.decrypt_directory(self.directorio, clave)#desencripta el archivo utilizando la clave

            messagebox.showinfo("Desencriptado completado", "¡Archivos desencriptados exitosamente!")
            

    def decrypt_file(self, file_path, clave):#toma la ruta y la clave para desencriptar
        cipher = Fernet(clave.encode())  # Convertir la clave a bytes
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

    def decrypt_directory(self, directory_path, clave):#toma los directorios y la clave, y recorre todos los directorios y subdirectorios
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(file_path, clave) #desencripta el archivo con la clave   


App()#crea una instancia app 

