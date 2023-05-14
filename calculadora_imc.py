# IMC = É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

def calcular_peso():
    while True:
        try:
            peso = float(input('Digite seu peso (Ex. 70): '))
            altura = float(input('Digite sua Altura (Ex. 1.80): '))
            break
        except:
            print('Digite apenas números!')
            
    altura = float(altura)
    imc = peso / altura ** 2           
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc > 18.6 and imc < 24.9:
        print('Peso Ideal')
    elif imc > 25.0 and imc < 29.9:
        print('Levimente acima do peso')
    elif imc > 30.0 and imc < 34.9:
        print('Obesidade grau 1')
    elif imc > 35.0 and imc < 39.9:
        print('Obesidade grau 2 (severa)')
    else:
        print('Obesidade 3 (móbida)')
                           
    return


calcular_peso()
