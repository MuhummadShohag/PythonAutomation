#=============== Display given string at left\right\center\ of a line title format===========================

import os

t_w=os.get_terminal_size().columns # it is showed terminal size

given_string=input("Enter your String: ")
print(given_string)

#  knowing Number of Column :mod
print(f"{given_string.center(t_w).title()}") # it is showed center with Title format
print(given_string.ljust(t_w).title()) # it is showed left with Title format
print(given_string.rjust(t_w).title()) # it is showed right with Title format