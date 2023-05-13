G=6.6743*10**(-8)
c=2.9979*10**10

s = 2.9979*10**10
g = G*c**(-2)

#K en unidades G=c=1
K_GC= (5.38*10**(9))*(g**(-2/3))*(s**(-2))

#rho en unidades G=c=1
rho_0c = (1.0*10**15)*g

#
gamma = 5/3
p0c = K_GC*rho_0c**(gamma)

a_0= rho_0c/p0c


print(f"%.3e"%K_GC)
print(f"%.3e"%rho_0c)
print(a_0)