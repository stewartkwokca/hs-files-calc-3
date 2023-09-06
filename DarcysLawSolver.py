import numpy as np

# Constants
mu = 0.001002 # According to this journal (https://aip.scitation.org/doi/abs/10.1063/1.1707481?journalCode=jap), viscosity of water at 20 degrees celsius is 1.002 centipoise = 0.001002 Pa-s)
rho = 998 # According to this government website (https://www.usgs.gov/special-topics/water-science-school/science/water-density), density of water is 0.99802 g / cm^3 at 21 degrees celsius (70 degrees Fahrenheit). That's 998 kg/m^3
g = 9.8 # 9.8 is acceleration due to gravity

"""
Preconditions:
Sizes of phiList, kList, and xList must be the same(because the number of different sections in the aquifer is constant)
phiList, kList, and xList must not be empty
Cross-sectional area of aquifer is assumed to be constant (not an input stated in instructions)

Parameters:
h_0 - initial height of water flowing into aquifer (piezometric head)
h_f - final height of water flowing out of aquifer (piezometric head)
phiList - array of porosity values for each section of the aquifer
kList - array of permeability values for each section of the aquifer
xList - array of lengths of each section of the aquifer

Returns:
v - array of velocities
"""

def solve(h_0, h_f, kList, xList, phiList):
    p_0 = g * rho * h_0 
    p_f = g * rho * h_f

    for i in range(len(kList)):
        kList[i] = float(kList[i]) # Elements within lists should be floats to prevent truncation during division
        xList[i] = float(xList[i])
        phiList[i] = float(phiList[i])

    if len(kList) >= 3:
        n = len(kList) - 1
        M = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            M[i][i] = (kList[i] / xList[i]) + (kList[i+1] / xList[i+1])
            if i > 0:
                M[i][i-1] = -1 * kList[i] / xList[i]
            if i < n-1:
                M[i][i+1] = -1 * kList[i+1] / xList[i+1]
                
        b = [0 for i in range(n)]
        b[0] = p_0 * kList[0] / xList[0]
        b[-1] = p_f * kList[-1] / xList[-1]

        mMatrix = np.array(M)
        bMatrix = np.array(b)
     
        pList = np.linalg.solve(mMatrix, bMatrix).tolist()
        pComplete = [p_0] + pList + [p_f]

        vList = [(kList[i] * (pComplete[i] - pComplete[i+1])) / (phiList[i] * xList[i] * mu) for i in range(len(kList))]
        
        return vList

    elif len(kList) == 2:
        p_1 = ((kList[0]/xList[0] * p_0) + (kList[0]/xList[1] * p_f)) / ((kList[0] / xList[0]) + (kList[1] / xList[1]))
        pComplete = [p_0, p_1, p_f]
        return [(pComplete[i] - pComplete[i+1]) * kList[i] / (mu * xList[i] * phiList[i]) for i in range(2)]

    else: # len(kList) == 1 due to preconditions
        return [(p_0 - p_f) * kList[0] / (mu * xList[0] * phiList[0])]
    

    
    
