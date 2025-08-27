import numpy as np
a = np.array([1, 2, 3])
print(a)

#mean & median
a = np.array([1,2,3,4])
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))

#reshape
a = np.arange(0,11,2)
print("original:", a)

b = a.reshape(2, 3)
print("reshaped:", b)

#random np.random.rand()

a = np.random.rand()
print(a)
b = np.random.rand(5)
print(b)
c = np.random.rand(2, 3)
print(c)

#np.random.randint()
a = np.random.randint(1, 10)
print(a)
y = np.random.randint(1, 100, size=5)
print(y)
z = np.random.randint(10, 21, size=(3, 3))
print(z)

#six digit otp generation
otp = np.random.randint(100000, 999999)
print("OTP:", otp)

#zeros & ones
print(np.zeros((2, 3)))
print(np.ones((3, 4)))