#paquetes de python
import tkinter
from tkinter import messagebox
import sqlite3 

#crear base de datos
def bd():
    try:
        base_datos    = sqlite3.connect('./BD')
        conexion      = base_datos.cursor()   

        conexion.execute("""CREATE TABLE credenciales(
                    CUENTA varchar(45) not null unique,
                    CONTRASENA varchar(45) not null);
                    """)

        base_datos.commit()
        base_datos.close()

    except:
        print('Base de datos creada')

bd()

#funcionalidades
def verificar():
    try:
        usuario     = user_variable.get()
        contrasena  = password_variable.get()

        base_datos    = sqlite3.connect('./BD')
        conexion      = base_datos.cursor()   
        conexion.execute(f"""
                            SELECT CUENTA,CONTRASENA 
                            FROM credenciales
                            WHERE CUENTA = '{usuario}' 
                                and CONTRASENA = '{contrasena}'
                        """)
        respuesta   = conexion.fetchall()
        base_datos.commit()
        base_datos.close()

        if (usuario,contrasena) in respuesta:
            messagebox.showinfo("Aprobado","Acceso exitoso")
        else:
            messagebox.showwarning("Denegado","Credenciales no validas")
    
    except:
        messagebox.showwarning("Error","Problema en BD")

    user_variable.set('')
    password_variable.set('')

def crear():
    try:
        usuario     = user_variable.get()
        contrasena  = password_variable.get()

        base_datos    = sqlite3.connect('./BD')
        conexion      = base_datos.cursor()   
        conexion.execute(f"""
                            INSERT INTO credenciales(CUENTA,CONTRASENA)
                            values('{usuario}','{contrasena}')
                        """)
        base_datos.commit()
        base_datos.close()

    except sqlite3.IntegrityError:
        messagebox.showwarning("Error","Usuario registrado")

    except:
        messagebox.showwarning("Error","Problema en BD")
 
    user_variable.set('')
    password_variable.set('')

#window
ventana = tkinter.Tk()
ventana.title('LOG-IN')
ventana.geometry('300x280')
ventana.resizable(False,False)

#variables
user_variable       = tkinter.StringVar()
password_variable   = tkinter.StringVar()

#frame
frame               = tkinter.Frame(ventana)
frame.place(x=50,y=60)

#widgets
label_usuario       = tkinter.Label(frame, text="Usuario").grid(row=1,column=1, pady=5)
label_contrasena    = tkinter.Label(frame, text="Contraseña").grid(row=2,column=1, pady=5)
entry_usuario       = tkinter.Entry(frame,textvariable=user_variable).grid(row=1,column=2, pady=5)
entry_contrasena    = tkinter.Entry(frame,textvariable=password_variable).grid(row=2,column=2, pady=5)
button_verificar    = tkinter.Button(frame,text="Verificar",command=verificar).grid(row=3,column=1, pady=5,columnspan=2)
button_crear        = tkinter.Button(frame,text="Crear nueva cuenta",command=crear).grid(row=4,column=1, pady=5,columnspan=2)

#ejecucion
ventana.mainloop()

