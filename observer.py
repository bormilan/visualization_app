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

		#Buttons
		self.title1 = tk.Button(text="Head")
		self.title1.config(width=8,height=2)
		self.title1.config(font=("Courier", 15))
		self.title1.place(x=1000-520,y=700-180-70)		
		self.title1.config(relief="groove")		
		self.title1.config(command=lambda: self.setMode(0))

		self.title2 = tk.Button(text="Describe")
		self.title2.config(width=8,height=2)
		self.title2.config(font=("Courier", 15))
		self.title2.place(x=1000-400,y=700-180-70)		
		self.title2.config(relief="groove")
		self.title2.config(command=lambda: self.setMode(1))

		#Label
		self.SummaryLabel = tk.Label()
		self.SummaryLabel.place(x=1000-520,y=700-180)
		self.SummaryLabel.config(bg="thistle2")
		self.SummaryLabel.config(relief="solid")
		self.SummaryLabel.config(width=70,height=10)

	def update(self): 		
		#Button colors
		if self.mode == 0:
			self.title1.config(bg="tomato3")
			self.title2.config(bg="dim gray")
		else:
			self.title1.config(bg="dim gray")
			self.title2.config(bg="tomato3")

		self.SummaryLabel.config(text=self.getSummary())

	#function to get the data from subject
	def getSummary(self):
		if self.mode == 0:	
			return self.subject.getState().head()
		else:
			return self.subject.getState().describe()

	#function to change label mode
	def setMode(self,newMode):
		if newMode == 0:
			self.mode = 0
			self.update()
		else:
			self.mode = 1
			self.update()

class Column(Observer):
	"""SurvivedSum"""
	def __init__(self, Subject):
		super().__init__(Subject)
		self.column = ""

		self.columnLabel = tk.Label()
		self.columnLabel.config(text="nincs oszlop kiválasztva")
		self.columnLabel.place(x=10,y=520)
		self.columnLabel.config(bg="thistle2")
		self.columnLabel.config(relief="solid")
		self.columnLabel.config(width=40,height=10)

		self.entry = tk.Entry(bg="cyan3")
		self.entry.place(x=10,y=480,width=100,height=30)
		self.entry.bind('<Return>',(lambda event: self.setColumn(self.entry.get())))

		self.button = tk.Button(text="Ok")
		self.button.config(width=8,height=2)
		self.button.config(font=("Courier", 15))
		self.button.place(x=120,y=450)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.entry.get()))

	def setColumn(self,column):
		self.column = column
		self.update()

	def update(self):	
		try:
			sum = np.sum(self.subject.getState()[self.column])
			self.columnLabel.config(text=sum)
		except KeyError:
			self.columnLabel.config(text="nincs oszlop kiválasztva")
		except TypeError:
			self.columnLabel.config(text="az oszlop adatai nem megfelelőek")