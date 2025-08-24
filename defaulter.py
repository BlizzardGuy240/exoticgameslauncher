import pickle
f = open("sensitive.dat", "wb")
d = {"admin": "123123"}
pickle.dump(d, f)
f.close()