num = input("Digite um numero! ")

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print(num_int, "é par") 
    else :
        print(num_int, "é impar") 
except: 
    print(f"Erro, '{num}' não é um numero")

hora = input("Digite a hora! ")

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int < 12:
        print("Bom Dia!")
    elif hora_int > 11 and hora_int < 18:
        print("Boa Tarde!")
    elif hora_int > 17 and hora_int < 24:
        print("Boa Noite!")
    else:
        print("Hora invalida!")     
except: 
    print(f"Erro, '{hora}' não é um numero")


first_name = input("Digite seu primeiro nome! ")

name_size =  len(first_name)

if name_size <= 4 :
    print("Seu nome está curto")
elif name_size > 4 and name_size <= 6:
    print("Seu nome está normal")
else:
    print("Seu nome é muito Grande")