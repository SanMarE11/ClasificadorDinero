#SanMarE11
def monedas(cartera):
    indice=5
    valores=[.10,.5,1,2,5,10]
    if cartera>=.1:
        while(cartera>=.1):
            if valores[indice]>cartera:
                indice=indice-1
            else:
                print("Tienes una moneda de {} pesos".format(valores[indice]))
                cartera=cartera-valores[indice]

def billetes(cartera):
    indice=5
    valores=[0,50,100,200,500,1000]
    if cartera>=20:
        while(cartera>=20):
            if valores[indice]>cartera:
                indice=indice-1
            else:
                print("Tienes un billete de {} pesos".format(valores[indice]))
                cartera=cartera-valores[indice]
    return cartera

if __name__ == '__main__':
    print("Ingresa El dinero en cartera para clasificarlo > ")
    dinero=float(input())
    dinero = billetes(dinero)
    monedas(dinero)