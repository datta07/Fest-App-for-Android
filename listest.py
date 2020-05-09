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
import network

#print(k1,k2)
#k1={1:'9:00 \t inarugration',2:'11:00 \t Coding round 1',3:'1:00 \t lunch',3:'3:00 \t Quiz round 2',4:'5:00 \t flash mob',5:'6:30 -Cult night'}
#k2={1:'10:15 \t coading round 2',2:'11:30 \t debuging',3:'1:00  \tlunch',4:'2:00 \t quiz',5:'3:00 \t validatry',6:'5:00 \tcamp fire'}
class lis(Screen):
	theme_cls = ThemeManager()
	def __init__(self):
		super(lis,self).__init__()
		tot=network.get_firebase('Schedule')
		day1=tot['Day1']
		day2=tot['Day2']
		k1={}
		k2={}
		for no,i in enumerate(day1):
			if (no==0):
				continue
			k1[no]=i.replace('\\t','\t')
		for no,i in enumerate(day2):
			if (no==0):
				continue
			k2[no]=i.replace('\\t','\t')
		self.name='shed'
		t=Toolbar(title='shedule',md_bg_color= self.theme_cls.primary_color,background_palette='Primary')
		t.add_widget(MDRaisedButton(text='back',on_press=lambda x:self.cng_scr('vute')))
		#b1=BoxLayout(orientation='vertical')
		b1=GridLayout(rows=12)
		n=MDList()
		l1=OneLineListItem(text='Day 1')
		n.add_widget(l1)
		k1_key=k1.keys()
		for i in k1_key:
			ln=OneLineListItem(text=k1[i])
			n.add_widget(ln)
		l3=OneLineListItem(text='')
		n.add_widget(l3)
		l2=OneLineListItem(text='Day 2')
		n.add_widget(l2)
		k2_key=k2.keys()
		for i in k2_key:
			ln=OneLineListItem(text=k2[i])
			n.add_widget(ln)

		b1.add_widget(t)
		b1.add_widget(n)
		self.add_widget(b1)
	def cng_scr(self,k):
		self.manager.current=k
