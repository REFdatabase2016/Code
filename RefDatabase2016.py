from tkinter import *
from tkinter import messagebox

##--------------------------------Ventana De Inventario------------------------------------------------------------------------##
global lista
lista=[]


def iniciarArchivo():
    archivo= open("BI.txt","a")
    archivo.close()


def cargar():
    archivo= open("BI.txt","r")
    linea= archivo.readline()
    if linea:
        while linea:
            if linea[-1] == "\n":
                linea= linea[:-1]
            lista.append(linea)
            linea=archivo.readline()
    archivo.close()


def escribirProducto():
    archivo= open("BI.txt","w")
    lista.sort()
    for elemento in lista:
	    archivo.write(elemento+"\n")
    archivo.close()



def invent():
    ventanaabrir= Toplevel()
    ventanaabrir.title("Inventario de productos")
    ventanaabrir.geometry("1920x1080")
    iniciarArchivo()
    cargar()
    r = Text(ventanaabrir,width=185, height=40)
    valores=[]
    lista.sort()
    r.insert(INSERT,"Id\t\t\t\tCantidad\t\t\t\tProducto\t\t\t\t\t\tPrecio\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[1])
        r.insert(INSERT,arreglo[0]+"\t\t\t\t\t\t"+arreglo[1]+"\t\t\t"+arreglo[2]+"\t\t\n")
    r.place(x=10,y=200)    


def modifinventario():
    global ventanainventario
    ventanainventario= Toplevel()
    ventanainventario.title("Inventario de productos")
    ventanainventario.geometry("1920x1080")
    global Id
    Id = StringVar()
    global nombre
    nombre = StringVar()
    global precio
    precio = StringVar()
    global cantidad
    cantidad = StringVar()
    global contenteliminar
    contenteliminar=StringVar()
    iniciarArchivo()
    cargar()
    consultar()
    etiquetl1=Label(ventanainventario, text="Agregar Un Producto",font=("helvetica",14)).place(x=40,y=40)
    etiquetaN=Label(ventanainventario,text="Nombre:",font=("Helvetica",12)).place(x=40,y=90)
    cajaN=Entry(ventanainventario, textvariable=nombre).place(x=130,y=90)
    etiquetap=Label(ventanainventario,text="Precio:",font=("Helvetica",12)).place(x=40,y=120)
    cajap=Entry(ventanainventario, textvariable=precio).place(x=130,y=120)
    etiquetaC=Label(ventanainventario,text="Cantidad:",font=("Helvetica",12)).place(x=40,y=150)
    cajaC=Entry(ventanainventario, textvariable=cantidad).place(x=130,y=150)
    guardarbton=Button(ventanainventario, text="Guardar",font=("Helvetica",10),command=guardar).place(x=170,y=170)
    eliminarbton=Button(ventanainventario, text="Eliminar",font=("Helvetica",10),command=eliminar).place(x=560,y=140)
    etiquetaeliminar=Label(ventanainventario,text="nombre",font=("Helvetica",10)).place(x=480,y=120)
    entradanombre=Spinbox(ventanainventario,textvariable=contenteliminar).place(x=560,y=120)
    ventanainventario.mainloop()


def consultar():
    r = Text(ventanainventario, width=185, height=40)
    valores=[]
    lista.sort()
    r.insert(INSERT,"Producto\t\t\t\t\t\tPrecio\t\t\tCantidad\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[0])
        r.insert(INSERT,arreglo[0]+"\t\t\t\t\t\t"+arreglo[1]+"\t\t\t"+arreglo[2]+"\t\n")
    r.place(x=10,y=200)
    entradanombre=Spinbox(ventanainventario,value=(valores),textvariable=contenteliminar).place(x=560,y=120)
    if lista==[]:
        entradanombre=Spinbox(ventanainventario,value=(valores)).place(x=560,y=120)
    r.config(state=DISABLED)
    

def guardar():
    n=nombre.get()
    p=precio.get()
    c=cantidad.get()
    lista.append(n+"$"+p+"$"+c)
    escribirProducto()
    nombre.set("")
    precio.set("")
    cantidad.set("")
    consultar()

def eliminar():
    eliminado=contenteliminar.get()
    removido=False
    for elemento in lista:
        arreglo=elemento.split("$")
        if contenteliminar.get()==arreglo[0]:
            lista.remove(elemento)
            removido=True
    escribirProducto()
    consultar()
   





    
 
        
    
    

##----------------------------Ventana Empleado------------------------------------------------
def ventanaempl():
    ventanaempl=Toplevel()
    ventanaempl.title=("Ventana De Empleado")
    ventanaempl.geometry("950x370")
    Mensajelbl=Label(ventanaempl, text="Haz iniciado Sesion Como Empleado",font=("Calibri",20)).place(x=150, y=20)
    Mensajelbl2=Label(ventanaempl, text="Escoje una de las sig. opciones para continuar",font=("Calibri",20)).place(x=150, y=60)
    abririnvt2=Button(ventanaempl, text="Abrir Inventario",font=("Calibri",17),command=invent).place(x=200, y=150)
    




##---------------------------------------Ventana administrador-----------------------------------------------------------------------##
def VentAdmin():
    ventanaadm= Toplevel()
    ventanaadm.Title=("Ventana De Administrador")
    ventanaadm.geometry("950x550")
    Titulo1= Label(ventanaadm, text="Bienvenido",font=("Comic Sans",25)).place(x=150, y=50)
    Titulo2= Label(ventanaadm, text="Has Iniciado Sesion Como Administrador",font=("Comic Sans",20)).place(x=150, y=150)
    mensaje=Label(ventanaadm, text="Por favor escoge una Opcion para continuar",font=("Comic Sans",20)).place(x=150, y=200)
    abririnvt=Button(ventanaadm, text="Abrir Inventario",font=("Calibri",17),command=invent).place(x=200, y=260)
    modificarinvBtn=Button(ventanaadm, text="Modificar inventario",font=("Calibri",17),command=modifinventario).place(x=450, y=260)
    cerrarvemtana=Button(ventanaadm, text="Salir", font=("Calibri",17), command=exit).place(x=380, y=325)

    ventanaadm.resizable(0,0)
   






##-----------------------------Ventana principal-----------------------------------------------------------------------------------------------##


Principal= Tk()

Principal.title("Bienvenido")
Principal.geometry("650x350")
Principal.configure(bg="#BDBDBD")
presentacion = Label(Principal, text="Bienvenido a REFdatabase2016",bg="#BDBDBD", fg="black",font=("Times New Roman", 22)).place(x=75,y=10)
presentacion2 = Label(Principal, text="Porfavor escoge un usuario",bg="#BDBDBD",fg="black", font=("Times New Roman", 22)).place(x=75,y=50)

BtnADM=Button(Principal,text="Administrador", font=("Comic Sans",18),command=VentAdmin).place(x=140,y=195)
BtnUsr=Button(Principal,text="Usuario", font=("Comic Sans",18),command=ventanaempl).place(x=450,y=195)
Salir=Button(Principal, text="Salir",font=("Comic Sans",16),command=Principal.destroy).place(x=550, y=270)



Principal.resizable(0,0)
Principal.mainloop()

