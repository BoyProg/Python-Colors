import color
print (dir(color))

###########################################################
# IF -> Windows #
# colors and background-colors
color.startC(color.RED)
print("Alaa Prog ")
print("This Test ^_^")
print ()
color.endC()
# or 
color.startC(2)
print("Python 3||2 !!")
print("^_^ !!")
print()
color.endC()

# Background_GREEN # like -> print with -> "color"
color.puts("Hello World",color.BLUE|color.B_GREEN)
print()

# input With Color
name = color.gets("Enter Your Name: ",color.BLUE,color.CYAN)
color.puts("Your Name is -> %s"%name,color.CYAN)
# 1- color.BLUE : print "Enter ....  "
# 2- color.CYAN : input User

# print Msg like : [ Error ] : , Some Msg !!
color.Pmsg("[ Error ] : , Some Msg !!",color.RED,color.YELLOW)
# split(",") -> list[2]
# color.RED    : print  [ Error ] : 
# color.YELLOW : print  Some Msg !!

#######################################################
#	IF -> Linux #

# Style and background-colors and colors
# like 

# u = under line 
# color.Put_Tc("Hello World",color=color.d_green,background="",style=color.u)
# and 
# ( color.Re_Tc ) like Put_Tc but " return Not Print "
# in_color = input color
# Input_Tc("msf>",color=color.l_green,in_color=color.l_blue,style=color.u)
# and 
# color.start(color.d_blue,background=color.bd_green,style=color.pl) 
# print ("asdfasdfasdfa0")
# print ("asdfasdfasdfa0")
# color.end()
# color.P_Msg("[ Error ] : , Some Msg !!",color.l_red,color.l_blue)
# color.R_Msg
