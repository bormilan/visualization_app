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
		self.mode = 0

	def update(self): 
		title1 = tk.Button(text="Summary")
		title1.config(width=8,height=2)
		title1.config(font=("Courier", 15))
		title1.place(x=1000-520,y=700-180-70)		
		title1.config(relief="solid")
		title1.config(command=lambda: self.setMode(0))

		title2 = tk.Button(text="Describe")
		title2.config(width=8,height=2)
		title2.config(font=("Courier", 15))
		title2.place(x=1000-400,y=700-180-70)		
		title2.config(relief="solid")
		title2.config(command=lambda: self.setMode(1))

		if self.mode == 0:
			title1.config(bg="tomato3")
			title2.config(bg="dim gray")
		else:
			title1.config(bg="dim gray")
			title2.config(bg="tomato3")

		SummaryLabel = tk.Label(text=self.getSummary())
		SummaryLabel.place(x=1000-520,y=700-180)
		SummaryLabel.config(bg="thistle2")
		SummaryLabel.config(relief="solid")
		SummaryLabel.config(width=70,height=10)

	def getSummary(self):
		if self.mode == 0:	
			return self.subject.getState().head()
		else:
			return self.subject.getState().describe()

	def setMode(self,newMode):
		if newMode == 0:
			self.mode = 0
			self.update()
		else:
			self.mode = 1
			self.update()

class ColumnSum(Observer):
	"""SurvivedSum"""
	def __init__(self, Subject, column):
		super().__init__(Subject)
		self.column = column

	def update(self):
		sum = np.sum(self.subject.getState()[self.column])
		SumLabel = tk.Label(text=sum)
		SumLabel.place(x=100,y=400)