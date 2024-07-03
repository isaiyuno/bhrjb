import pynbody #this imports the package pynbody
import pynbody.analysis.halo
import numpy as np 
import matplotlib.pylab as plt

#this loads all the halos and puts them in physical units
s1 = pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.003200/h148.cosmo50PLK.3072g3HbwK1BH.003200')
s2 = pynbody.load('/mnt/data0/jillian/h148/6144/h148.cosmo50PLK.6144g3HbwK1BH.003264/h148.cosmo50PLK.6144g3HbwK1BH.003264')
s1.physical_units()
s2.physical_units()
h1 = s1.halos()
h2 = s2.halos()

top_halos1 = h1[:6] #listing halos 0-5 in s1
top_halos2 = h1[7:9]
top_halos3 = h1[10:11]
s2top_halos1 = h2[:10] #listing halos 0-9 in s2

def percent_difference(value1, value2): # defining percent difference using math
    return abs(value1-value2) / ((value1 + value2) / 2) * 100

def calculate_masses(halo): # defining calculation of mass using .sum() functinos
    total_mass = halo['mass'].sum()
    dark_matter_mass = halo.d['mass'].sum() 
    stellar_mass = halo.s['mass'].sum() 
    return total_mass, dark_matter_mass, stellar_mass 

masses_s1_1 = [calculate_masses(halo) for halo in top_halos1] #calculates the different masses for halos in s1
masses_s1_2 = [calculate_masses(halo) for halo in top_halos2] #calculates the different masses for halos in s1
masses_s1_3 = [calculate_masses(halo) for halo in top_halos3] #calculates the different masses for halos in s1

masses_s2 = [calculate_masses(halo) for halo in s2top_halos1] #calculates the different masses for halos in s2

# Matrix to store percent differences
percent_diff_matrix = np.zeros((len(h1), len(h2), 3))  # 3 dimensions for total mass, dark matter, and stellar mass

# Compare each halo in s1 with each halo in s2
for i, (total_mass1, dm_mass1, stellar_mass1) in enumerate(masses_s1_1):
    for j, (total_mass2, dm_mass2, stellar_mass2) in enumerate(masses_s2):
        total_mass_diff = percent_difference(total_mass1, total_mass2) #using the percent_difference function we defined
        dm_mass_diff = percent_difference(dm_mass1, dm_mass2)
        stellar_mass_diff = percent_difference(stellar_mass1, stellar_mass2)
        
        # Store percent differences in the matrix
        percent_diff_matrix[i, j, 0] = total_mass_diff
        percent_diff_matrix[i, j, 1] = dm_mass_diff
        percent_diff_matrix[i, j, 2] = stellar_mass_diff
for i in range(len(top_halos1)):
    for j in range(len(s2top_halos1)):
        print(f"Comparison between s1 halo {i} and s2 halo {j}:")
        print(f"Total Mass Difference: {percent_diff_matrix[i, j, 0]:.2f}%")
        print(f"Dark Matter Mass Difference: {percent_diff_matrix[i, j, 1]:.2f}%")
        print(f"Stellar Mass Difference: {percent_diff_matrix[i, j, 2]:.2f}%\n")



for i, (s1total_mass1, s1dm_mass1, s1stellar_mass1) in enumerate(masses_s1_2, start = 7):
    for j, (total_mass2, dm_mass2, stellar_mass2) in enumerate(masses_s2):
        total_mass_diff = percent_difference(s1total_mass1, total_mass2) #using the percent_difference function we defined
        dm_mass_diff = percent_difference(s1dm_mass1, dm_mass2)
        stellar_mass_diff = percent_difference(s1stellar_mass1, stellar_mass2)
        
        # Store percent differences in the matrix
        percent_diff_matrix[i, j, 0] = total_mass_diff
        percent_diff_matrix[i, j, 1] = dm_mass_diff
        percent_diff_matrix[i, j, 2] = stellar_mass_diff
for i in range(len(top_halos2)):
    for j in range(len(s2top_halos1)):
        print(f"Comparison between s1 halo {i} and s2 halo {j}:")
        print(f"Total Mass Difference: {percent_diff_matrix[i, j, 0]:.2f}%")
        print(f"Dark Matter Mass Difference: {percent_diff_matrix[i, j, 1]:.2f}%")
        print(f"Stellar Mass Difference: {percent_diff_matrix[i, j, 2]:.2f}%\n")



for i, (s1total_mass3, s1dm_mass3, s1stellar_mass3) in enumerate(masses_s1_3, start = 10):
    for j, (total_mass2, dm_mass2, stellar_mass2) in enumerate(masses_s2):
        total_mass_diff = percent_difference(s1total_mass3, total_mass2) #using the percent_difference function we defined
        dm_mass_diff = percent_difference(s1dm_mass3, dm_mass2)
        stellar_mass_diff = percent_difference(s1stellar_mass3, stellar_mass2)
        
        # Store percent differences in the matrix
        percent_diff_matrix[i, j, 0] = total_mass_diff
        percent_diff_matrix[i, j, 1] = dm_mass_diff
        percent_diff_matrix[i, j, 2] = stellar_mass_diff
for i in range(len(top_halos3)):
    for j in range(len(s2top_halos1)):
        print(f"Comparison between s1 halo {i} and s2 halo {j}:")
        print(f"Total Mass Difference: {percent_diff_matrix[i, j, 0]:.2f}%")
        print(f"Dark Matter Mass Difference: {percent_diff_matrix[i, j, 1]:.2f}%")
        print(f"Stellar Mass Difference: {percent_diff_matrix[i, j, 2]:.2f}%\n")

