import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('IPhonda2006_sno_solmin')
flux2 = nuflux.makeFlux('honda2006')
flux3 = nuflux.makeFlux('IPhonda2014_spl_solmin')
nu_type1=nuflux.NuMu
nu_type2=nuflux.NuE
nu_type3=nuflux.NuMuBar
nu_type4=nuflux.NuEBar
nu_cos_zenith =1.0
x = np.arange(start=50, stop=200, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1=flux1.getFlux(nu_type1,nu_energy,nu_cos_zenith)*nu_energy**3
fluxe1=flux1.getFlux(nu_type2,nu_energy,nu_cos_zenith)*nu_energy**3
fluxmubar1=flux1.getFlux(nu_type3,nu_energy,nu_cos_zenith)*nu_energy**3
fluxebar1=flux1.getFlux(nu_type4,nu_energy,nu_cos_zenith)*nu_energy**3
totflux1=fluxmu1+fluxe1+fluxmubar1+fluxebar1
plt.plot(nu_energy,totflux1,color='black', linestyle='dashed', linewidth = 3)
fluxmu2=flux2.getFlux(nu_type1,nu_energy,nu_cos_zenith)*nu_energy**3
fluxe2=flux2.getFlux(nu_type2,nu_energy,nu_cos_zenith)*nu_energy**3
fluxmubar2=flux2.getFlux(nu_type3,nu_energy,nu_cos_zenith)*nu_energy**3
fluxebar2=flux2.getFlux(nu_type4,nu_energy,nu_cos_zenith)*nu_energy**3
totflux2=fluxmu2+fluxe2+fluxmubar2+fluxebar2
plt.plot(nu_energy,totflux2,color='green', linestyle='solid', linewidth = 3)
fluxmu3=flux3.getFlux(nu_type1,nu_energy,nu_cos_zenith)*nu_energy**3
fluxe3=flux3.getFlux(nu_type2,nu_energy,nu_cos_zenith)*nu_energy**3
fluxmubar3=flux3.getFlux(nu_type3,nu_energy,nu_cos_zenith)*nu_energy**3
fluxebar3=flux3.getFlux(nu_type4,nu_energy,nu_cos_zenith)*nu_energy**3
totflux3=fluxmu3+fluxe3+fluxmubar3+fluxebar3
plt.plot(nu_energy,totflux3,color='red', linestyle='dashed', linewidth = 3)
plt.xlabel('Energy(GeV)', fontsize=20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu+\bar\nu} E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$', fontsize=20)

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Total Flux (neutrino+anti-neutrino)versus Energy (cos_zenith=1)', fontsize=20)
plt.xscale("log")
plt.yscale("log")
plt.legend(["IPhonda2006_sno_solmin", "honda2006", "IPhonda2014_spl_solmin"], loc ="lower left", fontsize = 20)
plt.show()

# plt.plot(nu_energy,(fluxmu1/fluxmu2),color='blue', linestyle='solid', linewidth = 3)
# plt.plot(nu_energy,(fluxmu3/fluxmu2),color='red', linestyle='solid', linewidth = 3)
# plt.xlabel('Energy(GeV))')
# # naming the y axis
# plt.ylabel(r'$\phi_{\nu_{\mu}}/\phi_{\nu_{\mu}}$')

# #plt.xlim(3,6)
# #plt.ylim(-22,-10)
# # giving a title to my graph
# plt.title('Flux Ratio versus Energy (cos_zenith=1)')
# plt.xscale("log")
# plt.yscale("log")
# plt.legend(["IPhonda2006_sno_solmin", "IPhonda2014_spl_solmin"], loc ="lower right", fontsize = 20)
# plt.show()
