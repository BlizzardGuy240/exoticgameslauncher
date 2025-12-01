import pickle
# f = open("sensitive.dat", "wb")
# d = {"Admin": "123123"}
# pickle.dump(d, f)
# f.close()

PASSWORD = input("ENTER YOUR MYSQL PASSWORD: ")
f = open("sensitive.dat", "wb")
pickle.dump(PASSWORD, f)
f.close()