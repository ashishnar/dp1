import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('honda2006')
nu_type=nuflux.NuMu
nu_cos_zenith =1.0
x = np.arange(start=1, stop=10000, step=5)
nu_energy= x # in GeV
fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu1)
if (nu_energy.any() <= 100):
	fluxmu1_err = 0.07*fluxmu1
elif (nu_energy.any() <= 1000 and nu_energy.any() > 100):
	fluxmu1_err = 0.14*fluxmu1
elif (nu_energy.any() <= 10000 and nu_energy.any() >= 1000):
	fluxmu1_err = 0.25*fluxmu1
#plt.errorbar(nu_energy,fluxmu1, fluxmu1_err)
plt.fill_between(nu_energy,fluxmu1-fluxmu1_err, fluxmu1+fluxmu1_err,facecolor='r',alpha=0.5)

plt.xlabel('Energy(GeV)', fontsize=20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$', fontsize=20)

plt.xlim(10,1e4)
# plt.ylim(-22,-10)
# giving a title to my graph
# plt.title(r'Flux versus Energy (cos$\theta$) for honda2006', fontsize=20)
plt.xscale("log")
plt.yscale("log")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.legend(["IPhonda2006_sno_solmin", "honda2006", "IPhonda2014_spl_solmin"], loc ="lower left", fontsize = 20)
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
