def ler_numeros():
	n=int(input("Quantos termos voce quer? "))
	lista=[]
	x=0
	while (x<n):
		y=int(input("Termo: "))
		lista.append(y)
		x=x+1
	return(lista)