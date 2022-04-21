n=30
m=30
print(id(n));
print(id(m));
lista1=[[1,2,3],[1,2,3],[1,2,3]]
print(type(lista1))   


""" lambda
"""
def func(x,y,z):
	return x + y + z     

print(func(2,3,4) )   

f = lambda x, y, z: x + y + z
numeros=[1,2,3,4,5,6,7,6,9]
print(f(2, 3, 4))
impares=filter(lambda x: x % 2!=0,numeros);
print(list (impares))
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

