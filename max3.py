def maxde3(lista):
	lista.sort()
	return lista[-1]

parm1i = input('Ingese primer numero: ')
parm2i = input('Ingese psegundo numero: ')
parm3i = input('Ingese primer numero: ')

listai = []
listai.append(parm1i)
listai.append(parm2i)
listai.append(parm3i)

print(maxde3(listai))