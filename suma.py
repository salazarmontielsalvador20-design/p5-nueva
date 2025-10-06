import sys

def main():
	# Si se pasan dos argumentos por línea de comandos, úsalos
	if len(sys.argv) >= 3:
		try:
			a = float(sys.argv[1])
			b = float(sys.argv[2])
		except ValueError:
			print("Entrada inválida")
			return
	else:
		try:
			a = float(input("Número 1: "))
			b = float(input("Número 2: "))
		except ValueError:
			print("Entrada no permitida")
			return

	print(a + b)

if __name__ == '__main__':
	main()