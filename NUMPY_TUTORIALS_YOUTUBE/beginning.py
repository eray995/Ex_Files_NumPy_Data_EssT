import  numpy as np

a = np.array([1,2,3],dtype='int32')
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

print(b.ndim)

print(b.shape)

#Get Type

print(a.dtype)

#Get Size
print(a.itemsize)
print(b.itemsize)

#Total Size

print(a.nbytes)


"""Accesing specific elements"""

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

"""Get a specific element [r,c] """
print(a[1,5])

""" Get a specific row"""
print(a[0,:])

"""Get a specific column"""
print(a[:,2])

"""Getting even fancier [startindex:endindex:stepsize]"""

print(a[0,1:6:2])

a[1,5]=20
print(a)

a[:,2]=[1,2]
print(a)


""" 3D example"""

b= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

"""Get specific element(work outside in) """

print(b[0,1,1])

"""replace"""
b[:,1,:]=[[9,9],[8,8]]
print(b)
