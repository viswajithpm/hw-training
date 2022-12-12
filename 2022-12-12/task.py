import datetime
import json
from datetime import date

class Emp:
	def __init__(self,eid,name):
		self.eid=eid
		self.name=name
		self.lst=[]
		self.dictionary={}

	def login(self):
		login_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		self.dictionary.update({
			'name':self.name,
			'id':self.eid,
			'login_time':login_time,
		})

	def logout(self):
		logout_time=datetime.datetime.now().isoformat().replace("T"," ")[0:16]
		self.dictionary.update({
			'logout_time':logout_time,
		})
		dt=date.today()
		dict_str=json.dumps(self.dictionary,indent=1)
		filename=f'{dt}_{self.name}.json'
		file=open(filename,"w")
		file.write(dict_str)

	def addTask(self,*details):
		for items in details:
			self.lst.append(items)
		self.dictionary.update({
			'tasks':self.lst
		})

	def endTask(self,*details):
		for items in details:
			self.lst.append(items)
		self.dictionary.update({
			'tasks':self.lst
		})
		
eid=input("Enter employee id:")
name=input("Enter employee name:")

obj_eid=Emp(eid,name)
obj_eid.login()
obj_eid.addTask("title","description","start")
obj_eid.endTask("end","flag")
obj_eid.logout()