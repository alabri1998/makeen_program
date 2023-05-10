
fehrenhite_celsius = input('write F for Fehrenhite , C for celsius: ')
temp = int(input('Enter tempreature: '))
if fehrenhite_celsius.upper() == 'F':
    celsius = (temp-32)/1.8
    print(celsius)
elif fehrenhite_celsius.upper() == 'C':
    fahrenheit = (temp * 1.8) + 32
    print(fahrenheit)
else:
    print('you enter wrong string')