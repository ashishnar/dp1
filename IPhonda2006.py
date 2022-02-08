import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('IPhonda2006_sno_solmin')
flux2 = nuflux.makeFlux('honda2006')
flux3 = nuflux.makeFlux('IPhonda2014_spl_solmin')
nu_type=nuflux.NuMu
nu_cos_zenith =1.0
x = np.arange(start=50, stop=200, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu1)
fluxmu1_err = 0.1*fluxmu1
#plt.errorbar(nu_energy,fluxmu1, fluxmu1_err)
plt.fill_between(nu_energy,fluxmu1-fluxmu1_err, fluxmu1+fluxmu1_err,facecolor='r',alpha=0.5)
#plt.plot(nu_energy,fluxmu1,color='red', linestyle='solid', linewidth = 3)
fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu2)
fluxmu2_err = 0.1*fluxmu2
plt.fill_between(nu_energy,fluxmu2-fluxmu2_err, fluxmu2+fluxmu2_err,facecolor='b',alpha=0.5)
#plt.plot(nu_energy,fluxmu2,color='blue', linestyle='solid', linewidth = 3)
fluxmu3=flux3.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu3)
fluxmu3_err = 0.1*fluxmu3
plt.fill_between(nu_energy,fluxmu3-fluxmu3_err, fluxmu3+fluxmu3_err,facecolor='g',alpha=0.5)
#plt.plot(nu_energy,fluxmu3,color='green', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV)', fontsize=20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$', fontsize=20)

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Flux versus Energy (cos_zenith=1)', fontsize=20)
plt.xscale("log")
plt.yscale("log")
plt.legend(["IPhonda2006_sno_solmin", "honda2006", "IPhonda2014_spl_solmin"], loc ="lower left", fontsize = 20)
plt.show()

plt.plot(nu_energy,(fluxmu1/fluxmu2),color='blue', linestyle='solid', linewidth = 3)
plt.plot(nu_energy,(fluxmu3/fluxmu2),color='red', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV))')
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}/\phi_{\nu_{\mu}}$')

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Flux Ratio versus Energy (cos_zenith=1)')
plt.xscale("log")
plt.yscale("log")
plt.legend(["IPhonda2006_sno_solmin", "IPhonda2014_spl_solmin"], loc ="lower right", fontsize = 20)
plt.show()
