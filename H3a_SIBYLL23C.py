"""import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('H3a_SIBYLL23C_pr')
nu_type=nuflux.NuMu
nu_energy=5 # in GeV
for x in range(-50,50):
    nu_cos_zenith =0.02*x
    fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)
    print(fluxmu1)
    plt.plot(nu_cos_zenith,fluxmu1,color='red', linestyle='solid', linewidth = 3, marker='o', markerfacecolor='blue', markersize=2)

plt.xlabel('cos_zenith')
# naming the y axis
plt.ylabel('Flux mu1 BERSS_H3a')

plt.xlim(-1,1)

# giving a title to my graph
plt.title('Flux versus cos_zenith at 1kGeV and 10kGeV(green)')

plt.legend()
plt.show()
"""


import nuflux
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
flux1 = nuflux.makeFlux('H3a_SIBYLL23C_pr')
flux2 = nuflux.makeFlux('H3a_SIBYLL23C_conv')
flux3 = nuflux.makeFlux('H3a_SIBYLL23C_k')
flux4 = nuflux.makeFlux('H3a_SIBYLL23C_K0')
flux5 = nuflux.makeFlux('H3a_SIBYLL23C_K0L')
#flux6 = nuflux.makeFlux('H3a_SIBYLL23C_K0S')
flux7 = nuflux.makeFlux('H3a_SIBYLL23C_pi')
flux8 = nuflux.makeFlux('H3a_SIBYLL23C_mu')
flux9 = nuflux.makeFlux('H3a_SIBYLL23C')

nu_type=nuflux.NuMu
nu_cos_zenith =1
x = np.arange(start=1, stop=400, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux1=fluxmu1*(nu_energy**3)
print(w_flux1)
plt.plot(nu_energy,w_flux1,color='red', linestyle='solid')
fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux2=fluxmu2*(nu_energy**3)
print(fluxmu2)
plt.plot(nu_energy,w_flux2,color='green', linestyle='solid')
fluxmu3=flux3.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux3=fluxmu3*(nu_energy**3)
print(w_flux3)
plt.plot(nu_energy,w_flux3,color='blue', linestyle='solid')
fluxmu4=flux4.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux4=fluxmu4*(nu_energy**3)
print(w_flux4)
plt.plot(nu_energy,w_flux4,color='black', linestyle='solid')
fluxmu5=flux5.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux5=fluxmu5*(nu_energy**3)
print(w_flux5)
plt.plot(nu_energy,w_flux5,color='yellow', linestyle='solid')
"""fluxmu6=flux6.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux6=fluxmu6*(nu_energy**3)
print(w_flux6)
plt.plot(nu_energy,w_flux6,color='brown', linestyle='solid', linewidth = 3, marker='*', markerfacecolor='blue', markersize=2)
"""
fluxmu7=flux7.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux7=fluxmu7*(nu_energy**3)
print(w_flux7)
plt.plot(nu_energy,w_flux7,color='magenta', linestyle='solid')
fluxmu8=flux8.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux8=fluxmu8*(nu_energy**3)
print(w_flux8)
plt.plot(nu_energy,w_flux8,color='tan', linestyle='solid')
fluxmu9=flux9.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux9=fluxmu9*(nu_energy**3)
print(w_flux9)
plt.plot(nu_energy,w_flux8,color='cyan', linestyle='solid')
plt.xlabel('Energy(GeV)', fontsize = 20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}} E^3 [GeV^2 cm^{-2} sr^{-1} s^{-1}]$', fontsize = 20)
#plt.xlim(3, 5)
#plt.ylim(10**(-6), 0.1)
plt.xscale("log")
plt.yscale("log")
plt.title('Flux versus Energy for all model)(cos_zenith=1)' , fontsize=15)
plt.legend(["H3a_SIBYLL23C_pr","H3a_SIBYLL23C_conv","H3a_SIBYLL23C_k","H3a_SIBYLL23C_K0","H3a_SIBYLL23C_K0L","H3a_SIBYLL23C_pi","H3a_SIBYLL23C_mu","H3a_SIBYLL23C"], loc ="lower left")
plt.show()
