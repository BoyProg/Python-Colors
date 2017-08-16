from sys import platform
# Chacked System !!
if platform == "win32":
	from color_cmd import *
elif platform == "linux":
	from color_shell import *
