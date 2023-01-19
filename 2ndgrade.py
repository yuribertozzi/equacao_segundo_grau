import math

def delta(a, b, c):

	return b**2 - 4 * a * c


def main():

	a = float(input("Digite o valor de a: "))

	b = float(input("Digite o valor de b: "))

	c = float(input("Digite o valor de c: "))

	raizes(a, b, c)


def raizes(a, b, c):

	
	d = delta(a, b, c)
	
	
	if d == 0:

		x = (- b + math.sqrt(d)) / (2 * a)
		
		print("A única raiz é", x, ".")


	else:

		if d < 0:

			print("Esta equação não possui raízes reais.")


		else:

			m = (- b + math.sqrt(d)) / (2 * a)

			n = (- b - math.sqrt(d)) / (2 * a)

			print("As raízes são", m, "e", n, ".")
		
			

		

