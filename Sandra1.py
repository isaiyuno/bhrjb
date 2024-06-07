import pynbody
import matplotlib.pylab as plt

s1 = pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.003200/h148.cosmo50PLK.3072g3HbwK1BH.003200')
s2 = pynbody.load('/mnt/data0/jillian/h148/6144/h148.cosmo50PLK.6144g3HbwK1BH.003264/h148.cosmo50PLK.6144g3HbwK1BH.003264')

h1 = s1.halos()
h2 = s2.halos()
pynbody.analysis.angmom.faceon(h1[3])
pynbody.analysis.angmom.faceon(h2[3])
s1.physical_units()
s2.physical_units()
p1 = pynbody.analysis.profile.Profile(h1[3].s, vmin =.01, max=50)
p2 = pynbody.analysis.profile.Profile(h2[3].s, vmin =.01, max=50)
'''THE ABOVE loads the simulation file as well as center on halo "h[1]" as well as align the disk
in a certain angle. p is a profile for the stars, f is the figure and sub plots.
'''


#This creates the plot of that, also using 'plt' instead of 'axs[#]' produces images of plot one by one
plt.plot(p1['rbins'],p1['density'], 'k')
plt.plot(p2['rbins'],p2['density'], 'r')

plt.semilogy()
plt.xlabel('R [kpc]')
plt.ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-2}$]')
plt.title("Gas Density vs Distance From Center")
plt.legend(loc='upper left',fontsize=8)
plt.grid(True)
plt.tight_layout()




#plt.semilogy, plt.xlabel, and plt.ylabel were deleted because they don't need to be repeated



'''I wrote commented "plt.show()" above to make note that plt.show should work under 
normal circumstances, but for now I will see the plot on github using "plt.savefig("blah.png")"
. In reality, plt.savefig will not be on the final code of this'''
#plt.show()
plt.savefig("gas_density.png")
#plt.show()


plt.close()

#Now I will create a second plot of the sandra 1 simulation where we are centering on Halo [3]
p1 = pynbody.analysis.profile.Profile(h1[3].d,min=.01,max=50,ndim=3)
p2 = pynbody.analysis.profile.Profile(h2[3].d,min=.01,max=50,ndim=3)


plt.plot(p1['rbins'],p1['density'], 'k')
plt.plot(p2['rbins'],p2['density'], 'r')

plt.semilogy()
plt.xlabel('R [kpc]')
plt.ylabel(r'$\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
plt.title("Dark Matter Density vs Distance From Center")
plt.legend(loc='upper left',fontsize=8)
plt.grid(True)
plt.tight_layout()




#plt.show()
plt.savefig("darkmatter.png")
