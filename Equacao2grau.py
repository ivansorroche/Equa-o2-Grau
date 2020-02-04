# D = b**2 - 4 * a * c
# X = -b + RD /2 * a
# X = -b - RD /2 * a


import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))


D = (b**2) - (4 * a * c)

if D <= 0:
	print("Não existe raiz de numero negativo!")
	

else:
	if D > 0:

		raiz_delta = math.sqrt(D)

	else:
		
		x1 = (-b + raiz_delta) /2 * a

		x2 = (-b - raiz_delta) /2 * a


		print(x1)
		print(x2)





	

		


	

	
