1. First, let's make all the necessary imports:
>>> import numpy as np
import scipy.stats as st
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
%matplotlib inline
2. We now define a deterministic nonlinear function underlying our generative model:
>>> def f(x):
return np.exp(3 * x)
3. We generate the values along the curve on :
>>> x_tr = np.linspace(0., 2, 200)
y_tr = f(x_tr)
4. Now, let's generate data points within . We use the function and we add some
Gaussian noise:
>>> x = np.array([0, .1, .2, .5, .8, .9, 1])
y = f(x) + 2 * np.random.randn(len(x))
5. Let's plot our data points on :
>>> fig, ax = plt.subplots(1, 1, figsize=(6, 3))
ax.plot(x_tr, y_tr, '--k')
ax.plot(x, y, 'ok', ms=10)
ax.set_xlim(0, 1.5)
ax.set_ylim(-10, 80)
ax.set_title('Generative model')