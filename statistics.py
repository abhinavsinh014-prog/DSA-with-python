gems = [18,29,27,45,23,25,24,26,27,29,36,34,35,38,152]

import numpy as np

print(np.mean(gems))
print(np.median(gems))

q1 ,q3 = np.percentile(gems,[25,75])
print(q1,q3)

IQR = q3 - q1
print(IQR)


lower_flance = q1 - 1.5*IQR
Higher_flance = q3 + 1.5*IQR
print(lower_flance,Higher_flance)

