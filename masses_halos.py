import pynbody #this imports the package pynbody
import pynbody.analysis.halo
import numpy as np 
import matplotlib.pylab as plt

s1 = pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.003200/h148.cosmo50PLK.3072g3HbwK1BH.003200')
s2 = pynbody.load('/mnt/data0/jillian/h148/6144/h148.cosmo50PLK.6144g3HbwK1BH.003264/h148.cosmo50PLK.6144g3HbwK1BH.003264')
s1.physical_units()
s2.physical_units()
h1 = s1.halos()
h2 = s2.halos()
#this all just loads stuff and puts them into comprehensible units 

top_halos1 = h1[:6] 
top_halos2 = h1[7:9]

halo1  = top_halos1[1]
mass_units = halo1['mass'].units
print(f"the units of mass in the simulation are: {mass_units}")


MASSES1 = []
for halo in top_halos1:
    total_mass = halo['mass'].sum()  # Calculate the total mass of the current halo
    MASSES1.append(total_mass)  # Append the total mass to the list
for i, mass in enumerate(MASSES1):
    print(f"Total mass of halo {i}: {mass}")
MASSES2 = []
for halo in top_halos2:
    total_mass = halo['mass'].sum()
    MASSES2.append(total_mass)
for i, mass in enumerate(MASSES2, start=7):
    print(f"Total mass of halo {i}: {mass}")  


STELLAR1 = []
for halo in top_halos1:
    stellar_mass = halo.s['mass'].sum()
    STELLAR1.append(stellar_mass) 
for i, mass in enumerate(STELLAR1):
    print(f"Total stellar mass of halo {i}: {mass}")
STELLAR2 = []
for halo in top_halos2:
    stellar_mass = halo.s['mass'].sum()
    STELLAR2.append(stellar_mass)
for i, mass in enumerate(STELLAR2, start=7):
    print(f"Total stellar mass of halo {i}: {mass}")



#s2 stuff
s2top_halos1 = h2[:10] 
s2top_halos2 = h2[12:15]

s2MASSES1 = []
for halo in s2top_halos1:
    total_mass = halo['mass'].sum()  # Calculate the total mass of the current halo
    s2MASSES1.append(total_mass)  # Append the total mass to the list
for i, mass in enumerate(s2MASSES1):
    print(f"Total mass of halo {i}: {mass}")
s2MASSES2 = []
for halo in s2top_halos2:
    total_mass = halo['mass'].sum()
    s2MASSES2.append(total_mass)
for i, mass in enumerate(s2MASSES2, start=12):
    print(f"Total mass of halo {i}: {mass}")  


s2STELLAR1 = []
for halo in s2top_halos1:
    stellar_mass = halo.s['mass'].sum()
    s2STELLAR1.append(stellar_mass) 
for i, mass in enumerate(s2STELLAR1):
    print(f"Total stellar mass of halo {i}: {mass}")
s2STELLAR2 = []
for halo in s2top_halos2:
    stellar_mass = halo.s['mass'].sum()
    s2STELLAR2.append(stellar_mass)
for i, mass in enumerate(s2STELLAR2, start=12):
    print(f"Total stellar mass of halo {i}: {mass}")










