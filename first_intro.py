from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color,Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class kar(Screen):
	def __init__(self):
		super(kar,self).__init__()
		self.name='all'
		self.kw=BoxLayout(orientation='vertical')
		self.k=BoxLayout()
		self.k1=BoxLayout(padding=10,orientation='vertical',spacing=10)
		l=Label(text='[b]Hello, Welcome to Cezar 2020\b',color=[0,0,0,1],markup=True)
		d=MDRaisedButton(text='login',size_hint=[1,0.5],on_press=lambda x:self.reg(1))
		d1=MDRaisedButton(text='register',size_hint=[1,0.5],on_press=lambda x:self.reg(2))
		self.k1.add_widget(l)
		self.k1.add_widget(d)
		self.k1.add_widget(d1)
		self.k.bind(size=self._update1,pos=self._update1)
		with self.k.canvas.before:
			Color(rgb=(1,1,1))
			self.rect=Rectangle(source='cezar.png',pos=[0,0], size=[self.k.size[0]/2,self.k.size[1]/2])
		self.kw.add_widget(self.k)
		self.kw.add_widget(self.k1)
		self.add_widget(self.kw)
	 	#return MDRaisedButton(text='datta',pos_hint={'center_x':0.5,'center_y':0.4},elevation_normal=2,size_hint=[1,0.1])      
		#return Button(text='datta',pos_hint={'center_x':0.5,'center_y':0.4})
	def _update1(self,instance,value):
		self.rect.pos=instance.pos
		self.rect.size=instance.size
	def reg(self,i):
		if (i==2):
			a=App.get_running_app()
			a.path_back.append('all')
			self.manager.current='rege'
		else:
			a=App.get_running_app()
			a.path_back.append('all')
			self.manager.current='logi'
