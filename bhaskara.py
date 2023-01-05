import math


a = float(input("Digite o valor de a: "))

b = float(input("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))



if b ** 2 - 4 * a * c<0:
	
	print("esta equação não possui raízes reais")



if b ** 2 - 4 * a * c == 0:

	x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
	
	print("a raiz dupla desta equação é", x)



if b ** 2 - 4 * a * c > 0:

	m = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

	n = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

	if m>n:
			
		print("as raízes da equação são", n, "e", m)

	if m<n:	
		
		print("as raízes da equação são", m, "e", n)

	
