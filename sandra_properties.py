import numpy as np 
import pynbody
import matplotlib

s1 = pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.003200/h148.cosmo50PLK.3072g3HbwK1BH.003200')
s1.physical_units()
h1 = s1.halos()

top_halos1 = h1[:6]
top_halos2 = h1[7:9]

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

for i, halo in enumerate(top_halos1):
    BH = findBH(halo)
    total_bh_mass = np.sum(BH['mass'])
    print(f'Halo {i} black hole mass: {total_bh_mass.in_units("Msol"):.2e}')

bh_masses = [np.sum(findBH(halo)['mass']).in_units("Msol") for halo in top_halos1]

for i, halo in enumerate(top_halos2):
    BH = findBH(halo)
    total_bh_mass = np.sum(BH['mass'])
    print(f'Halo {i} black hole mass: {total_bh_mass.in_units("Msol"):.2e}')

bh_masses = [np.sum(findBH(halo)['mass']).in_units("Msol") for halo in top_halos2]

s2 = pynbody.load('/mnt/data0/jillian/h148/6144/h148.cosmo50PLK.6144g3HbwK1BH.003264/h148.cosmo50PLK.6144g3HbwK1BH.003264')
s2.physical_units()
h2 = s2.halos()

s2top_halos1 = h2[:10] 
s2top_halos2 = h2[12:15]

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

for i, halo in enumerate(s2top_halos1):
    BH = findBH(halo)
    total_bh_mass = np.sum(BH['mass'])
    print(f'Halo {i} black hole mass: {total_bh_mass.in_units("Msol"):.2e}')

bh_masses = [np.sum(findBH(halo)['mass']).in_units("Msol") for halo in s2top_halos1]

for i, halo in enumerate(s2top_halos2):
    BH = findBH(halo)
    total_bh_mass = np.sum(BH['mass'])
    print(f'Halo {i} black hole mass: {total_bh_mass.in_units("Msol"):.2e}')

bh_masses = [np.sum(findBH(halo)['mass']).in_units("Msol") for halo in s2top_halos2]
