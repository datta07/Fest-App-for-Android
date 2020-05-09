from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager
from kivy.metrics import dp
from kivymd.bottomsheet import MDGridBottomSheet
from kivy.clock import Clock
Clock.max_iteration = 60
import threading
import sqlite3
import db
stat= db.get_db('all')


Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar

<sponsers>
    name:'spons'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Sponsors'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        ScrollView:
            do_scroll_x: False
            GridLayout:
                padding: 40
                rows:10
                spacing: 30
                size_hint_y: None
                height: self.minimum_height/1.65
                row_default_height:
                    (0.5 * (self.width - self.spacing[0]) -
                    self.padding[0])
                row_force_default: True

                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'ACE'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'ace.jpg'
                            on_press:
                                import webbrowser
                                webbrowser.open('https://www.time4education.com/')
                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'SBI'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'sponser3.jpg'
                            on_press:
                                import webbrowser
                                webbrowser.open('https://www.onlinesbi.com/')
                    
<event>
    name:'event'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Events'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        ScrollView:
            do_scroll_x: False
            GridLayout:
                padding: 40
                rows:10
                spacing: 30
                size_hint_y: None
                height: self.minimum_height/1.65
                row_default_height:
                    (0.5 * (self.width - self.spacing[0]) -
            		self.padding[0])
                row_force_default: True

                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'code_race'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'code_race.jpeg'
                            on_press:app.cng_screen(4)
                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'quiz'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'quiz.jpeg'
                            on_press:app.cng_screen(5)
                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'project expo'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'project.jpeg'
                            on_press:app.cng_screen(6)
                MDCard:
                    size_hint: 1, 1.5
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'paper expo'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        Button:
                            background_normal:'paper.jpeg'
                            on_press:app.cng_screen(1)

<show1>
    name:'show1'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'PPT'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('event')]]
        RstDocument:
            source: 'paper.rst'
		MDRaisedButton:
			id: but
			text: 'enroll'
			size_hint:[1,0.1]
            md_bg_color:root.color()
            on_press:app.enroll(but.text,'paper',1)

<show4>
    name:'show4'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Geek Race'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('event')]]
        RstDocument:
            source: 'code_race.rst'
		MDRaisedButton:
			id: but
			text: 'enroll'
			size_hint:[1,0.1]
            md_bg_color:root.color()
            on_press:app.enroll(but.text,'code_race',4)

<show5>
    name:'show5'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Quiz'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('event')]]
        RstDocument:
            source: 'quiz.rst'
		MDRaisedButton:
			id: but
			text: 'enroll'
			size_hint:[1,0.1]
            md_bg_color:root.color()
            on_press:app.enroll(but.text,'quiz',5)
<show6>
    name:'show6'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Project Expo'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('event')]]
        RstDocument:
            source: 'project.rst'
		MDRaisedButton:
			id: but
			text: 'enroll'
			size_hint:[1,0.1]
            md_bg_color:root.color()
            on_press:app.enroll(but.text,'project',6)

<contact>
    name:'cont'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Contact us'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        RstDocument:
            source: 'contact.rst'
        MDRaisedButton:
            id: but
            text: 'follow us'
            size_hint:[1,0.1]
            on_press: root.show_example_grid_bottom_sheet()

                            """)

class event(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k

class contact(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k
    def show_example_grid_bottom_sheet(self):
        bs = MDGridBottomSheet()
        bs.add_item("Website", lambda x: self.conn(1),
                    icon_src='web.jpg')
        bs.add_item("Instagram", lambda x: self.conn(2),
                    icon_src='insta.png')
        bs.open()
    def conn(self,i):
        import webbrowser
        if (i==1):
            webbrowser.open("https://jntuhcej.ac.in/viewdept/16") 
        else:
            webbrowser.open("https://www.instagram.com/cezar_2k20/")

class sponsers(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k

class show1(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(1))
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor

class show2(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(2))
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor

class show3(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(3))
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor
        
class show4(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(4))
        
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor

class show5(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(5))
        
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor

class show6(Screen):
    theme_cls = ThemeManager()
    def color(self):
        posta=int(db.get_db(6))
        
        if (db.get_status()==0):
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        elif (posta==1):
            self.ids.but.text='registered'
            nocolor=self.theme_cls.green_color
        else:
            self.ids.but.text='enroll'
            nocolor=self.theme_cls.primary_color
        return nocolor