import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('sarcevic_min')
flux2 = nuflux.makeFlux('sarcevic_std')
flux3 = nuflux.makeFlux('sarcevic_max')
nu_type=nuflux.NuMu
nu_cos_zenith =1.0
x = np.arange(start=150, stop=400, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1 =flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy*3.1536*10**17
fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy*3.1536*10**17
fluxmu3=flux3.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy*3.1536*10**17
plt.plot(nu_energy,fluxmu1,color='red', linestyle='dashed', linewidth = 2)
plt.plot(nu_energy,fluxmu2,color='green', linestyle='solid', linewidth = 3)
plt.plot(nu_energy,fluxmu3,color='blue', linestyle='dashed', linewidth = 2)
# for x in range(150,400):
#     nu_energy=10**(x/50) # in GeV
    
#     print(fluxmu1)
#     plt.plot(nu_energy,fluxmu1,color='red', linestyle='dashed', linewidth = 3)
#     fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy*3.1536*10**17
#     print(fluxmu2)
#     # plt.plot(nu_energy,fluxmu2,color='green', linestyle='solid', linewidth = 3, marker='.', markerfacecolor='blue', markersize=1,label = 'sarcevic_std',loc ='upper right', fontsize = 20)
#     fluxmu3=flux3.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy*3.1536*10**17
#     print(fluxmu3)
#     # plt.plot(nu_energy,fluxmu3,color='blue', linestyle='dashed', linewidth = 3, marker='.', markerfacecolor='blue', markersize=1,label = 'sarcevic_max',loc ='upper right', fontsize = 20)

plt.xlabel('log(Energy)')
# naming the y axis
plt.ylabel(r'E$\phi_{\nu_{\mu}}[km^{-2} yr^{-1}sr^{-1}]$')
plt.xlim(10000, 10000000)
plt.ylim(1, 100000000 )
plt.xscale("log")
plt.yscale("log")
# giving a title to my graph
plt.title('Weighted Flux versus Energy for sarcevic(cos_zenith=1)')

plt.legend(["sarcevic_min","sarcevic_std", "sarcevic_max"],loc ="upper left", fontsize = 17)
plt.show()  
