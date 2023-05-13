from matplotlib import pyplot as plt
from tov_solution import R, M, P
from tov_modified_solution import R_modified, M_modified, P_modified
from definitions import n,K

# Plots
plt.plot(R,M)
plt.plot(R_modified,M_modified, linestyle="--", color="red", label="Modified")
plt.xlabel("R(km)")
plt.ylabel("M(Solar)")
plt.title("Mass - Distance")
plt.legend()
name = "Plots/M_n_{}_K_{}.pdf".format(n,K)
plt.savefig(name)
plt.clf()
plt.plot(R,P)
plt.plot(R_modified,P_modified, linestyle="--", color="red", label="Modified")
plt.xlabel("R(km)")
plt.ylabel("Pressure (dyn/cm^2)")
plt.title("Pressure - Distance")
plt.legend()
name = "Plots/Pressure_n_{}_K_{}.pdf".format(n,K)
plt.savefig(name)