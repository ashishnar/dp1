
#########################For Flux vs zenith angle


import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('BERSS_H3p_central')
flux2 = nuflux.makeFlux('sarcevic_std')
nu_type1=nuflux.NuMu
nu_type2=nuflux.NuE
nu_energy1 =100
nu_energy2 =1000
x = np.arange(start=0, stop=100, step=1)
nu_cos_zenith= -1+x*0.02
fluxmu1=flux1.getFlux(nu_type1,nu_energy1,nu_cos_zenith)
fluxe1=flux1.getFlux(nu_type2,nu_energy1,nu_cos_zenith)
fratio1 = fluxmu1/fluxe1
plt.plot(nu_cos_zenith,fratio1,color='red', linestyle='solid', linewidth = 3)
fluxmu2=flux2.getFlux(nu_type1,nu_energy1,nu_cos_zenith)
fluxe2=flux2.getFlux(nu_type2,nu_energy1,nu_cos_zenith)
fratio2 = fluxmu2/fluxe2
plt.plot(nu_cos_zenith,fratio2,color='blue', linestyle='solid', linewidth = 3)
fluxmu3=flux1.getFlux(nu_type1,nu_energy2,nu_cos_zenith)
fluxe3=flux1.getFlux(nu_type2,nu_energy2,nu_cos_zenith)
fratio3 = fluxmu3/fluxe3
plt.plot(nu_cos_zenith,fratio3,color='red', linestyle='dashed', linewidth = 3)
fluxmu4=flux2.getFlux(nu_type1,nu_energy2,nu_cos_zenith)
fluxe4=flux2.getFlux(nu_type2,nu_energy2,nu_cos_zenith)
fratio4 = fluxmu4/fluxe4
print(fluxe4)
print(fluxmu4)
print(fratio4)
plt.plot(nu_cos_zenith,fratio4,color='blue', linestyle='dashed', linewidth = 3)
plt.xlabel(r'$cos(\theta)$',fontsize = 20)
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}/\phi_{\nu_e}$', fontsize=20)

plt.xlim(-1,1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.ylim(-22,-10)
# giving a title to my graph
# plt.xscale("log")
# plt.yscale("log")
# plt.title(r'Flux versus $cos(\theta)$ for bartol and honda2006(E=100 GeV)',fontsize = 20)
plt.legend(["BERSS at 100 GeV", "BERSS group at 100 GeV","ERS at 10 GeV", "ERS 10 GeV"], loc ="upper center",fontsize = 20)
plt.show()

# plt.plot(nu_energy,(fluxmu1/fluxmu2),color='blue', linestyle='solid', linewidth = 3)
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

