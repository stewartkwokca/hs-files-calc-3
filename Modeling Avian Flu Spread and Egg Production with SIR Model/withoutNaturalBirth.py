import numpy as np
import math
from functions import *
import matplotlib.pyplot as plt

'''
Case Unvax
l = 0.691
e = 1
m = 0.5  # varies by case
g = 0  # varies by case

Case Vax
l = 0.691
e = .5
m = .15  # varies by case
g = .35  # varies by case
'''

maxDays = 365

def f(t, varVals, n):
  dSdt = ((-1 * b * varVals[0] * varVals[2]) / n)
  dEdt = ((b * varVals[0] * varVals[2]) / n) - (e * varVals[1])
  dIdt = e * varVals[1] - (m + g) * varVals[2]
  dRdt = g * varVals[2]
  dDdt = varVals[2] * m
  dGdt = l * (varVals[0] + varVals[1] + varVals[3])
  return np.array([dSdt, dEdt, dIdt, dRdt, dDdt, dGdt])

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

initVarVals = [55317, 100, 0, 0, 0, 0]
initPop = initVarVals[0] + initVarVals[1]
r = math.sqrt(46527.8 / (initPop*math.pi))

b = getBetaUnvax(r)  # varies by case
l = 0.691
e = 1
m = 0.5  # varies by case
g = 0  # varies by case
###############################Inputs#########################################
'''
varList = ['Susceptible', 'Exposed', 'Infected', 'Recovered', 'Dead', 'Eggs']

results = rk4(f, 0, maxDays, initVarVals, 1, initPop)

x = results[0]
y = [[results[1][j][i] for j in range(len(results[1]))] for i in range (6)]

print("r = " + str(r) + ", area = " + str((math.pi * (r**2))))
print("b = " + str(b))

for i in range(5):
  plt.plot(x, y[i], label = varList[i])
for i in range(5):
  if round(y[i][-1], 4) < 1:
    pass
  elif round(y[i][-1], 4) > 1000:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 1000))
  else:
    plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, y[i][-1] + 3000*i))
graph('Chickens')

i = 5
plt.plot(x, y[i], label = varList[i])

if round(y[i][-1], 4) > 1:
  plt.annotate(varList[i] + ': ' + str(round(y[i][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-50, y[i][-1] + 100))

plt.plot(x, [100000*l*i for i in x], label = 'Eggs Sold With Constant Population of 100,000')
plt.annotate('Eggs Sold With Constant Population of 100,000' + ': ' + str(round([100000*l*i for i in x][-1], 4)), xy=(x[-1], y[i][-1]), xytext=(x[-1]-125, [100000*l*i for i in x][-1] + 100))

graph('Eggs')
plt.show()
'''

ctr = 0
l = 0.691
e = 1
m = 0.5  # varies by case
g = 0  # varies by case
x = []
y = []
while ctr <= 99899:
  ctr += 1
  initVarVals = [ctr, 100, 0, 0, 0, 0]
  initPop = initVarVals[0] + initVarVals[1]
  r = math.sqrt(46527.8 / (initPop*math.pi))
  b = getBetaUnvax(r)
  results = rk4(f, 0, maxDays, initVarVals, 1, initPop)
  x += [ctr]
  y += [results[1][-1][-1]]
  print(str(ctr) + " " + str(results[1][-1][-1]))

plt.plot(x, y)
plt.xlabel('Initial Susceptible Population')
plt.ylabel('Total Eggs After One Year')
plt.title('Total Eggs vs Initial Susceptible Population')
plt.show()
