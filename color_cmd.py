."""
Colors text in console mode application (win32).
Uses ctypes and Win32 methods SetConsoleTextAttribute and
GetConsoleScreenBufferInfo.

$Id: color_console.py 534 2009-05-10 04:00:59Z andre $

$devlop: Alaa Prog $
"""

import ctypes,sys  


SHORT = ctypes.c_short
WORD = ctypes.c_ushort


class COORD(ctypes.Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("X", SHORT),
    ("Y", SHORT)]

class SMALL_RECT(ctypes.Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("Left", SHORT),
    ("Top", SHORT),
    ("Right", SHORT),
    ("Bottom", SHORT)]

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("dwSize",COORD),
    ("dwCursorPosition", COORD),
    ("wAttributes", WORD),
    ("srWindow", SMALL_RECT),
    ("dwMaximumWindowSize", COORD)
    ]


BLACK     = 0
BLUE      = 1
GREEN     = 2
CYAN      = 3
RED       = 4
MAGENTA   = 5
YELLOW    = 6
GREY      = 7
INTENSITY = 8


B_BLACK     = 0
B_BLUE      = 16
B_GREEN     = 32
B_CYAN      = 48
B_RED       = 64
B_MAGENTA   = 80
B_YELLOW    = 96
B_GREY      = 112
B_INTENSITY = 128 

stdout_handle = ctypes.windll.kernel32.GetStdHandle(-11)
SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute
GetConsoleScreenBufferInfo = ctypes.windll.kernel32.GetConsoleScreenBufferInfo



def endColor():
  csbi = CONSOLE_SCREEN_BUFFER_INFO()
  GetConsoleScreenBufferInfo(stdout_handle, ctypes.byref(csbi))
  return csbi.wAttributes
endCs = endColor()

def startC(color):
  endCs = endColor()
  SetConsoleTextAttribute(stdout_handle, color);sys.stdout.flush()
def endC():
  SetConsoleTextAttribute(stdout_handle, endCs)

def puts(text,colors):
  endCs = endColor()
  SetConsoleTextAttribute(stdout_handle, colors);print(text) 
  SetConsoleTextAttribute(stdout_handle,endCs);sys.stdout.flush()

def Pmsg(text,colors1,colors2=endCs):
  endCs = endColor()
  # [ done ] : , ^_^ help u;
  text = text.split(",");
  SetConsoleTextAttribute(stdout_handle, colors1);print(text[0],end="");sys.stdout.flush()
  SetConsoleTextAttribute(stdout_handle, colors2);print(text[1])
  SetConsoleTextAttribute(stdout_handle,endCs);sys.stdout.flush()

def gets(text,colorT,colorIn=endCs):
  endCs = endColor()
  SetConsoleTextAttribute(stdout_handle, colorT);
  print(text,end=" ");sys.stdout.flush()
  SetConsoleTextAttribute(stdout_handle,colorIn);text = input();
  SetConsoleTextAttribute(stdout_handle,endCs);sys.stdout.flush()
  return text

