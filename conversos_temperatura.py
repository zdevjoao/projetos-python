def celsius_para_fahrenheit(c):
    f = (c * 1.8) + 32
    return f
def fahrenheit_para_celsius(f):
    c = (f - 32) * 5/9
    return c

cel = float(input('Digite a temperatura em Celcius: '))
fahr = celsius_para_fahrenheit(cel)
print('A temperatura é de {} Fahrenheit'.format(fahr))


fehr = float(input('Digite a temperatura em Fahrenheit: '))
cel = fahrenheit_para_celsius(fehr)
print('A temperatura é de {} Celsius'.format(cel))