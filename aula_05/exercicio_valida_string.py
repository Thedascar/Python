def valida_str(string,min,max):
    tam = len(string)
    if (tam < min) or (tam > max):
        return False
    else:
        return True

string = input('Digite uma String entre (3-20 caracteres): ')
while not valida_str(string,3,20):
    string = input('Digite uma String entre (3-20 caracteres): ')

print(string)