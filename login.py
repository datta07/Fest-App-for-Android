from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
import threading
import db
from network import get_firebase
from kivymd.snackbar import Snackbar
import pop
from kivy.uix.screenmanager import FadeTransition

Builder.load_string("""


<exmple>
    name:'logi'
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'cezer 2020-Login'
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
                    hint_text: "enter email address"

                MDTextField:
                    id:name2
                    hint_text: "enter password"
                    password:True



                MDRaisedButton:
                    text: "login"
                    size_hint:[1,None]
                    on_press:root.show_example_dialog(name1.text,name2.text)

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
                            text: 'welcome to cezar 2020'
                            theme_text_color: 'Primary'

            

""")

class exmple(Screen): 

    def show_example_dialog(self,name1,name2):
        self.dialog = pop.load_pop()
        k=threading.Thread(target=self.regis,args=(name1,name2))
        k.start()
        self.dialog.open()


    def regis(self,email,password):
        if (email=='' )| (password==''):
            pop.error_pop('fill all the partuculars')
            self.dialog.dismiss()
            return

        email=email.replace('.','')
        r2=get_firebase(email)
        if r2!=0:
            if (r2==None):
                pop.error_pop('entered non registerd email address')    
                self.dialog.dismiss()
                return
            r=str(r2['password'])
            if (r!=password):
                pop.error_pop('incorrect password')    
                self.dialog.dismiss()
                return
            db.change_all_db(r2['name'],r2['phone'],email,r2['t1'],r2['t2'],r2['t3'],r2['t4'],r2['t5'],r2['t6'],r2['t7'],r2['t8'])
            db.change_status('1')
            self.dialog.dismiss()
            a=App.get_running_app()
            if a.info_state!=0:
                a.info_state=1
            a.event_scr_effects=[1,1,1,1,1,1]
            Snackbar(text="login success").show()
            a.main_widget.ids.logStatus.text='logout'    
            #self.manager.=FadeTransition
            self.manager.current='vute'
        else:
            pop.error_pop('no internet connection')
            self.dialog.dismiss()
