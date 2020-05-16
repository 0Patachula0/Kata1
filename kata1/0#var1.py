precio = 3.49
descuento = 1 - 0.6
precio_con_descuento = precio*descuento

num_barras = input("Introduzca el num de barras vendidas:")
num_barras = int(num_barras)

print("Precio habitual:", precio)
print("Descuento:", precio_con_descuento)
print("Coste final:", num_barras*precio_con_descuento)