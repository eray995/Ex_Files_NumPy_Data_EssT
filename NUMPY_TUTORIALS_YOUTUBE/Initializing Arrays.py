import numpy as np

"""All 0s matrix"""
#print(np.zeros((2,3,3)))

"""2 item 3 X 3 """
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.zeros((2,3)))

"""All is matrix"""

print(np.ones((4,2,2), dtype='int32'))


"""Any other number"""

print(np.full((2,2),99,dtype='float32'))

"""Any other number (full_like)"""

print(np.full_like(a,4))


"""Random decimal numbers"""

print(np.random.rand(4,2))

#print(np.random.random_sample(a.shape))


"""Random Integer Values"""
print(np.random.randint(4,7,size=(3,3)))


print(np.identity(5))

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

"""Exercise"""

output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:4,1:4]=z
print(output)

""""Markdown : Be careful when copying arrays"""

a=np.array([1,2,3])
b=a.copy()
b[0]=100
print(b)
print(a)


