from tkinter import *
import Pmw

class SLabel(Frame):
	'''SLabel defines a 2-sided label within a Frame. The left hand label has blue letters; the right has white letters'''
	def __init__(self,master,leftl,rightl):
		Frame.__init__(self,master,bg='gray40')
		self.pack(side=LEFT,expand=YES,fill=BOTH)
		Label(self,text=leftl,fg='steelblue1',font=("arial",6,"bold"),width=1,bg='gray40').pack(side=LEFT,expand=YES,fill=BOTH)
		Label(self,text=rightl,fg='white',font=("arial",6,"bold"),width=1,bg="gray40").pack(side=RIGHT,expand=YES,fill=BOTH)
		
class Key(Button):
	def __init__(self,amster,font=('arial',8,'bold'),fg='white',width=5,borderwidth=5,**kw):
		kw['font']=font
		kw['fg']=fg
		kw['width']=width
		kw['borderwidth']=borderwidth
		apply(Button.__init__,(self,amster),kw)
		self.pack(side=LEFT,expand=NO,fill=NONE)
		
class Calculator(Frame):
	def __init__(self,parent=None):
		Frame.__init__(self,bg='gray40')
		self.pack(expand=YES,fill=BOTH)
		self.master.title('Tkinter Toolkit TT-42')
		self.master.iconname('Tk-42')
		self.calc=Evaluator()
		self.buildCalculator()
		
		self.actionDict={'second':self.doThis,'mode':self.doThis,'delete':self.doThis,'alpha':self.doThis,'stat':self.doThis,'math':self.doThis,'matrix':self.doThis,
		'program':self.doThis,'vars':self.doThis,'clear':self.clearall,'sin':self.doThis,'cos':self.doThis,'tan':self.doThis,'up':self.doThis,'X1':self.doThis,'X2':self.doThis,
		'log':self.doThis,'ln':self.doThis,'store':self.doThis,'off':self.turnoff,'neg':self.doThis,'enter':self.doEnter}
		
		self.current=" "
		
	def doThis(self,action):
		print('"%s" has not been implemented'%action)
	def turnoff(self,*args):
		self.quit()
	def clearall(self,*args):
		self.current=" "
		self.display.component('text').delete(1.0,END)
	def doEnter(self,*args):
		self.display.insert(END,'\n')
		result=self.calc.runpython(self.current)
		if result:
			self.display.insert(END,'%s\n'%result,'ans')
		self.current=""
	def doKeypress(self,event):
		key=event.char
		if key !='\b':
			self.current=self.current+key
		else:
			self.current=self.current[:-1]
	def keyAction(self,key):
		self.display.insert(END,key)
		self.current=self.current+key
	def evalAction(self,action):
		try:
			self.actionDict[action](action)
		except KeyError:
			pass
	
	def buildCalculator(self):
		FUN=1
		KEY=0
		KC1='gray30'
		KC2='gray50'
		KC3='steelblue1'
		KC4='steelblue'
		keys=[
		[('2nd','','',KC3,FUN,'second'),
		('Mode','Quit','',KC1,FUN,'mode'),
		('Del','Ins','',KC1,FUN,'delete'),
		('Alpha','Lock','',KC2,FUN,'alpha'),
		('Stat','List','',KC2,FUN,'stat'),
		],
		[
		('Math','Test','A',KC1,FUN,'math'),
		('Mtrx','Angle','B',KC1,FUN,'matrix'),
		('Prgm','Draw','C',KC1,FUN,'program'),
		('Vars','YVars','',KC1,FUN,'vars'),
		('Clr','','',KC1,FUN,'clear'),
		],
		[('X-1','Abs','D','KC1',FUN,'X1'),
		('Sin','Sin-1','E',KC1,FUN,'sin'),
		('Cos','Cos-1','F',KC1,FUN,'cos'),
		('Tan','Tan-1','G',KC1,FUN,'tan'),
		('^','PI','H',KC1,FUN,'up')
		],
		[('X-2','Root','I',KC1,FUN,'X2'),
		(',','EE','J',KC1,KEY,','),
		('(','{','K',KC1,KEY,'('),
		(')','}','L',KC1,KEY,')'),
		('/','','M',KC4,KEY,'/')
		],
		[('Log','10x','N',KC1,FUN,'log'),
		('7','Un-1','O',KC2,KEY,'7'),
		('8','Vn-1','P',KC2,KEY,'8'),
		('9','n','Q',KC2,KEY,'9'),
		('X','[','R',KC4,KEY,'*')
		],
		[('Ln','ex','S',KC1,FUN,'ln'),
		('4','L4','T',KC2,KEY,'4'),
		('5','L5','U',KC2,KEY,'5'),
		('6','L6','V',KC2,KEY,'6'),
		('-',']','W',KC4,KEY,'-')
		],
		[('STO','RCL','X',KC1,FUN,'store'),
		('1','L1','Y',KC2,KEY,'1'),
		('2','L2','Z',KC2,KEY,'2'),
		('3','L3','',KC2,KEY,'3'),
		('+','MEM','"',KC4,KEY,'+')
		],
		[('Off','','',KC1,FUN,'off'),
		('0','','',KC2,KEY,'0'),
		('.',':','',KC2,KEY,'.'),
		('(-)','ANS','?',KC2,FUN,'neg'),
		('Enter','Entry','',KC4,FUN,'enter')
		]]
		self.display=Pmw.ScrolledText(self,hscrollmode='dynamic',vscrollmode='dynamic',hull_relief='sunken',hull_background='gray40',hull_borderwidth=10,
		text_background='honeydew4',text_width=16,text_foreground='black', text_height=16,text_padx=10,text_pady=10,text_relief='groove',text_font=('arial',12,'bold'))
		self.display.pack(side=TOP,expand=YES,fill=BOTH)
		self.display.tag_config('ans',foreground='white')
		self.display.component('text').bind('<Key>',self.doKeypress)
		self.display.component('text').bind('<Return>',self.doEnter)
		
		for row in keys:
			rowa=Frame(self,bg='gray40')
			rowb=Frame(self,bg='gray40')
			for p1,p2,p3,color,Ktype,func in row:
				if Ktype==FUN:
					a=lambda s=self,a=func:s.evalAction(a)
				else:
					a=lambda s=self,k=func:s.keyAction(k)
					
				SLabel(rowa,p2,p3)
				Key(rowb,text=p1,bg=color,command=a)
			rowa.pack(side=TOP,expand=YES,fill=BOTH)
			rowb.pack(side=TOP,expand=YES,fill=BOTH)
			
class Evaluator:
	def __init__(self):
		self.myNameSpace={}
		self.runpython("from math import *")
	def runpython(self,code):
		try:
			return eval(code,self.myNameSpace,self.myNameSpace)
		except SyntaxError:
			try:
				exec (code in self.myNameSpace,self.myNameSpace)
			except:
				return 'Error'
				
Calculator().mainloop()
