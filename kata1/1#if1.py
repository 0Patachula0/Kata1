password = "contrasena"
password_user = input("Introduzca contrasena:")

if password == password_user.lower():
    print("Password correcto")
else:
    print("Password NO correcto")