import pynbody; from pynbody.analysis import profile; import matplotlib.pylab as plt
s1 = pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.003200/h148.cosmo50PLK.3072g3HbwK1BH.003200')
s2 = pynbody.load('/mnt/data0/jillian/h148/6144/h148.cosmo50PLK.6144g3HbwK1BH.003264/h148.cosmo50PLK.6144g3HbwK1BH.003264')

s1.physical_units()
s2.physical_units()

h1 = s1.halos()
h2 = s2.halos()

pynbody.analysis.angmom.faceon(h1[3])
pynbody.analysis.angmom.faceon(h2[3])

p1 = pynbody.analysis.profile.Profile(h1[3].s, vmin =.01, max=50)
p2 = pynbody.analysis.profile.Profile(h2[3].s, vmin =.01, max=50)

plt.plot(p1['rbins'].in_units('kpc'),p1['feh'],'k')
plt.plot(p2['rbins'].in_units('kpc'),p2['feh'],'r')

plt.xlabel('$R$ [kpc]'); plt.ylabel('[Fe/H]')
plt.title("Metallicity (Fe/H) vs Distance From Center")
plt.legend(loc='upper left',fontsize=8)
plt.grid(True)
plt.tight_layout()


#June 3, 2024: please tell me this push worked




plt.savefig("FehSandra1.png")
