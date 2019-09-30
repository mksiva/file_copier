from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory
import shutil, errno, os
from shutil import ignore_patterns
root = Tk(  )
    
def copyanything():
    srcPath = PathTextBox.get('1.0','end-1c')
    destPathRoot = PathTextBoxDest.get('1.0','end-1c')
    srcDirName = os.path.basename(os.path.normpath(srcPath))
    destPath = destPathRoot + "/" + srcDirName
    try:
	    shutil.rmtree(destPath)
    except (OSError, WindowsError, IOError, os.error) as exc: # python >2.5
            ResultTextBox.delete('1.0',END)
            ResultTextBox.insert(END,str(exc))
            pass
			
    try:
        shutil.copytree(srcPath, destPath, ignore=ignore_patterns('*.git', 'log', '.git', '.gradle', '.idea','.settings','.classpath','app.*','target','.project','.gitignore','README.*'))
        ResultTextBox.delete('1.0',END)
        ResultTextBox.insert(END,"Files are copied to : " + destPath)
    except (OSError, WindowsError, IOError, os.error) as exc: # python >2.5
            ResultTextBox.delete('1.0',END)
            ResultTextBox.insert(END,str(exc))    

def SelectSrcDir():
    options = {}
    options['initialdir'] = os.getcwd()
    options['title'] = "Choose a src directory."
    options['mustexist'] = False
		
    name = askdirectory(**options) 
    PathTextBox.delete("1.0",END)
    PathTextBox.insert(END,name)

def SelectDestDir():
    name = askdirectory(initialdir="/",
                           title = "Choose a destination directory."
                           ) 
    PathTextBoxDest.delete("1.0",END)
    PathTextBoxDest.insert(END,name)
	
Title = root.title( "Files Copier!")
path = StringVar()

HeadLabel1 = Label(root,text="Files ")
HeadLabel1.grid(row = 1,column = 1,sticky=(E))
HeadLabel2 = Label(root,text=" Copier")
HeadLabel2.grid(row = 1,column = 2,sticky=(W))

InputLabel = Label(root,text = "FROM:")
InputLabel.grid(row=2,column = 1)

BrowseButton = Button(root,text="Browse",command = SelectSrcDir)
BrowseButton.grid(row=2,column=2)

PathLabel = Label(root,text = "Source:")
PathLabel.grid(row = 3,column=1,sticky=(W))

PathTextBox = Text(root,height = 2)
PathTextBox.grid(row = 4,column = 1,columnspan=2)


InputLabelDest = Label(root,text = "TO:")
InputLabelDest.grid(row=5,column = 1)

BrowseButtonDest = Button(root,text="Browse",command = SelectDestDir)
BrowseButtonDest.grid(row=5,column=2)

PathLabelDest = Label(root,text = "Destination:")
PathLabelDest.grid(row = 6,column=1,sticky=(W))

PathTextBoxDest = Text(root,height = 2)
PathTextBoxDest.grid(row = 7,column = 1,columnspan=2)


ReadButton = Button(root,text="COPY DIR",command = copyanything)
ReadButton.grid(row = 8,column = 2)

ResultTextBox = Text(root,height = 4)
ResultTextBox.grid(row = 9,column = 1,columnspan=2)

root.mainloop()
