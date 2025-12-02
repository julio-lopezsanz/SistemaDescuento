"""Sistema de descuento"""

try:
    #inputs
    item_name = input("Ingrese el nombre del producto: ")
    item_price = float(input("Ingrese el precio del producto: $"))
    item_amount = int(input("Ingrese la cantidad de productos: "))

    #Validacion del precio y cantidad del producto
    if item_price <= 0 or item_amount <= 0:
        print("ERROR: precio y cantidad deben ser mayores que cero.")
        exit()

    #Validacion del cliente VIP
    customer_vip = input("¿El cliente es VIP? (si/no): ").lower()
    if customer_vip in ('si', 's'):
        VIP = True
    elif customer_vip in ('no', 'n'):
        VIP = False
    else:
        print("ERROR: responde solo 'si' o 'no'")
        exit()

    #Aplicacion del descuento por subtotal
    sub_total = item_price * item_amount
    if sub_total > 3000:
        PERCENT = 40
    elif sub_total > 2000:
        PERCENT = 30
    elif sub_total > 1000:
        PERCENT = 20
    else:
        PERCENT = 0

    #Aplicacion del descuento por cantidad
    if item_amount >= 12:
        PERCENT += 5

    #Aplicacion del descuento por cliente VIP
    if VIP:
        PERCENT += 10

    #Calcular el descuento total
    discount = sub_total * (PERCENT / 100)

    #Impresion en pantalla
    print(f"\nPRODUCTO: {item_name}")
    print(f"PRECIO: ${item_price:.2f}")
    print(f"CANTIDAD: {item_amount}")
    print(f"SUBTOTAL: ${sub_total:.2f}")
    print(f"DESCUENTO APLICADO: {PERCENT}%")
    print(f"DESCUENTO: ${discount:.2f}")
    print(f"TOTAL A PAGAR: ${sub_total - discount:.2f}")

except ValueError:
    print("ERROR: el precio y la cantidad deben ser valores numéricos.")
