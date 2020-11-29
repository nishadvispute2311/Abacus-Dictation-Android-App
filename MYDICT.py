from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivymd.toast import toast
from plyer import battery,tts,vibrator
import time
import random


Window.keyboard_anim_args={'d':0.2,'t':'in_out_expo'}
Window.softinput_mode="below_target"

screen_helper="""
ScreenManager:
	FirstScreen:
	DataScreen:
	SpeaksScreen:

<FirstScreen>:
	name:'first'
	Image:
		source:'ucmas.jpg'
		pos_hint:{'center_x':0.5,'center_y':0.6}
		size_hint:None,None
		width:1000
		height:1000
	MDRoundFlatButton:
		text:"Let's Go !!"
		pos_hint:{'center_x':0.5,'center_y':0.20}
		on_press:
			root.manager.current='data'
			root.manager.transition.direction="left"
	MDFloatingActionButton:
		icon:'moon-first-quarter'
		pos_hint:{'center_x':0.9,'center_y':0.950}
		on_release:app.theme_changer()

<DataScreen>:
	name:'data'     	  
	MDTextField:
		id:my_digit
		hint_text:'Digits You Want'
		input_filter: 'int'
		icon_right:"numeric"
		icon_right_color:app.theme_cls.primary_color
		pos_hint:{'center_x':0.5,'center_y':0.6}
		size_hint:None,None
		width:700
	MDTextField:
		id:my_row
		hint_text:'Rows You Want'
		input_filter: 'int'
		icon_right:"numeric-10"
		icon_right_color:app.theme_cls.primary_color
		pos_hint:{'center_x':0.5,'center_y':0.5}
		size_hint:None,None
		width:700
	MDTextField:
		id:my_sum
		hint_text:'Sums You Want'
		input_filter: 'int'
		icon_right:"crosshairs-question"
		icon_right_color:app.theme_cls.primary_color
		pos_hint:{'center_x':0.5,'center_y':0.4}
		size_hint:None,None
		width:700
	MDTextField:
		id:my_gap
		hint_text:'Gap You want'
		input_filter: 'float'
		icon_right:"clock-outline"
		icon_right_color:app.theme_cls.primary_color
		pos_hint:{'center_x':0.5,'center_y':0.3}
		size_hint:None,None
		width:700
	MDRoundFlatButton:
		text:'Start'
		pos_hint:{'center_x':0.5,'center_y':0.2}
		on_press:
			root.manager.current="speaks"
			root.manager.transition.direction="left"
			on_release:app.my_dict(my_digit.text,my_row.text,my_sum.text,my_gap.text)
	MDRoundFlatButton:
		text:'Back'
		pos_hint:{'center_x':0.5,'center_y':0.1}
		on_press:
			root.manager.current='first'	
			root.manager.transition.direction="right"
							 
			
			

<SpeaksScreen>:
	name:'speaks'
	MDLabel:
		text:'Hiiii Welcome Dear Abacus Student . I hope you are ennoying the Dictation Session'
		halign:'center'
	MDRoundFlatButton:
		text:'Back'
		pos_hint:{'center_x':0.5,'center_y':0.3}
		on_press:
			root.manager.current='data'	
			root.manager.transition.direction="right"	
"""
class FirstScreen(Screen):
	pass
class DataScreen(Screen):
	pass
class SpeaksScreen(Screen):
	pass

#Creating ScreenManager
sm=ScreenManager()
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(DataScreen(name='data'))
sm.add_widget(SpeaksScreen(name='speaks'))

class DemoApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Green"
		self.theme_cls.theme_style="Light"
		screen=Builder.load_string(screen_helper)
		return screen
	
	def theme_changer(self):
		if self.theme_cls.theme_style=="Light":
			self.theme_cls.theme_style="Dark"
		else:
			self.theme_cls.theme_style="Light"
	
	def speak(self,item):
		tts.speak(item)
	
	def my_reset(self,my_digit,my_row,my_sum,my_gap):
		my_digit=""
		my_row=""
		my_sum=""
		my_gap=""
	
	def my_dict(self,my_digit,my_row,my_sum,my_gap):
		#toast(f"this is {my_digit},{my_row},{my_sum},{my_gap}")
		#self.speak("Welcome To My Dictation")
		#time.sleep(1)
		#self.speak("Are you ready . Lets start in....")
		#for i in range(3,0,-1):
			#self.speak(str(i))
			#time.sleep(1.5)
		
		if my_digit !="" and my_row !="" and my_sum !="" and my_gap !="":
			if my_digit=="2":
				self.speak(f"Welcome To The {my_digit} digit Dictation")
				time.sleep(1)
				self.speak("Are you ready . Lets start in....")
				dictation=[]
				result=[]
				for i in range (1,int(my_sum)+1):
				#time.sleep(3)
					for i in range (1,int(my_row)+1):
						value=random.randint(10,99)
						dictation.append(value)
					for i in range (1,int(my_row)//3+1):
						place_to_replace=random.randint(1,int(my_row)-1)
						value_to_replace=random.randint(10,99)
						dictation[place_to_replace]=(value_to_replace*(-1))
					for i in dictation:
						self.speak(str(i))
						time.sleep(float(my_gap))
					results=sum(dictation)
					result.append(results)
					dictation.clear()
					self.speak("That is")
					time.sleep(9)
				time.sleep(8)
				self.speak("Now lets see the answers")
				for i in result:
					time.sleep(2)
					self.speak(str(i))
				
				time.sleep(3)
				self.speak("if You Got All correct ...Congrats...Keep it up")
			
			if my_digit=="1":
				self.speak(f"Welcome To The {my_digit} digit Dictation")
				time.sleep(1)
				self.speak("Are you ready . Lets start in....")
				#toast(f"{my_digit}")
				dictation=[]
				result=[]
				for i in range (1,int(my_sum)+1):
					#time.sleep(3)
					for i in range (1,int(my_row)+1):
						value=random.randint(1,9)
						dictation.append(value)
					for i in range (1,int(my_row)//3+1):
						place_to_replace=random.randint(1,int(my_row)-1)
						value_to_replace=random.randint(1,9)
						dictation[place_to_replace]=(value_to_replace*(-1))
					for i in dictation:
						self.speak(str(i))
						time.sleep(float(my_gap))
					results=sum(dictation)
					result.append(results)
					dictation.clear()
					self.speak("That is")
					time.sleep(6)
				time.sleep(6)
				self.speak("Now lets see the answers")
				for i in result:
					time.sleep(2)
					self.speak(str(i))
				
				time.sleep(3)
				self.speak("if You Got All correct ...Congrats...Keep it up")	
			
			if my_digit=="3":
				self.speak(f"Welcome To The {my_digit} digit Dictation")
				time.sleep(1)
				self.speak("Are you ready . Lets start in....")
				#toast(f"{my_digit}")
				dictation=[]
				result=[]
				for i in range (1,int(my_sum)+1):
				#time.sleep(3)
					for i in range (1,int(my_row)+1):
						value=random.randint(100,999)
						dictation.append(value)
					for i in range (1,int(my_row)//3+1):
						place_to_replace=random.randint(1,int(my_row)-1)
						value_to_replace=random.randint(10,99)
						dictation[place_to_replace]=(value_to_replace*(-1))
					for i in dictation:
						self.speak(str(i))
						time.sleep(float(my_gap))
					results=sum(dictation)
					result.append(results)
					dictation.clear()
					self.speak("That is")
					time.sleep(9)
				time.sleep(9)
				self.speak("Now lets see the answers")
				for i in result:
					time.sleep(2)
					self.speak(str(i))
				
				time.sleep(3)
				self.speak("if You Got All correct ...Congrats...Keep it up")
			
			if my_digit=="12":
				self.speak("Welcome To The 1 and 2 digit combine Dictation")
				time.sleep(1)
				self.speak("Are you ready . Lets start in....")
				#toast(f"{my_digit}")
				dictation=[]
				result=[]
				for i in range (1,int(my_sum)+1):
					#time.sleep(3)
					for i in range (1,int(my_row)+1):
						value=random.randint(1,99)
						dictation.append(value)
					for i in range (1,int(my_row)//3+1):
						place_to_replace=random.randint(1,int(my_row)-1)
						value_to_replace=random.randint(1,9)
						dictation[place_to_replace]=(value_to_replace*(-1))
					for i in dictation:
						self.speak(str(i))
						time.sleep(float(my_gap))
					results=sum(dictation)
					result.append(results)
					dictation.clear()
					self.speak("That is")
					time.sleep(9)
				time.sleep(8)
				self.speak("Now lets see the answers")
				for i in result:
					time.sleep(2)
					self.speak(str(i))
				
				time.sleep(3)
				self.speak("if You Got All correct ...Congrats...Keep it up")
			if (int(my_digit) >3 and int(my_digit) <12) or int(my_digit) > 12:
				toast("Sorry ! The dictation is Available only for 1,2,3 and for 1 and 2 digits")
		
		else:
			toast("Please enter all the terms .....!!!")	
			
				
			
			
			
			
		
			
					
			
			
			
		


if __name__=='__main__' :
	DemoApp().run()


