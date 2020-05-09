from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.theming import ThemeManager
from kivy.app import App


Builder.load_string("""

#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import SmartTile kivymd.grid.SmartTile



<profser>
    name:'pro'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2k19-Faculty'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        GridLayout:
            cols: 1
            padding: dp(4), dp(4)
            spacing: dp(4)
            SmartTileWithLabel:
                mipmap: True
                source: 'prof2.jpg'
                text: "DR SURESH KUMAR"
                on_press:app.cng_screen('prof1',1)
            BoxLayout:
                SmartTileWithLabel:
                    mipmap: True
                    source: 'prof1.jpg'
                    text: "Prof. MIRYALA. DHANALAKSHMI"
                    on_press:app.cng_screen('prof2',1)
                SmartTileWithLabel:
                    mipmap: True
                    source: 'prof3.jpg'
                    text: "Mrs. CH. Asha Jyothi"
                    on_press:app.cng_screen('prof3',1)
    
<prof1>
    name:'prof1'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2k19-events'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('pro')]]
        RstDocument:
            source: 'prof1.rst'
    
<prof2>
    name:'prof2'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2k19-events'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('pro')]]
        RstDocument:
            source: 'prof2.rst'
    
<prof3>
    name:'prof3'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2k19-events'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('pro')]]
        RstDocument:
            source: 'prof3.rst'
     """)

class profser(Screen):
    theme_cls = ThemeManager()
    def cng_screen(self,k):
        self.manager.current=k
class prof1(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k
class prof2(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k
class prof3(Screen):
    theme_cls = ThemeManager()
    def cng_scr(self,k):
        self.manager.current=k
