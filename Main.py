import tkinter as tk
import Students as sd
from auth import main

#making main Window

mainWindow = tk.Tk()
mainWindow.configure(bg='#132c33')
mainWindow.title('ACME Assessment Database System ')
mainWindow.attributes('-alpha',0.2)
#authentication Setup
main(mainWindow)



mainWindow.mainloop()
