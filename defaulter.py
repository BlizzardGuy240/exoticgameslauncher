import pickle
f = open("sensitive.dat", "wb")
d = {"Admin": "123"}
pickle.dump(d, f)
f.close()