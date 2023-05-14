def contador_de_vogais(texto):
    contador = 0
    vogais = 'aeiouAEIOU'
    for char in texto:
        if char in vogais:
            contador += 1
    return contador


entrada = input('Digite um texto/frase: ')
texto = contador_de_vogais(entrada)

print('O texto/frase: {}, tem {} Vogais.'.format(entrada, texto))

