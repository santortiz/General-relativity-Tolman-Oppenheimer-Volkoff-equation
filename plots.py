from matplotlib import pyplot as plt
from tov_solution import R, M, P
from definitions import n,K

# Plots
plt.plot(R,M)
plt.xlabel("R(km)")
plt.ylabel("M(Solar)")
plt.title("Mass - Distance")
name = "Plots/M_n_{}_K_{}.pdf".format(n,K)
plt.savefig(name)
plt.clf()
plt.plot(R,P)
plt.xlabel("R(km)")
plt.ylabel("Pressure (dyn/cm^2)")
plt.title("Pressure - Distance")
name = "Plots/Pressure_n_{}_K_{}.pdf".format(n,K)
plt.savefig(name)