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

		#---MODE BUTTONS---#
		#1
		self.head = tk.Button(text="Head")
		self.head.config(width=8,height=2)
		self.head.config(font=("Courier", 15))
		self.head.place(x=1000-520,y=700-180-70)		
		self.head.config(relief="groove")		
		self.head.config(command=lambda: self.setMode(0))

		#2
		self.describe = tk.Button(text="Describe")
		self.describe.config(width=8,height=2)
		self.describe.config(font=("Courier", 15))
		self.describe.place(x=1000-400,y=700-180-70)		
		self.describe.config(relief="groove")
		self.describe.config(command=lambda: self.setMode(1))

		#---CONTENT LABEL---#
		self.SummaryLabel = tk.Label()
		self.SummaryLabel.place(x=1000-520,y=700-180)
		self.SummaryLabel.config(bg="thistle2")
		self.SummaryLabel.config(relief="solid")
		self.SummaryLabel.config(width=70,height=10)

	def update(self): 		
		#Button colors
		if self.mode == 0:
			self.head.config(bg="tomato3")
			self.describe.config(bg="dim gray")
		else:
			self.head.config(bg="dim gray")
			self.describe.config(bg="tomato3")

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
		self.mode = 0

		#---CONTENT LABEL---#
		self.columnLabel = tk.Label()
		self.columnLabel.config(text="nincs oszlop kiválasztva")
		self.columnLabel.place(x=10,y=600)
		self.columnLabel.config(bg="thistle2")
		self.columnLabel.config(relief="solid")
		self.columnLabel.config(width=20,height=5)

		#---COLUMN NAME ENTRY---#
		self.entry = tk.Entry(bg="cyan3")
		self.entry.place(x=10,y=560,width=100,height=30)
		self.entry.bind('<Return>',(lambda event: self.setColumn(self.entry.get())))

		#---OK BUTTON---#
		self.button = tk.Button(text="Ok")
		self.button.config(width=3,height=1)
		self.button.config(font=("Courier", 15))
		self.button.place(x=120,y=550)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.entry.get()))

		#---MODE BUTTONS---#
		#1
		self.sum = tk.Button(text="Sum")
		self.sum.config(width=6,height=1)
		self.sum.config(font=("Courier", 15))
		self.sum.place(x=180,y=600)		
		self.sum.config(relief="groove")		
		self.sum.config(command=lambda: self.setMode(0))

		#2
		self.type = tk.Button(text="type")
		self.type.config(width=6,height=1)
		self.type.config(font=("Courier", 15))
		self.type.place(x=180,y=650)		
		self.type.config(relief="groove")
		self.type.config(command=lambda: self.setMode(1))

	def setColumn(self,column):
		self.column = column
		self.update()

	def update(self):	
		try:
			self.columnLabel.config(text=self.getColumn())
		except KeyError:
			self.columnLabel.config(text="nincs oszlop kiválasztva")
		except TypeError:
			self.columnLabel.config(text="az oszlop adatai nem megfelelőek")

		#Button colors
		if self.mode == 0:
			self.sum.config(bg="tomato3")
			self.type.config(bg="dim gray")
		else:
			self.sum.config(bg="dim gray")
			self.type.config(bg="tomato3")

	def setMode(self,newMode):
		if newMode == 0:
			self.mode = 0
			self.update()
		else:
			self.mode = 1
			self.update()

	def getColumn(self):
		if self.mode == 0:	
			return np.sum(self.subject.getState()[self.column])
		else:
			return self.subject.getState()[self.column].dtypes