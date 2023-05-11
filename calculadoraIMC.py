


def calcular_IMC (altura, peso):
    
    IMC = peso / (altura**2)

    if IMC < 18.5:
        print("Abaixo do peso")
    elif IMC >= 18.5 and IMC < 24.9:
        print("Peso normal")
    elif IMC >= 25 and IMC < 30:
        print("Sobrepeso") 
    elif IMC >= 30:
        print("Obesidade")      

    print(altura)
    print(peso)
    print(IMC)  

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
calcular_IMC(altura, peso)



