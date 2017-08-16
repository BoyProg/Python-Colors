# Colors text in shell.py (linux). 
# by Programmer BOy ; 

import sys

endC = 0
C_color = "\033[%sm"

# COLOR >
COLORS = list(range(30,39)) + list(range(90,99))

# 	Dark Color :

d_black    = 30
d_red      = 31
d_green    = 32
d_yellow   = 33
d_blue     = 34
d_magenta  = 35
d_cyan     = 36
d_white    = 37

# 	light Color :

l_black    = 90
l_red      = 91
l_green    = 92
l_yellow   = 93
l_blue     = 94
l_magenta  = 95
l_cyan     = 96
l_white    = 97


## background -+>

# background Dark Color :
BACKGROUND_COLOR = list(range(40,49)) + list(range(100,109))

bd_red      = 41
bd_green    = 42 
bd_yellow   = 43
bd_blue     = 44
bd_magenta  = 45
bd_cyan     = 46
bd_white    = 47

# background light Color :

bl_red      = 91
bl_green    = 92 
bl_yellow   = 93
bl_blue     = 94
bl_magenta  = 95
bl_cyan     = 96
bl_white    = 97

# Style >

b   = 1
d_l = 2
u   = 4
u_b = 7
pl  = 9





# Print  Text With Color + bacground + Style 
# ----------------------------------------------{
def Put_Tc(text,color='',background='',style=''):
	if color in COLORS:
		color = "\033[%sm"%color
	else:
		color = ''

	if background in BACKGROUND_COLOR:
		background = "\033[%sm"%background
	else:
		background = ''
	if style in [1,2,4,7,8]:
		style = C_color%style
	else:
		style = ""
	sys.stdout.write(color+background+style+text+endC+"\n");

# Return Text With Color + bacground + Style 
def Re_Tc(text,color='',background='',style=''):
	if color in COLORS:
		color = "\033[%sm"%color
	else:
		color = ''

	if background in BACKGROUND_COLOR:
		background = "\033[%sm"%background
	else:
		background = ''

	if style in [1,2,4,7,8]:
		style = C_color%style
	else:
		style = ""

	return str(color+background+style+text+endC);
# }----------------------------------------------


# Color With ( Input ) Text  
# ---------------------------------------------{
def Input_Tc(text,color="",in_color='',style=''):
	if color in COLORS:
		color = "\033[%sm"%color
	else:
		color = ''

	if in_color in COLORS:
		in_color = "\033[%sm"%in_color
	else:
		in_color = ''

	if style in [1,2,4,7,8]:
		style = C_color%style
	else:
		style = ""

	input_text = color+style+text+in_color;
	get_input = raw_input(input_text);
	return str(get_input)
# }--------------------------------------------- 

# Print  Msg With Color like  {{ [ ok ]:, This Is Test }}
# ------------------------------{
def P_Msg(text,color_a,color_b):
	text = text.split(",")
	MSG = "\033[%sm"%color_a+text[0]+"\033[%sm"%color_b+text[1]
	sys.stdout.write(MSG+'\n'+endC)

def R_Msg(text,color_a,color_b):
	text = text.split(",")
	MSG = "\033[%sm"%color_a+text[0]+"\033[%sm"%color_b+text[1]
	return (MSG+'\n'+endC)	
# }-----------------------------

# color for all print From start_Pc  To end_Pc
#-----------------------------------------{

def start(color,background='',style=''):
	if color in COLORS:
		color = "\033[%sm"%color
	else:
		color = ''

	if background in BACKGROUND_COLOR:
		background = "\033[%sm"%background
	else:
		background = ''

	if style in [1,2,4,7,8]:
		style = C_color%style
	else:
		style = ""
	sys.stdout.write(color+background+style);



def end():
	sys.stdout.write(C_color%endC);

# }----------------------------------------#
