from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.theming import ThemeManager
Builder.load_string("""

#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import SmartTile kivymd.grid.SmartTile



<photos>
    name:'phot'
    BoxLayout:
        orientation:'vertical'
        Toolbar:
            id: toolbar
            title: 'Cezar 2k19-sponsers'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        GridLayout:
            cols: 2
            padding: dp(4), dp(4)
            spacing: dp(4)
            SmartTileWithLabel:
                mipmap: True
                source: 'gallery 1.jpeg'
                on_press:root.cng_screen('loadimg','gallery 1.jpeg')
            SmartTile:
                mipmap: True
                source: 'gallery 2.jpeg'
                on_press:root.cng_screen('loadimg','gallery 2.jpeg')
            SmartTile:
                mipmap: True
                source: 'gallery 3.jpeg'
                on_press:root.cng_screen('loadimg','gallery 3.jpeg')
            SmartTile:
                mipmap: True
                source: 'gallery 4.jpg'
                on_press:root.cng_screen('loadimg','gallery 4.jpg')

<loadimage>
    name: 'loadimg'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(13)
        Toolbar:
            id: toolbar
            title: 'Directions'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 10
            left_action_items: [['arrow-left', lambda x: app.back('phot')]]
        BoxLayout
            orientation: 'vertical'
            AsyncImage:
                id: img_venue
                source: 'gallery 1.jpeg'
                allow_stretch: True
                keep_ratio: True
    """)


class photos(Screen):
    theme_cls = ThemeManager()
    def cng_screen(self,k,img):
        self.manager.get_screen(k).ids.img_venue.source=img
        self.manager.current=k

class loadimage(Screen):
    theme_cls = ThemeManager()
    def cng_screen(self,k):
        self.manager.current=k

