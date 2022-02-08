 ######################## for Flux vs Energy
from mpl_toolkits import mplot3d 
import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('bartol')
flux2 = nuflux.makeFlux('honda2006')
nu_type1=nuflux.NuMu
nu_type2=nuflux.NuE
x = np.arange(start=20, stop=120, step=1)
nu_energy=100*(x-19) # in GeV
nu_cos_zenith = -1.4+ x*0.02
fluxmu1=flux1.getFlux(nu_type1,nu_energy,nu_cos_zenith)*nu_energy**3
fluxe1=flux1.getFlux(nu_type2,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu1)
plt.plot(nu_energy,fluxmu1,color='red', linestyle='solid', linewidth = 3)
fluxmu2=flux2.getFlux(nu_type1,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu2)
plt.plot(nu_energy,fluxmu2,color='blue', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV))')
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$')

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Flux versus Energy (cos_zenith=1)')
plt.xscale("log")
plt.yscale("log")
plt.title('Flux versus cos_zenith for bartol and honda2006')
plt.legend(["bartol", "honda2006"], loc ="upper right")
#plt.show()

plt.plot(nu_energy,(fluxmu1/fluxmu2),color='blue', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV))')
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}/\phi_{\nu_{\mu}}$')

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Flux Ratio versus Energy (cos_zenith=1)')
plt.xscale("log")
plt.yscale("log")
plt.legend(["bartol:honda2006"], loc ="lower right", fontsize = 20)
#plt.show()

# Data for a three-dimensional line
#ax.plot3D(xline, yline, zline, 'gray')
# # Data for three-dimensional scattered points
ax = plt.axes(projection ='3d')
ax.plot3D(nu_energy,nu_cos_zenith,(fluxmu1/fluxmu2), 'Green')
ax.set_title('Flux ratio versus cos_zenith and energy for bartol and honda2006 ', fontsize=14)
# plt.xscale("log")
ax.set_ylabel(r'$\phi_{\nu_{\mu}}E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$', fontsize=14)
ax.set_xlabel('Energy(GeV))', fontsize=14)
ax.set_zlabel('cos_zenith' , fontsize=14);
# plt.yscale("log")
# plt.show()
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(nu_energy,(fluxmu1/fluxmu2),nu_cos_zenith, 'Green')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z');
#plt.show()

# Creating dataset

x1,y1 = np.meshgrid(nu_energy,nu_cos_zenith)
z1=(flux1.getFlux(nu_type2,x1,y1)+flux1.getFlux(nu_type1,x1,y1))*nu_energy**3
# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
# ax.set_title(r'Flux  versus cos$\theta$(zenith angle) and energy by honda group ', fontsize=20)
# plt.xscale("log")
ax.set_zlabel(r'$\phi_{\nu}E^3[GeV^2 cm^{-2} s^{-1}sr^{-1}]$', fontsize=20, color = 'red',labelpad=20)

ax.set_xlabel('Energy(GeV))', fontsize=20, color = 'red',labelpad =20)
ax.set_ylabel(r'cos$\theta$' , fontsize=20, color = 'red',labelpad=20);
# Creating plot
ax.plot_surface(x1, y1, z1)
# plt.xscale("log")
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.zaxis.set_tick_params(labelsize=12)
ax.set_zscale('log')
# plt.yscale("log")
# show plot
plt.show()

#########################For Flux vs zenith angle

'''
import nuflux
import numpy as np
import matplotlib.pyplot as plt
flux1 = nuflux.makeFlux('bartol')
flux2 = nuflux.makeFlux('honda2006')
nu_type=nuflux.NuMu
nu_cos_zenith =1.0
x = np.arange(start=50, stop=200, step=1)
nu_energy=10**(x/50) # in GeV
fluxmu1=flux1.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu1)
plt.plot(nu_energy,fluxmu1,color='red', linestyle='solid', linewidth = 3)
fluxmu2=flux2.getFlux(nu_type,nu_energy,nu_cos_zenith)*nu_energy**3
print(fluxmu2)
plt.plot(nu_energy,fluxmu2,color='blue', linestyle='solid', linewidth = 3)
plt.xlabel('Energy(GeV))')
# naming the y axis
plt.ylabel(r'$\phi_{\nu_{\mu}}E^3 [GeV^2 cm^{-2} s^{-1}sr^{-1}]$')

#plt.xlim(3,6)
#plt.ylim(-22,-10)
# giving a title to my graph
plt.title('Flux versus Energy (cos_zenith=1)')
plt.xscale("log")
plt.yscale("log")
plt.title('Flux versus cos_zenith for bartol and honda2006(E=100 GeV)')
plt.legend(["bartol", "honda2006"], loc ="upper right")
plt.show()

plt.plot(nu_energy,(fluxmu1/fluxmu2),color='blue', linestyle='solid', linewidth = 3)
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

'''
