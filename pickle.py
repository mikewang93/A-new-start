import pickle
list=['Mike','1','Z','forever']
pickle_file = open('list.pkl','wb')
pickle.dump(list,pickle_file)
pickle_file.close() //Write file

pickle_file = open('list.pkl','rb') //Open file
list2 = pickle.load(pickle_file)
print (list2)
