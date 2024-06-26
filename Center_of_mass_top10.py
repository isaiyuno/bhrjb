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

top_halos1 = h1[:5] #shows location of halos and some properties of them like length
print(top_halos1) #prints it


'''top_halos2 = h1[7:8]
print(top_halos2)


top_halos3 = h1[10]
print(top_halos3)

top_halos4 = h1[12:14]
print(top_halos4)

top_halos5 = h1[16:17]
print(top_halos5)

top_halos6 = h1[21]
print(top_halos6)

top_halos7 = h1[23]
print(top_halos7)

top_halos8 = h1[25:26]
print(top_halos8)

top_halos9 = h1[30:34]
print(top_halos9)

#top_halos = h1[:34]'''
centers_of_mass_s1 = [] #enables the list

for i, halo in enumerate(top_halos1): #for every index in top_halos1, their center of mass will be found 
   com = pynbody.analysis.halo.center_of_mass(halo)
   centers_of_mass_s1.append(com)
   print(f"Center of mass in simulation 1for halo {i}: {com}") #center of mass is printed and written in comprehensible manner



'''#s2 stuff'''
s2top_halos1 = h2[:10] #just printing the halos and their location in file
print(s2top_halos1)

s2top_halos2 = h2[12:15] #same^^
print(s2top_halos2)

centers_of_mass_s2 = [] # enabling list 

for i, halo in enumerate(s2top_halos1):
   com =pynbody.analysis.halo.center_of_mass(halo)
   centers_of_mass_s2.append(com)
   print(f"Center of mass in simulation 2 for halo {i}: {com}")

for j, halo in enumerate(s2top_halos2):
   com =pynbody.analysis.halo.center_of_mass(halo)
   centers_of_mass_s2.append(com)
   print(f"Center of mass in simulation 2 for halo {j}: {com}")

threshold = 200.0 #this is the euclidean distance threshold

matches = [] #this enables lists for matches

def euclidean_distance(a, b): #two points for assessment on their euclidean distance
   return np.linalg.norm(a - b) #uses pythagorean theorem between centers of masses of two halos

for i, com1 in enumerate(centers_of_mass_s1):
    for j, com2 in enumerate(centers_of_mass_s2):
        distance = euclidean_distance(com1, com2)
        if distance < threshold:
            matches.append((i, j, distance))
            print(f"Match found: Halo {i} in s1 and Halo {j} in s2 with distance {distance}")

print("Matches (Halo index in s1, Halo index in s2, Distance):")
for match in matches:
   print(match)


