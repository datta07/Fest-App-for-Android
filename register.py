from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
import threading
from kivymd.snackbar import Snackbar
import db
from network import set_firebase
import pop
from kivy.app import App
 
Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDTextField kivymd.textfields.MDTextField
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator


<Example>
    name:'rege'
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'cezer 2020-Regestarion'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 10
            left_action_items: [['arrow-left', lambda x: app.back('all')]]


        ScrollView:

            GridLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                
                rows:7
                padding: dp(48)
                spacing: 50

                MDTextField:
                    id:name1
                    hint_text: "enter Name"

                MDTextField:
                    id:name2
                    hint_text: "enter College Name"


                MDTextField:
                    id:email
                    hint_text: "enter email adress"

                MDTextField:
                    id:phone
                    hint_text: "enter phone number"
                    input_type:'number'
                    max_text_length: 10

                MDTextField:
                    id:password
                    hint_text: "enter password"
                    helper_text:"keep remember your password"
                    helper_text_mode: "on_focus"
                    password:True

                MDRaisedButton:
                    text: "register"
                    size_hint:[1,None]
                    on_press:root.show_example_dialog(name1.text,name2.text,email.text,phone.text,password.text)

                MDCard:
                    size_hint: None, None
                    size: dp(320), dp(180)
                    GridLayout:
                        rows:7
                        padding: dp(8)
                        MDLabel:
                            text: 'Note'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        MDLabel:
                            text: 'make sure you have submited accurent details,so that you can get updates frequently'
                            theme_text_color: 'Primary'

            

""")
class Example(Screen):
    
    def show_example_dialog(self,name1,name2,email,phone,password):
        self.dialog = pop.load_pop()
        if (len(name1)==0)|(len(name2)==0)|(len(email)==0)|(len(phone)==0)|(len(password)==0):
            pop.error_pop("please fill all the details")
            return
        if (email[-10:]!='@gmail.com'):
            pop.error_pop("please enter valid email address")
            return

        if (len(phone)<10)|(len(phone)>10):
            pop.error_pop("please enter valid phone number")
            return

        if (len(password)<6):
            pop.error_pop("password should have a minimum 6 digits")
            return
        #self.regis()
        k=threading.Thread(target=self.regis,args=(name1,name2,email,phone,password))
        k.start()
        self.dialog.open()


    def regis(self,name1,name2,email,phone,password):
        email=email.replace('.','')
        data = { email : {'name':name1+' '+name2,'phone':phone,'password':password,'t1':'0','t2':'0','t3':'0','t4':'0','t5':'0','t6':'0','t7':'0','t8':'0'}} 
        response=set_firebase('',data)
        if response==0:
            pop.error_pop('please turn on internet')
            self.dialog.dismiss()
            return
        db.change_all_db(name1+' '+name2,phone,email,'0','0','0','0','0','0','0','0')
        a=App.get_running_app()
        if a.info_state!=0:
            a.info_state=1
        if db.get_status()!='0':
            a.event_scr_effects=[1,1,1,1,1,1]
        db.change_status('1')
        a.main_widget.ids.logStatus.text='logout'
        self.dialog.dismiss()
        Snackbar(text="registered successfully").show()
        self.manager.current='vute'

        
