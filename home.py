from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.metrics import dp
import threading
from kivy.app import App
from events import contact
import listest


Builder.load_string("""

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


<home_screen>
    name:'vute'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2020'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['face', lambda x: app.load_info()]]
        ScrollView:
            do_scroll_x: False
            GridLayout:
                padding: 15
                rows:10
                cols: 2
                spacing: 10
                size_hint_y: None
                height: self.minimum_height/2.5
                row_default_height:
                    (0.5 * (self.width - self.spacing[0]) -
            		self.padding[0])
                row_force_default: True

    	    	Button:
        	    	id: events
            		background_color: C('#3498db')
                    text:root.prof(1)
                    on_press: root.cng_scr('event')
    	    		background_normal: 'button_normal.png'
        			background_down: 'button_down.png'
                    font_size: 24
                    halign: 'center'
    	    		markup: True

                Button:
                    background_color: C('#2ecc71')
                    text:root.prof(2)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    on_press: root.cng_scr('shed')
                    font_size: 24
                    halign: 'center'
                    markup: True

                Button:
                    background_color: C('#e74c3c')
                    text: root.prof(3)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    on_press: root.cng_scr('pro')
                    font_size: 24
                    halign: 'center'
                    markup: True

                Button:
                    background_color: C('#1bbc96')
                    text: root.prof(4)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    on_press: app.gallery()
                    font_size: 24
                    halign: 'center'
                    markup: True
                Button:
                    background_color: C('#27ae60')
                    text: root.prof(5)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    font_size: 24
                    on_press: root.cng_scr('spons')
                    halign: 'center'
                    markup: True
                Button:
                    background_color: C('#16a085')
                    text: root.prof(6)
                    on_press: app.load_map()
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    font_size: 24
                    halign: 'center'
                    markup: True
                Button:
                    background_color: C('#c9b9e5')
                    text: root.prof(7)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    font_size: 24
                    halign: 'center'
                    on_press: root.cng_scr('cont')
                    markup: True
                Button:
                    background_color: C('#95a5a6')
                    text: root.prof(8)
                    background_normal: 'button_normal.png'
                    background_down: 'button_down.png'
                    font_size: 24
                    halign: 'center'
                    markup: True
                    on_press: app.cng_scr('feed')

                            """)

class home_screen(Screen):  
    def cng_scr(self,k):
        if (k=='cont'):
            App.get_running_app().cng_screen('cont',1)
            return
        if (k=='shed'):
            App.get_running_app().cng_screen('shed',1)
            return
        self.manager.current=k
    def prof(self,k):
        if k==1:
            return ('[font=Modern Pictograms][size=120]a[/size][/font]\n Events')
        elif k==2:
            return  '[font=Modern Pictograms][size=120]4[/size][/font]\n Schedule'
        elif k==3:
            return '[font=Modern Pictograms][size=120]g[/size][/font]\n Our Faculty'
        elif k==4:
            return '[font=Modern Pictograms][size=120]A[/size][/font]\n Our Gallery'
        elif k==5:
            return '[font=Modern Pictograms][size=120]#[/size][/font]\n Our Sponsors'
        elif k==6: 
            return  '[font=Modern Pictograms][size=120]w[/size][/font]\n Directions'
        elif k==7:
            return '[font=Modern Pictograms][size=120]m[/size][/font]\n Contact Us'
        elif k==8:
            return '[font=Modern Pictograms][size=120]e[/size][/font]\n Feedback'
            
   