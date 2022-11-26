with open("base_datos.txt", "a") as archivo:
  pregunta= "si"
  while pregunta == "si":
    print("Ingrese los siguientes datos del usuario:")
    doc = str(input("Ingrese el documento de identidad: "))
    nombre = str(input("Ingrese su nombre: "))
    apellido = str(input("Ingrese su apellido: "))
    archivo.write(doc + ",")
    archivo.write(nombre + ",")
    archivo.write(apellido + "\n")
    pregunta=input("¿Desea agreagar mas usuarios? \n Ingrese si o no: ")
  archivo.close()
print("El rpoceso se ha compleetado exitosamente.")