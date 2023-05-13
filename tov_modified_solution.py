import pandas as pd
from definitions import *

# File for Data
data = open("TOV.dat","w+")
data.write("xi: Dimensionless distance\ntheta: Dimensionless pressure T\nM: Dimensionless mass M\n\n\nxi\ttheta\tM\n")

# numerical integration
h = 0.00001
xi = 0.00001
theta = Theta(xi)
m = Mu(xi)
XI = []
THETA = []
MU = []
while theta>=0.0001:
    XI.append(xi)
    MU.append(m)
    THETA.append(theta)
    data.write(str(xi)+"\t"+str(theta)+"\t"+str(m)+"\n")
    m_k1 = dM_modified(xi, theta, m)
    theta_k1 = dT(xi, theta, m)
    m_k2 = dM_modified(xi+h, theta+theta_k1*h, m)
    theta_k2 = dT(xi+h, theta+theta_k1*h, m+m_k1*h)
    m = m + (m_k1+m_k2)*h/2
    theta = theta + (theta_k1+theta_k2)*h/2
    xi = xi + h
data.close()

R_modified = []
M_modified = []
P_modified = []


for i in range(0, len(XI)-1, 1):
    R_modified.append(RUnits(XI[i]))
    M_modified.append(MUnits(MU[i]))
    P_modified.append(PrUnits(THETA[i]))

pd.DataFrame({"R":R_modified, "M":M_modified, "P":P_modified}).to_csv("TOV_modified.csv", index=False)