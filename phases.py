import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from alive_progress import alive_bar

fig = plt.figure()

#ax = plt.axes(projection='3d')

Phi1 = np.linspace(-2,2,1000)*np.pi
Phi2 = np.linspace(-2,2,1000)*np.pi

K = np.zeros([1000,1000])
AllowedKs = []
AllowedPhi1 = []
AllowedPhi2 = []

with alive_bar(1000000,title='Calculating Allowed Phases',length=20,bar='filling',spinner='dots_waves2') as bar:
    for l,phi1 in enumerate(Phi1):
        for k,phi2 in enumerate(Phi2):
            absk = np.abs( (1+np.exp(phi1*(1j))+np.exp(phi2*(1j)))/( (1+np.exp(phi1*(0.5j))+np.exp(phi2*(0.5j)) )**2 ) )
            if (2/3+0.01) > absk > (2/3-0.01):
                AllowedKs.append(absk)
                AllowedPhi1.append(phi1/np.pi)
                AllowedPhi2.append(phi2/np.pi)
            bar()

plt.scatter(AllowedPhi1,AllowedPhi2,color='black',s=0.5)
plt.xlabel('$φ_1$/π')
plt.ylabel('$φ_2$/π')
plt.show()
