import subprocess 
import os
import tkinter
from tkinter import Button, Tk, messagebox


def gitCallBack():
    os.chdir('pathtodir')
    git_command = ['/usr/bin/git', 'add','-u']
    subprocess.run(git_command) 
    git_command = ['/usr/bin/git', 'add','.']
    subprocess.run(git_command)  
    git_command = ['/usr/bin/git', 'commit', '-m', '--allow-empty-message']
    subprocess.run(git_command) 
    msg = messagebox.showinfo( "Saving Preccess", "Done!")
    top.destroy()

top = Tk()
B = Button(top, text = "Save", command = gitCallBack )
B.place(x = 50,y = 50)
top.mainloop()



