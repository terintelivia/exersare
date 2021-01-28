orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase)
del orase [2:3]
print(orase)
orase.clear()
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.remove('Balti')
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.pop(2)
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase[0:2]=[]
print(orase)
orase[:]=[]
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.append('Floresti')
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.extend(['Floresti'])
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.extend('Glodeni')
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase.insert(2, 'Glodeni')
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase[1:2]=['Chisinau','Floresti']
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
orase[2]='Floresti'
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase)
orase[:] = ['Recea', 'Sangureni', 'Corlateni', 'Parlita' ]
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase)
lista1=orase[0:2]
lista2=orase[2:4]
print(lista1)
print(lista2)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase[::2])
print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase[::-1])
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
lista1=orase[:]
for orase in lista1:
     print(orase)
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase.index('Orhei'))
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
print(orase.count('Balti'))
orase = ['Balti', 'Cahul','Sangerei', 'Cahul' , 'Orhei','Cahul']
print(orase.count('Cahul'))
orase = ['Balti', 'Sangerei', 'Cahul' , 'Orhei']
