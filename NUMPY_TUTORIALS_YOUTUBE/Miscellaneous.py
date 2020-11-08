import numpy as np

filedata=np.genfromtxt('data.txt',delimiter=',')
"""data are in this case split by comma"""

filedata = filedata.astype('int32')
print(filedata)

"""Advanced Indexing-BOOLEAN MASKING """

print(filedata[filedata>50])

""""You can index with a list in Numpy"""

a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])


print(np.all(filedata>50,axis=1))

print(~((filedata>50) & (filedata<100)))