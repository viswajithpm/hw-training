import datetime
import json
from datetime import date

class Emp:
	def __init__(self):
		self.log={}
		self.task_list=[]
		self.nme=""
	def login(self):
		eid=input("Enter employee id:")
		name=input("Enter employee name:")
		self.nme=name
		login_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		print("Login successful")
		self.log.update({'id':eid,'name':name,'login':login_time})	
	def logout(self):
		print("Logout successfully and created log file")
		logout_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		self.log.update({'logout':logout_time})
		dt=date.today()
		dict_str=json.dumps(self.log,indent=1)
		filename=f'{dt}_{self.nme}.json'
		file=open(filename,"w")
		file.write(dict_str)
	def addTask(self):
		self.task_dic={}
		title=input("Enter the Task Title: ")
		description=input("Enter the description: ")
		start_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		e=int(input("Task added\n Press 1 when finished."))
		self.task_dic.update({'title':title,'description':description,'start_time':start_time})
		if e==1:
			obj_eid.endTask()
	def endTask(self):
		end_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		flag=input("Wheater the task was successful ?(Enter True or False)")
		self.task_dic.update({'end_time':end_time,'successful':flag})
		self.task_list.append((self.task_dic))
		self.log.update({'task':self.task_list})
obj_eid=Emp()
obj_eid.login()
print("=====================")
while True:
	print("Enter a option:")
	ch=int(input("1.AddTask\n2.Logout\n"))
	if ch==1:
		obj_eid.addTask()
	elif ch==2:
		obj_eid.logout()
		break
	else:
		print("Enter a valid option:")
		break