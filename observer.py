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
		title = tk.Label(text="Summary:")
		title.config(width=8,height=2)
		title.config(font=("Courier", 15))
		title.place(x=1000-450,y=700-150-70)
		title.config(bg="tomato3")
		title.config(relief="solid")

		summary = self.subject.getState().head()
		SummaryLabel = tk.Label(text=summary)
		SummaryLabel.place(x=1000-450,y=700-150)
		SummaryLabel.config(bg="thistle2")
		SummaryLabel.config(relief="solid")
		SummaryLabel.config(width=60,height=9)

class ColumnSum(Observer):
	"""SurvivedSum"""
	def __init__(self, Subject, column):
		super().__init__(Subject)
		self.column = column

	def update(self):
		sum = np.sum(self.subject.getState()[self.column])
		SumLabel = tk.Label(text=sum)
		SumLabel.place(x=100,y=400)
		
