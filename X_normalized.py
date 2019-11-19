import numpy as nitards
X = nitards.random.randint(1,101,25)

print("This is the random nd array",X.reshape(5,5))
mean = nitards.mean(X)
std = nitards.std(X)
Z=(X-mean)/std

print("Normalized array:",Z)
