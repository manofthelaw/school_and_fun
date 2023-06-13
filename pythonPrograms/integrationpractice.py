#simpsons rule for integration

def f(x):
    return x**4-2*x+1

N=10
a=0.0
b=2.0
h=(b-a)/N

s= f(a) + f(b)
for k in range(1,N,2):
    s += 4*f(a+k*h)

for k in range(2,N,2):
    s += 2*f(a+k*h)

print((1/3)*h*s)
