class estudiante:

 def __init__(self, nombre, apellido, cedula, correo, telefono):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.correo = correo
    self.telefono = telefono
 def imprimirnombre(self):
    print("texto1",self.nombre,"texto2",self.apellido,"texto3",self.cedula,"texto4",self.correo,"texto5",self.telefono)

p = estudiante("yajaira","apellido","cedula","correo","telefono")

print(p.imprimirnombre())