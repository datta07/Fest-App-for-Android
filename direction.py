from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mapview import MapView, MapMarker
 
 
class Venue(Screen):
 
    Builder.load_string('''
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDRaisedButton kivymd.button.MDRaisedButton
<Venue>
    name: 'dir'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(13)
        Toolbar:
            id: toolbar
            title: 'Directions'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 10
            left_action_items: [['arrow-left', lambda x: app.back('vute')]]
        BoxLayout
            orientation: 'vertical'
            AsyncImage:
                id: img_venue
                source: 'clg.jpeg'
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                lat: 18.665352
                lon: 78.9095754
                MapMarker
                    lat: 18.665352
                    lon: 78.9095754
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            MDRaisedButton:
                text: 'Get Directions'
                size_hint:[1,None]
                on_release:
                    import webbrowser
                    webbrowser.open("https://www.google.com/maps/dir//Academic+Block+1,+Telangana+505501/@18.665352,78.9095754,16z/data=!4m7!4m6!1m1!4e2!1m2!1m1!1s0x3bcd1a0b77652ac7:0xf8c665a2673afa4f!3e0") 
''')
 