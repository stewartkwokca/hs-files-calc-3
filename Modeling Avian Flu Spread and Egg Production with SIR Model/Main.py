import numpy as np
import math
from functions import *
import matplotlib.pyplot as plt

'''
Case Unvax
l = 0.691
e = 1
m = 0.5  # varies by case
w = 0.00018
g = 0  # varies by case
s = 1.0 / 21  # sigma

Case Vax
l = 0.691
e = .5
m = .15  # varies by case
w = 0.00018
g = .35  # varies by case
s = 1.0 / 21  # sigma
'''

maxDays = 365

def f(t, varVals, n):
  dSdt = ((-1 * b * varVals[0] * varVals[2]) / n) - (w * varVals[0]) + (s * varVals[6])
  dEdt = ((b * varVals[0] * varVals[2]) / n) - ((e + w) * varVals[1])
  dIdt = e * varVals[1] - (m + g) * varVals[2]
  dRdt = g * varVals[2] - w * varVals[3]
  dDdt = (varVals[0] + varVals[1] + varVals[3]) * w + (varVals[2]) * m
  dG1dt = l * (varVals[0] + varVals[1] + varVals[3]) - (
    (varVals[0] + varVals[1] + varVals[3]) * w + (varVals[2]) * m)
  dG2dt = (varVals[0] + varVals[1] +
           varVals[3]) * w + (varVals[2]) * m - s * varVals[6]
  return np.array([dSdt, dEdt, dIdt, dRdt, dDdt, dG1dt, dG2dt])

def getBetaUnvax(r):
  return ((1/r) - (1.0/3)) / 2.83142809

def getBetaVax(r):
  return ((1/r) - (1.0/3)) / 2.516824969

def graph(y):
  plt.xlabel('Time (days)')
  plt.ylabel(y)
  plt.title(y)
  plt.legend(loc='upper left')
  plt.show()

initVarVals = [99899, 100, 0, 0, 0, 0, 0]
initPop = initVarVals[0] + initVarVals[1]
r = math.sqrt(46527.8 / (initPop*math.pi))

b = getBetaUnvax(r)  # varies by case
l = 0.691
e = 1
m = 0.5  # varies by case
w = 0.00018
g = 0  # varies by case
s = 1.0 / 21  # sigma

###############################Inputs#########################################
varList = ['Susceptible', 'Exposed', 'Infected', 'Recovered', 'Dead', 'Eggs To Be Sold', 'Eggs To Be Hatched']

results = rk4(f, 0, maxDays, initVarVals, 1, initPop)

x = results[0]
y = [[results[1][j][i] for j in range(len(results[1]))] for i in range (7)]

print("r = " + str(r) + ", area = " + str((math.pi * (r**2))))
print("b = " + str(b))

for i in range(4):
  plt.plot(x, y[i], label = varList[i])
for i in range(4):
  if round(y[i][-1], 4) < 1:
    pass
  elif round(y[i][-1], 4) > 5000:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 1000))
  else:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 3000*i))
graph('Chickens')

plt.show()

for i in range(5):
  plt.plot(x, y[i], label = varList[i])
for i in range(5):
  if round(y[i][-1], 4) < 1:
    pass
  elif round(y[i][-1], 4) > 100000:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 1000))
  else:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 3000*i))
graph('Chickens')

for i in [5, 6]:
  plt.plot(x, y[i], label = varList[i])

for i in [5, 6]:
  if round(y[i][-1], 4) > 1:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-50, y[i][-1] + 100))

plt.plot(x, [100000*l*i for i in x], label = 'Eggs Sold With Constant Population of 100,000')
plt.annotate('Eggs Sold With Constant Population of 100,000' + ': ' + str(round([100000*l*i for i in x][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, [100000*l*i for i in x][-1] + 100))

graph('Eggs')
plt.show()
