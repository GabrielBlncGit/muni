def longlista(lista):
	i = 0
	for a in lista:
		i = i + 1
	return i

parm1i = input('Ingese primer numero: ')
parm2i = input('Ingese psegundo numero: ')
parm3i = input('Ingese primer numero: ')

listai = []
listai.append(parm1i)
listai.append(parm2i)
listai.append(parm3i)

print(longlista(listai))