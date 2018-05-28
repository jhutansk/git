import os
import tkinter

def run():
    #textboxOutput.configure(state='normal')
    #textboxOutput.delete('1.0', END)
    #textboxOutput.update()
    #textboxOutput.configure(state='disabled')


    WindowsURI = entWindowsURI.get()
    textToreplace = WindowsURI
    for ch in ['\\']:
        if ch in textToreplace:
            textToreplace = textToreplace.replace('\\', '/')
    for ch in [' ']:
         if ch in textToreplace:
             textToreplace = textToreplace.replace(' ', '%20')

    textboxOutput.configure(state='normal')
    textboxOutput.insert("end", "[file:///" + str(textToreplace)+"]")
    textboxOutput.configure(state='disabled')


window = tkinter.Tk()
window.title("External URI Generator")
window.geometry("600x130")
window.resizable(False, False)
lblWINURI = tkinter.Label(window, text="Windows URI")
lblRTCURI = tkinter.Label(window, text="RTC External URI")
lblWINURI.pack()
lblWINURI.place(x=5, y=5)
lblRTCURI.pack()
lblRTCURI.place(x=5, y=38)
entWindowsURI = tkinter.Entry()
entWindowsURI.pack()
entWindowsURI.place(x=120, y=5, width=404)
textboxOutput = tkinter.Text(window, width = 50, height = 5, state=tkinter.DISABLED)
textboxOutput.pack()
textboxOutput.place(x=120, y=38)
btnRun = tkinter.Button(window, text="Generate", height = 3, width = 8 ,command=run)
btnRun.pack()
btnRun.place(x=530, y=3)

window.mainloop()
