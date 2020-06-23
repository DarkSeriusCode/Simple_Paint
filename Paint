'''
FAQ:
How draw?
It`s easy! Just press LeftMouseButton or F3 and enjoy ^_^.

If I want to change a size?
You can select a size, just enter a number in the input line and press Enter!

I want to change the color, what do I do?
Just enter the color code (hex code or name of color) in the input lineand press Enter!

If you want to delete your drawing, click on the button "clear"

FullscreenOn - F11
FullsecreenOff - F12

I hope you like my programm! Enjoy :)

About author:

Hi I`am Dark Serius. I from Russia. I`m sorry if there are any mistakes. My English is very bad!
Programming language: Python 3
'''
import tkinter, sys, colorama
import threading, time, os
from colorama import Fore as F
from tkinter import *
colorama.init()

color = ['black']
position = [10]

banner = '''
=====================
    Simple Paint
=====================
By Dark Serius.
'''

#GetCursorPosition
def GetCursorPosition():
	x = root.winfo_pointerx() - root.winfo_rootx()  
	y = root.winfo_pointery() - root.winfo_rooty()
	return x, y

#Create functions
def Manual ():
	Manual = Tk()
	Manual.title('Manual')
	Manual.resizable(False, False)
	l1 = Label(Manual, text = __doc__).pack()
	Manual.mainloop()


def AppendToPosition (size):
	Enter_pos_x.delete(0, END)
	position.clear()
	position.append(int(size) / 2)

def Speener (name, raund, speed, znaks):
	x = 0
	while x != raund:
		for i in znaks:
			time.sleep(speed)
			print('{0}: {1}'.format(name, i), end = '\r')
		x +=1

def Draw (canvas, User_color, main):# Function for draw on the Canvas
	canvas.focus_set()
	if main == 1:
        #Get cursor position
		x, y = GetCursorPosition()

		#Create object
		pos = position[0]
		try:
			canvas.create_rectangle(x + pos, y + pos, x - pos, y - pos, fill = color[0], outline = color[0])
		except:
			os.system('cls')
			print(F.RED + '\t     Error: Color is not correct! %s not find!' % (color[0]), end = '\r')	

	else:
	    Selecr_color.delete(0, END)
	    color.clear()
	    color.append(User_color)

print(F.GREEN + banner)

WidthW = int(input('Enter Canvas width: '))
HeightW = int(input('Enter Canvas height: '))

#Root window
root = Tk()

#Setting window
W = WidthW
H = HeightW

if W >= root.winfo_screenwidth() - 150:
	print('Sorry. The width is very big!')
	sys.exit()

if H >= root.winfo_screenheight():
	print('Sorry. The height is very big!')
	sys.exit()

#start Speener()
ProgressBar = threading.Thread(target = Speener, args = (F.BLUE + 'Enjoy ^_^', float('inf'), 0.08, 
															['|', '/', '-', '\\', '|', '/', '-', '\\']))
ProgressBar.start()

root.title('Simple Paint')
root.geometry(f'{W + 140}x{H}+{0}+{0}')

#Create Canvas
art = Canvas(root, width = W, height = H, bg = 'white')
art.focus_set()
art.place(x = 0, y = 0)

#Create Frame for size
x_frame = LabelFrame(root, text = 'Size')

#Entry size
Enter_pos_x = Entry(x_frame, width = 700)
Enter_pos_x.bind('<Return>', lambda event: AppendToPosition(Enter_pos_x.get()))
Enter_pos_x.pack()

x_frame.place(x = W + 10, y = 0)

#Select color
SC = LabelFrame(root, text = 'Select color')
Selecr_color = Entry(SC, width = 400)
Selecr_color.bind('<Return>', lambda event: Draw(art, Selecr_color.get(), 0))
Selecr_color.pack()

SC.place(x = W + 10, y = 40)

#Delete
Del = Button(root, text = 'Clear', font = '30', command = lambda: art.delete('all')).place(x = W + 5, y = 80)

#Manual
Start_manual = Button(root, text = 'Click on me!', command = Manual).place(x = W + 60, y = 80)

#Bind a buttons
art.bind('<F11>', lambda event: root.attributes('-fullscreen', True))
art.bind('<F12>', lambda event: root.attributes('-fullscreen', False))

art.bind('<F3>', lambda event: Draw(art, color[0], 1))
art.bind('<Button-1>', lambda event: Draw(art, color[0], 1))

root.mainloop()
