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
        print(f" \n Usuario #{i + 1}")
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
def EditarUsuarios():
    buscarUser = buscarUsuario()
    for i in range(len(users["Users"][buscarUser - 1])):
        print(users["Users"][buscarUser - 1])    
    editarUser = input("Ingrese qué desea editar: ")
    nuevoValue = input("Ingresa la nueva información: ")
    users["Users"][buscarUser - 1][editarUser]=nuevoValue
    

EditarUsuarios()
