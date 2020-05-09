from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
import db
from network import set_firebase
import pop
import threading
from kivymd.snackbar import Snackbar



Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDRaisedButton kivymd.button


<fed>
    name:'feed'
    BoxLayout:
        orientation: 'vertical'
        
        Toolbar:
            id: toolbar
            title: 'cezar 2020-Feedback'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 10
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
            
		BoxLayout:
			padding:20
			spacing:20
			orientation:'vertical'
			TextInput:
				id:tt
				text:''
				multiline:True
			MDRaisedButton:
				text:'Submit Feedback'
				size_hint:1,0.3
				on_press:root.send_fed(tt.text)
			MDRaisedButton:
				text:'More Info'
				size_hint:1,0.3
				on_press:app.pop1()
			
			
			
			""")
class fed(Screen):	
	def send_fed(self,t):
		self.dialoga = pop.load_pop()
		k=threading.Thread(target=self.send_fed1,args=(t,))
		k.start()
		self.dialoga.open()

	def send_fed1(self,t):
		phone=db.get_db('phone')		
		data1 = {phone:t}
		response=set_firebase('feedback',data1)
		self.dialoga.dismiss()
		if response==0:
			pop.error_pop('please on internet')
		else:
			Snackbar(text="Thanks for feedback").show()
			self.manager.current='vute'

