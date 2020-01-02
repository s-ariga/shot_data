import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm
import pylab as plb

# shot-data.csv has column 'CoordinateX' and 'CoordinateY'
data = pd.read_csv("shot-data.csv")

paramX = norm.fit(data['CoordinateX'])
paramY = norm.fit(data['CoordinateY'])
print(paramX)
print(paramY)

# np.linspace(下限, 上限, 要素数)
x = np.linspace(-20, 20, 200)
pdf_fittedX = norm.pdf(x, loc=paramX[0], scale=paramX[1])
pdf_fittedY = norm.pdf(x, loc=paramY[0], scale=paramY[1])
pdf = norm.pdf(x)

fig = plt.figure()

plt.title('Histogram of AR 5970 shots')
plt.xlabel('mm')
plt.ylabel('freq')
plt.plot(x, pdf_fittedX, label="PDF CoordX")
plt.plot(x, pdf_fittedY, label="PDF CoordY")
plt.hist(data['CoordinateX'], bins=200, range=(-20, 20), density=True, label="CoordX")
plt.hist(data['CoordinateY'], bins=200, range=(-20, 20), density=True, label="CoordY")

plt.legend()

# Keep matplotlib on screen
plt.show()