import numpy as np
import matplotlib.pyplot as plt


dataset = [11,12,13,15,16,14,18,17,780,985,17,15,16,14,13,12,18,754,19,11,789,17,17,16]

plt.hist(dataset)
plt.show()
print("Mean:", np.mean(dataset))
print("Median:", np.median(dataset))        