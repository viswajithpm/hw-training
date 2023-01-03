import csv
import os.path

file_exists = os.path.isfile('name.csv')

d = {
	'first':'Baked',
	'last':'Beans',
	}
with open('name.csv','w')as cf:
	fields = ['first','last','middle']
	writer = csv.DictWriter(cf,fieldnames=fields)
	for i in range(5):
		if file_exists:
			writer.writerow(d)
		else:
			writer.writeheader()
			writer.writerow(d)



# import os.path


# file_exists = os.path.isfile(filename)

# with open (filename, 'a') as csvfile:
#     headers = ['TimeStamp', 'light', 'Proximity']
#     writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

#     if not file_exists:
#         writer.writeheader()  # file doesn't exist yet, write a header

#     writer.writerow({'TimeStamp': dic['ts'], 'light': dic['light'], 'Proximity': dic['prox']})