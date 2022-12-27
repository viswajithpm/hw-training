import datetime
import json
from datetime import date

class Employee:
	def __init__(self):
		self.log={}
		self.task_list=[]
		self.name=""
	def login(self, emp_id, emp_name):
		self.name=emp_name
		login_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		print("Login successful")
		self.log.update({
			'id':emp_id,
			'name':emp_name,
			'login':login_time
			})	
	def logout(self):
		print("Logout successfully and created log file")
		logout_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		self.log.update({'logout':logout_time})
		dt=date.today()
		dict_str=json.dumps(self.log,indent=1)
		filename=f'{dt}_{self.name}.json'
		file=open(filename,"w")
		file.write(dict_str)
	def addTask(self, title, description):
		self.task_dic={}
		start_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		e=int(input("Task added\n Press 1 when finished."))
		self.task_dic.update({
			'title':title,
			'description':description,
			'start_time':start_time
			})
		if e==1:
			obj_eid.endTask("flag")
	def endTask(self, flag):
		end_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		self.task_dic.update({
			'end_time':end_time,
			'successful':flag
			})
		self.task_list.append((self.task_dic))
		self.log.update({'task':self.task_list})
obj_eid=Employee()
obj_eid.login("100","Athul")
print("=====================")
while True:
	print("Enter a option:")
	choice=int(input("1.AddTask\n2.Logout\n"))
	if choice==1:
		obj_eid.addTask("title","description")
	elif choice==2:
		obj_eid.logout()
		break
	else:
		print("Enter a valid option:")
		break