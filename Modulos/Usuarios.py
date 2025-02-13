import json

def abrirJSON():
    dicFinal={}
    with open("../Jsons/users.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open("../Jsons/users.json",'w') as outFile:
        json.dump(dic,outFile)
    
users = {}
users = abrirJSON()
 
def buscarUsuario():
    cc = input("ingrese la cc del usuario")
    print(users["Users"][0][cc])



def verUsuarios():
    print("Nombre: ",users["Users"][0]["nombreCompleto"])
    print("CC: ",users["Users"][0]["CC"])
    print("Telefono: ",users["Users"][0]["telefono"])

