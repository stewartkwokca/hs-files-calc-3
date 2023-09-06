import numpy as np

def rk4(f, t0, tf, varVals0, deltaT, n):
  t = np.arange(t0, tf + deltaT, deltaT)  # time array
  varVals = np.zeros((len(t), len(varVals0)))  # solution array
  varVals[0] = varVals0
  for i in range(len(t) - 1):
    k1 = f(t[i], varVals[i], n)
    k2 = f(t[i] + deltaT / 2, varVals[i] + deltaT / 2 * k1, n)
    k3 = f(t[i] + deltaT / 2, varVals[i] + deltaT / 2 * k2, n)
    k4 = f(t[i] + deltaT, varVals[i] + deltaT * k3, n)
    varVals[i + 1] = varVals[i] + deltaT / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
  return t, varVals
