#Observer
import abc
import numpy as np
import tkinter as tk

class Observer():
	"""Observer"""
	def __init__(self,Subject):
		self.subject = Subject

	@abc.abstractmethod
	def update():
		pass

class Summary(Observer):
	"""Summary"""
	def __init__(self,Subject):
		super().__init__(Subject)

	def update(self):
		summary = self.subject.getState().head()
		SummaryLabel = tk.Label(text=summary).place(x=100,y=200)

class ColumnSum(Observer):
	"""SurvivedSum"""
	def __init__(self, Subject, column):
		super().__init__(Subject)
		self.column = column

	def update(self):
		sum = np.sum(self.subject.getState()[self.column])
		SumLabel = tk.Label(text=sum).place(x=100,y=10)
		
