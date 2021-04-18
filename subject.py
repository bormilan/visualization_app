#Subject
import pandas as pd
import abc

class Subject():
	""" Subject"""
	def __init__(self):
		self.observers = []
		print("elkészültem")

	def attach(self,Observer):
		self.observers.append(Observer)
		self.Notify()

	def detach(Observer):
		self.observers.pop(Observer)

	def Notify(self):
		for observer in self.observers:
			observer.update()

	@abc.abstractmethod
	def getState():
		pass

class Dataset(Subject):

	def __init__(self,path):
		super().__init__()
		self.data = pd.read_csv(path)

	def getState(self):
		return self.data


		
		
