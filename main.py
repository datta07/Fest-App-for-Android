#project by akula guru datta(Garuda)
from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import SwapTransition
from kivymd.label import MDLabel
from kivy.metrics import dp
from kivymd.card import MDSeparator
from register import Example
from kivy.config import Config
from kivy.clock import Clock
import first_intro
from login import exmple
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from network import set_firebase
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from home import home_screen
from kivymd.snackbar import Snackbar
import listest
import events
import threading
import multiprocessing
import direction
import feed
import db
import pop
import prof
import person
import time
import webbrowser


state=int(db.get_status())
main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader

#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager


NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Cezar 2020"
        NavigationDrawerIconButton:
            icon: 'book'
            text: 'Events'
            on_release: app.root.ids.scr_mngr.current = 'event'
        NavigationDrawerIconButton:
            icon: 'calendar'
            text: 'Schedule'
            on_release: app.cng_screen('shed',1)
        NavigationDrawerIconButton:
            icon: 'nature-people'
            text:'Our Faculty'
            on_release: app.root.ids.scr_mngr.current = 'pro'
        NavigationDrawerIconButton:
            icon: 'image-multiple'
            text: 'Our Gallery'
            on_release: app.gallery()
        NavigationDrawerIconButton:
            icon: 'cash-multiple'
            text: "Our Sponsers"
            on_release: app.root.ids.scr_mngr.current = 'spons'
        NavigationDrawerIconButton:
            icon: 'google-maps'
            text: 'Directions'
            on_release: app.load_map()
        NavigationDrawerIconButton:
            icon: 'contact-mail'
            text: 'Contact Us'
            on_release: app.cng_screen('cont',1)
        NavigationDrawerIconButton:
            icon: 'lead-pencil'
            text: 'Feedback' 
            on_press:app.cng_scr('feed')
        NavigationDrawerIconButton:
            id:logStatus
            icon: 'exit-to-app'
            text: 'Logout'
            on_press: app.show_logout()
    BoxLayout:
        orientation: 'vertical'
        ScreenManager:
            id: scr_mngr
'''




class total(App):
    theme_cls = ThemeManager()
    map_state=0
    info_state=0
    event_scr_effects=[0,0,0,0,0,0]
    path_back=[]
    prof_con=[False,False,False,False,False]
    def cng_scr(self,scr):
        if (db.get_status()==0):
            self.golag=pop.conf_pop('Please Login to submit Feedback','Login',lambda x:self.GoLog())
            self.golag.open()
            return
        self.main_widget.ids.scr_mngr.current=scr


    def logout(self):
        db.change_status('0')
        try:
           self.dialog0.dismiss()
        except Exception:
            pass
        self.main_widget.ids.scr_mngr.current='all'

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        self.main_widget.ids.scr_mngr.transition = SwapTransition()
        self.main_widget.ids.scr_mngr.add_widget(home_screen())
        self.main_widget.ids.scr_mngr.add_widget(first_intro.kar())
        self.main_widget.ids.scr_mngr.add_widget(events.event())
        self.main_widget.ids.scr_mngr.add_widget(prof.profser())
        self.main_widget.ids.scr_mngr.add_widget(events.sponsers())
        self.main_widget.ids.scr_mngr.add_widget(feed.fed())
        self.main_widget.ids.scr_mngr.add_widget(Example())
        self.main_widget.ids.scr_mngr.add_widget(exmple()) 
        return self.main_widget

    def on_start(self): 
        if (db.get_status()==0):
            self.main_widget.ids.logStatus.text='login'
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if (self.main_widget.ids.scr_mngr.current_screen.name=='vute'):
                return True
            level={'logi':'all','rege':'all','info':'vute','show6': 'event', 'show5': 'event', 'show3': 'event', 'show4': 'event','show1': 'event', 'prof1': 'pro', 'prof2': 'pro', 'prof3': 'pro', 'event':'vute','shed': 'vute', 'pro': 'vute', 'spons': 'vute', 'feed': 'vute', 'cont': 'vute', 'dir': 'vute'}
            self.main_widget.ids.scr_mngr.current=level[self.main_widget.ids.scr_mngr.current_screen.name]
        return True

    def on_pause(self):
        return True

    def back(self,sc):
        self.main_widget.ids.scr_mngr.current=sc

    def show_logout(self):
        print(db.get_status())
        if (db.get_status()==0):
            self.logout()
            return
        self.dialog0=pop.conf_pop('are you sure to logout','logout',lambda x:self.logout())
        self.dialog0.open()

    
    def enroll(self,status,event,no):
        if (db.get_status()==0):
            self.golag=pop.conf_pop('Please Login to get Enroll','Login',lambda x:self.GoLog())
            self.golag.open()
            return
        if status=='registered':
            return
        self.dialog0=pop.conf_pop('are you sure to enroll '+event,'enroll',lambda x:self.enroll2(event,no))
        self.dialog0.open()

    def enroll2(self,event,no):
        self.dialog0.dismiss()
        self.dialoga = pop.load_pop()
        k=threading.Thread(target=self.enroll1,args=(event,no))
        k.start()
        self.dialoga.open()

    def enroll1(self,event,no):
    	dblist=db.get_db('all')
    	namedb=dblist[0]
    	numberdb=dblist[1]
    	maildb=dblist[2]
    	data = { numberdb: {'name':namedb}} 
    	k1=set_firebase(event,data)
    	data1 = { 't'+str(no):'1'}
    	k2=set_firebase(maildb,data1)
    	if (k1==0)|(k2==0):
    		pop.error_pop('please turn on internet')
    		self.dialoga.dismiss()
    		return
    	else:
    		db.change_db(no,'1')
    	self.dialoga.dismiss()
    	self.event_scr_effects[no-1]=1
    	if self.info_state!=0:
    		self.info_state=1
    	Snackbar(text="successfully enrolled").show()
    	self.main_widget.ids.scr_mngr.current='event'
        
    def load_map(self):
    	if self.map_state==0:
    		self.main_widget.ids.scr_mngr.add_widget(direction.Venue())
    		self.map_state=1
    	self.path_back.append('vute')
    	self.main_widget.ids.scr_mngr.current='dir'

    def load_info(self):
        if (db.get_status()==0):
            self.golag=pop.conf_pop('Please Login to get info','Login',lambda x:self.GoLog())
            self.golag.open()
            return
        if self.info_state==0:
            self.main_widget.ids.scr_mngr.add_widget(person.lis())
            self.info_state=2
        elif self.info_state==1:
            self.main_widget.ids.scr_mngr.get_screen('info').clear_widgets()
            self.main_widget.ids.scr_mngr.get_screen('info').__init__()
        self.path_back.append('vute')
        self.main_widget.ids.scr_mngr.current='info' 

    def cng_screen(self,non,pro=0):
    	if (self.main_widget.ids.scr_mngr.has_screen(non)):
    		self.cng_screen1(non,pro)
    		return
    	elif (self.main_widget.ids.scr_mngr.has_screen('show'+str(non))):
    		self.cng_screen1(non,pro)
    		return
    	else:
            self.dialoga = pop.load_pop()
            #k=threading.Thread(target=self.cng_screen1,args=(non,pro))
            #k.start()
            Clock.schedule_once(lambda dt: self.cng_screen1(non,pro),0)
            self.dialoga.open()

    def GoLog(self):
        self.main_widget.ids.scr_mngr.current='all'
        try:
            self.golag.dismiss()
        except Exception:
            pass

    def cng_screen1(self,non,pro=0):
        if (pro==1):
            if ((non=="prof1")&(not self.prof_con[0])):
            	print('loading')
            	self.prof_con[0]=True
            	self.main_widget.ids.scr_mngr.add_widget(prof.prof1())
            if ((non=="prof2")&(not self.prof_con[1])):
            	self.prof_con[1]=True
            	self.main_widget.ids.scr_mngr.add_widget(prof.prof2())
            if ((non=="prof3")&(not self.prof_con[2])):
            	self.prof_con[2]=True
            	self.main_widget.ids.scr_mngr.add_widget(prof.prof3())
            if ((non=="cont")&(not self.prof_con[3])):
            	self.prof_con[3]=True
            	self.main_widget.ids.scr_mngr.add_widget(events.contact())
            if ((non=="shed")&(not self.prof_con[4])):
            	try:
                    self.main_widget.ids.scr_mngr.add_widget(listest.lis())
            	except Exception:
            		self.dialog0=pop.conf_pop('no Internet Connection','Dismiss',lambda x:self.dialog0.dismiss())
            		self.dialog0.open()
            		self.dialoga.dismiss()
            		return
            	self.prof_con[4]=True
            try:
            	self.dialoga.dismiss()
            except Exception:
            	pass
            self.main_widget.ids.scr_mngr.current=non
            return

        if not self.main_widget.ids.scr_mngr.has_screen('show'+str(non)):
            if (non==1):
                self.main_widget.ids.scr_mngr.add_widget(events.show1())
                self.event_scr_effects[non-1]=0
            if (non==2):
                self.main_widget.ids.scr_mngr.add_widget(events.show2())
                self.event_scr_effects[non-1]=0
            if (non==3):
                self.main_widget.ids.scr_mngr.add_widget(events.show3())
                self.event_scr_effects[non-1]=0
            if (non==4):
                self.main_widget.ids.scr_mngr.add_widget(events.show4())
                self.event_scr_effects[non-1]=0
            if (non==5):
                self.main_widget.ids.scr_mngr.add_widget(events.show5())
                self.event_scr_effects[non-1]=0
            if (non==6):
                self.main_widget.ids.scr_mngr.add_widget(events.show6())
                self.event_scr_effects[non-1]=0
            self.path_back.append('event')
            try:
            	self.dialoga.dismiss()
            except Exception:
            	pass
            self.main_widget.ids.scr_mngr.current='show'+str(non)
            return
        if self.event_scr_effects[non-1]==0:
            self.path_back.append('event')
            try:
            	self.dialoga.dismiss()
            except Exception:
            	pass
            self.main_widget.ids.scr_mngr.current='show'+str(non)
            return
        posta=int(db.get_db(non))
        if (posta==1):
            nor='registered'
            nocolor=self.theme_cls.green_color
        else:
            nor='enroll'
            nocolor=self.theme_cls.primary_color
        self.main_widget.ids.scr_mngr.get_screen('show'+str(non)).ids.but.text = nor
        self.main_widget.ids.scr_mngr.get_screen('show'+str(non)).ids.but.md_bg_color = nocolor
        self.event_scr_effects[non-1]=0
        self.path_back.append('event')
        try:
        	self.dialoga.dismiss()
        except Exception:
        	pass
        self.main_widget.ids.scr_mngr.current='show'+str(non)

    def pop1(self):
        p=Popup(title='IT 2017-2021',title_color=[1,0,0,1],background='',size_hint=[0.75,0.6])
        b=BoxLayout(orientation='vertical')
        #b.add_widget(Image(source='a1.jpg'))
        b1=BoxLayout(orientation='vertical')
        b1.add_widget(MDSeparator(height= dp(1)))
        b1.add_widget(MDLabel(text='Developed by IT 2017 Batch\n Special Thanks to All who helped this',halign='left'))
        b1.add_widget(MDSeparator(height= dp(1)))
        b.add_widget(b1)
        p.add_widget(b)
        p.open()

    def gallery(self):
        webbrowser.open('https://drive.google.com/folderview?id=112Jf12hrm2V5sjiXXXrRIAY2YMIuwYPa')


if __name__ == '__main__':
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '900')
    LabelBase.register(name='Modern Pictograms',fn_regular='modernpics.ttf')
    k=total().run()