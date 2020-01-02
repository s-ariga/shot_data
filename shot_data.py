import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm
import pylab as plb

# shot-data.csv has column 'CoordinateX' and 'CoordinateY'
data = pd.read_csv("shot-data.csv")

param = norm.fit(data['CoordinateX'])
print(param)

# np.linspace(下限, 上限, 要素数)
x = np.linspace(-20, 20, 200)
pdf_fitted = norm.pdf(x, loc=param[0], scale=param[1])
pdf = norm.pdf(x)

fig = plt.figure()

plt.title('Histogram of AR 5970 shots')
plt.xlabel('mm')
plt.ylabel('freq')
plt.plot(x, pdf_fitted)
plt.hist(data['CoordinateX'], bins=200, range=(-20, 20), density=True)
plt.show()