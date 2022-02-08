import nuflux
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# flux1 = nuflux.makeFlux('H3a_SIBYLL23C_pr')
flux2 = nuflux.makeFlux('H3a_SIBYLL23C_conv')
flux3 = nuflux.makeFlux('H3a_SIBYLL23C_k')
flux4 = nuflux.makeFlux('H3a_SIBYLL23C_K0')
flux5 = nuflux.makeFlux('H3a_SIBYLL23C_K0L')
flux6 = nuflux.makeFlux('H3a_SIBYLL23C_K0S')
flux7 = nuflux.makeFlux('H3a_SIBYLL23C_pi')
flux8 = nuflux.makeFlux('H3a_SIBYLL23C_mu')
flux9 = nuflux.makeFlux('H3a_SIBYLL23C')

# flux11 = nuflux.makeFlux('H3a_SIBYLL21_pr')
flux12 = nuflux.makeFlux('H3a_SIBYLL21_conv')
flux13 = nuflux.makeFlux('H3a_SIBYLL21_k')
flux14 = nuflux.makeFlux('H3a_SIBYLL21_K0')
flux15 = nuflux.makeFlux('H3a_SIBYLL21_K0L')
flux16 = nuflux.makeFlux('H3a_SIBYLL21_K0S')
flux17 = nuflux.makeFlux('H3a_SIBYLL21_pi')
flux18 = nuflux.makeFlux('H3a_SIBYLL21_mu')
flux19 = nuflux.makeFlux('H3a_SIBYLL21')

nu_type=nuflux.NuMu
nu_cos_zenith =1
x = np.arange(start=1, stop=400, step=1)
nu_energy=10**(x/50) # in GeV
# fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)
# fluxmu11=flux11.getFlux(nu_type,nu_energy,nu_cos_zenith)
# w_flux1=fluxmu1/fluxmu11
# print(w_flux1)
# plt.plot(nu_energy,w_flux1,color='red', linestyle='solid', linewidth = 3, marker='o', markerfacecolor='blue', markersize=2)
fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu12=flux12.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux2=fluxmu2/fluxmu12
print(w_flux2)
print(fluxmu2)
print(fluxmu12)
plt.plot(nu_energy,w_flux2,color='green', linestyle='solid', linewidth = 3)
fluxmu3=flux3.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu13=flux13.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux3=fluxmu3/fluxmu13
print(w_flux3)
print(fluxmu3)
print(fluxmu13)
# plt.plot(nu_energy,w_flux3,color='blue', linestyle='solid', linewidth = 3, marker='x', markerfacecolor='blue', markersize=2)
fluxmu4=flux4.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu14=flux14.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux4=fluxmu4/fluxmu14
print(w_flux4)
print(fluxmu4)
print(fluxmu14)
# plt.plot(nu_energy,w_flux4,color='black', linestyle='solid', linewidth = 3, marker='*', markerfacecolor='blue', markersize=2)
fluxmu5=flux5.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu15=flux15.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux5=fluxmu5/fluxmu15
print(w_flux5)
print(fluxmu5)
print(fluxmu15)
plt.plot(nu_energy,w_flux5,color='black', linestyle='dashed', linewidth = 3)
# fluxmu6=flux6.getFlux(nu_type,nu_energy,nu_cos_zenith)
# fluxmu16=flux16.getFlux(nu_type,nu_energy,nu_cos_zenith)
# w_flux6=fluxmu6/fluxmu16
# print(w_flux6)
# plt.plot(nu_energy,w_flux6,color='yellow', linestyle='solid', linewidth = 3, marker='*', markerfacecolor='blue', markersize=2)
fluxmu7=flux7.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu17=flux17.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux7=fluxmu7/fluxmu17
print(w_flux7)
print(fluxmu7)
print(fluxmu17)
plt.plot(nu_energy,w_flux7,color='blue', linestyle='solid', linewidth = 3)
fluxmu8=flux8.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu18=flux18.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux8=fluxmu8/fluxmu18
print(w_flux8)
print(fluxmu8)
print(fluxmu18)
plt.plot(nu_energy,w_flux8,color='tan', linestyle='dashed', linewidth = 3)
fluxmu9=flux9.getFlux(nu_type,nu_energy,nu_cos_zenith)
fluxmu19=flux19.getFlux(nu_type,nu_energy,nu_cos_zenith)
w_flux9=fluxmu9/fluxmu19
print(w_flux9)
print(fluxmu9)
print(fluxmu19)
plt.plot(nu_energy,w_flux9,color='red', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV)', fontsize = 20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}^{SIB23}/\phi_{\nu_{\mu}}^{SIB21}$', fontsize = 20)
#plt.xlim(3, 5)
#plt.ylim(10**(-6), 0.1)
plt.xscale("log")
plt.yscale("log")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.title('Muon Neutrino flux ratio(SIBYLL23 to SIBYLL21)(cos_zenith=1)' , fontsize=15)
plt.legend(["K Decay","K0L decay","pi decay","muon decay","overall"], loc ="upper left", fontsize = 17)
plt.show()
