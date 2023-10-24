array = []
number = int(input("ingresar el numero"))
array.append(1) 
while True:
    if len(array) == number:
        break
    else:
        array.append(array[len(array)-1]+2)

for i in range(len(array)):
    for j in range(i,-1,-1):
        print(array[j], end=" ")
    print("")

'''
1
31
351
7531
97531
'''


