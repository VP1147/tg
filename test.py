import math as m

def Fx(x):
	return m.sin(x)

def integ(f, a, b):				# Integral de f(x) dx no intervalo [a, b]
	n = 1e3
	i = 0  						# Contador de iteracoes
	k = a
	h = (b-a)/(3*n)				# Dividindo os subintervalos
	S = 0						# Variavel de soma
	while(i <= (3*n)-3):
		try: S += f(k) + 3*f(k + h) + 3*f(k + 2*h) + f(k + 3*h)
		except: pass
		i += 3
		k += 3*h
	S = S*((3*h)/8)
	print("I ~= {:.12f}".format(S))
	return S

integ(Fx, 0, m.pi/4)