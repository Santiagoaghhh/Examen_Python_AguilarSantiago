import json

def abrirJSON():
    dicFinal={}
    with open("../Jsons/users.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("../Jsons/users.json",'w') as outFile:
        json.dump(dic,outFile)
    
users = {}
users = abrirJSON()
# ESTAS FUNCIONES SON SOLO PARA EL MENU DE CRUD USUARIOS

#1 . VER USUARIO
def verUsuarios():
    for i in range(len(users["Users"])):
        if users["Users"][i]["activo"]:
            print(" \n Usuario #", i + 1)
            print("Nombre: ", users["Users"][i]["nombreCompleto"])
            print("CC: ", users["Users"][i]["CC"])        
            print("=================================================0")

#2. BUSCAR USUARIO
def buscarUsuario():
    verUsuarios()
    buscarUser = int(input("Ingrese el numero de usuario #: "))
    if users["Users"][buscarUser - 1]["activo"]:
        print("Activo: Sí")
    else:
        print("Activo: No")
    print("Nombre: ", users["Users"][buscarUser - 1]["nombreCompleto"])
    print("CC: ", users["Users"][buscarUser - 1]["CC"])
    return buscarUser

#3. EDITAR USUARIO
def editarUsuarios():
    buscarUser = buscarUsuario()
    print(users["Users"][buscarUser - 1])    
    editarUser = input("Ingrese qué desea editar: ")
    nuevoValue = input("Ingresa la nueva información: ")
    users["Users"][buscarUser - 1][editarUser]=nuevoValue
    guardarJSON(users)

#4. ELIMINAR USUARIO
def eliminarUsuario():
    buscarUser = buscarUsuario()
    eliminarUser = input("¿Desea eliminar a este usuario?")
    users["Users"][buscarUser - 1]["activo"]=False

verUsuarios()


#============================================================================================#

def calcularTiempo()
    for i in range ()