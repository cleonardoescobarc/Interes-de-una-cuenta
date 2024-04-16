print("Vamos a calcular el interes")
dinero = float(input("Ingrese la cantidad: "))

if dinero<10000.00:
    dinero = dinero * (1+0.03)
else:
    dinero = dinero * (1+0.04)

print("El saldo final es: ", dinero)