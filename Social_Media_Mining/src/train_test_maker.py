import math
test_split = 0.20

#Read the whole data set
f = open("../data/final_data.csv","rb")
data = f.readlines()
no_of_test_samples = math.floor(len(data)*test_split)
print no_of_test_samples


#Create a dictionary for labels with count
#This count dictionary will be used later for test data
labels_count = {} 
for i in range(1,len(data)):
	k = data[i].split("\n")[0]
	k = k.split(",")
	labels_count[k[1]] = 0


#Write header for train and test dataset
f_train = open("../data/train.csv","w")
f_train.write("Tweet,Category"+"\n")

f_test = open("../data/test.csv","w")
f_test.write("Tweet,Category"+"\n")

#Get the total size for each class 
class_split = no_of_test_samples/float(len(labels_count))
print "Expecting:"+ str(class_split * len(labels_count)) + "rows in test data"

for i in range(1,len(data)):

	k = data[i].split("\n")[0]
	tweet, category = k.split(",")

	if labels_count[category] < class_split:
		f_test.write(k+"\n")
		labels_count[category] +=1
	else:
		f_train.write(k+"\n")

f_test.close()
f_train.close()
