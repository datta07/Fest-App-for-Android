from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.metrics import dp
def load_pop():
	content = MDLabel(font_style='Title',theme_text_color='Primary',text='Loading...',size_hint_y=None,valign='top')
	content.bind(texture_size=content.setter('size'))
	dialog = MDDialog(content=content,size_hint=(.8,.2),height=dp(200),auto_dismiss=False)
	return dialog

#the element it takes this function should be named
def conf_pop(dis,but1,action1):
	content = MDLabel(font_style='Body1',theme_text_color='Secondary',text=dis,size_hint_y=None,valign='top')
	content.bind(texture_size=content.setter('size'))
	dialog0 = MDDialog(content=content,size_hint=(.8, None),height=dp(200),auto_dismiss=True)
	dialog0.add_action_button(but1,action= action1)
	dialog0.add_action_button("cancel",action=lambda *x: dialog0.dismiss())
	return dialog0

def error_pop(matter):
	content = MDLabel(font_style='Body1',theme_text_color='Secondary',text=matter,size_hint_y=None,valign='top')
	content.bind(texture_size=content.setter('size'))
	dialog2 = MDDialog(title="Error",content=content,size_hint=(.8, None),height=dp(200),auto_dismiss=False)
	dialog2.add_action_button("Dismiss",action=lambda *x:dialog2.dismiss())
	dialog2.open()
#This PC\Lenovo K8 Plus\SanDisk SD card\Android\data\org.coursera.android\files\Download