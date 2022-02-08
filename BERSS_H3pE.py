import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('BERSS_H3p_lower')
flux2 = nuflux.makeFlux('BERSS_H3p_central')
flux3 = nuflux.makeFlux('BERSS_H3p_upper')
flux4 = nuflux.makeFlux('bartol')
nu_type1=nuflux.NuMu
nu_type2=nuflux.NuE
nu_cos_zenith =1.0
x = np.arange(start=150, stop=400, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1=flux1.getFlux(nu_type1,nu_energy,nu_cos_zenith)*(nu_energy**3)
fluxe1=flux1.getFlux(nu_type2,nu_energy,nu_cos_zenith)*(nu_energy**3)
print(fluxmu1)
plt.plot(nu_energy,fluxmu1+fluxe1,color='red', linestyle='dashed', linewidth = 1)
fluxmu2=flux2.getFlux(nu_type1,nu_energy,nu_cos_zenith)*(nu_energy**3)
fluxe2=flux2.getFlux(nu_type2,nu_energy,nu_cos_zenith)*(nu_energy**3)
print(fluxmu2)
plt.plot(nu_energy,fluxmu2+fluxe2,color='green', linestyle='solid', linewidth = 3)
fluxmu3=flux3.getFlux(nu_type1,nu_energy,nu_cos_zenith)*(nu_energy**3)
fluxe3=flux3.getFlux(nu_type2,nu_energy,nu_cos_zenith)*(nu_energy**3)
print(fluxmu3)
plt.plot(nu_energy,fluxmu3+fluxe3,color='blue', linestyle='dashed', linewidth = 1)
fluxmu4=flux4.getFlux(nu_type1,nu_energy,nu_cos_zenith)*(nu_energy**3)
fluxe4=flux4.getFlux(nu_type2,nu_energy,nu_cos_zenith)*(nu_energy**3)
plt.plot(nu_energy,fluxmu4+fluxe4,color='black', linestyle='dashed', linewidth = 1)
plt.xlabel('Energy(GeV)', fontsize = 20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}+\nu_e}E^3$', fontsize = 20)
plt.xlim(1e3, 1e8)
#plt.ylim(10**(-6), 0.1)
plt.xscale("log")
plt.yscale("log")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.title('Flux versus Energy for BERSS_H3p)(cos_zenith=1.0)' , fontsize=15)
plt.legend(["BERSS_H3p_lower", "BERSS_H3p_central","BERSS_H3p_upper","Bartol group (conventional)"], loc ="upper right", fontsize=20)
plt.show()              
