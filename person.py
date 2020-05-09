from kivymd.list import MDList
from kivymd.list import OneLineListItem
from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager
from kivymd.toolbar import Toolbar 
from kivymd.button import MDRaisedButton 
import db
proj=['Paper Presentation','Poster Presentation','Tectonic-Bug','Code Race','Quiz','Aavishkar']
class lis(Screen):
	theme_cls = ThemeManager()
	def __init__(self):
		super(lis,self).__init__()
		self.k1=db.get_db('all')
		self.k2=self.k1[3:]
		k1=self.k1
		k2=self.k2
		self.name='info'
		t=Toolbar(title='personal info',md_bg_color= self.theme_cls.primary_color,background_palette='Primary')
		t.add_widget(MDRaisedButton(text='back',on_press=lambda a:self.cng_scr('vute')))
		#b1=BoxLayout(orientation='vertical')
		b1=GridLayout(rows=12)
		n=MDList()
		l1=OneLineListItem(text='Details')
		n.add_widget(l1)
		name=k1[0].split(' ')[0]
		n.add_widget(OneLineListItem(text='Name :\t'+name))
		n.add_widget(OneLineListItem(text='phone :\t'+k1[1]))
		n.add_widget(OneLineListItem(text='email :\t'+k1[2]))
		l3=OneLineListItem(text='')
		n.add_widget(l3)
		l2=OneLineListItem(text='Registered courses')
		n.add_widget(l2)
		cou=1
		for i in range(len(k2)):
			if k2[i]=='1':
				ln=OneLineListItem(text=str(cou)+')  '+proj[i])
				cou+=1
				n.add_widget(ln)
		if cou==1:
			ln=OneLineListItem(text='no regestered courses')
			n.add_widget(ln)
			

		b1.add_widget(t)
		b1.add_widget(n)
		self.add_widget(b1)
	def cng_scr(self,t):
		self.manager.current=t