continuar = 1
while continuar:
    compra = float(input("Ingrese la cantidad de la compra :"))
    if compra <= 100:
        importe_a_pagar = compra
        print("Total a pagar es :" + str(importe_a_pagar))
    elif compra > 100:
        tasa_descuento = 10
        importe_descuento = (compra * tasa_descuento)/100
        importe_a_pagar = compra - importe_descuento
    print("Total a pagar es :" + str(importe_a_pagar))
    continuar = int(input("Desea continuar ingrese 1 de lo contrario ingrese 0 :"))