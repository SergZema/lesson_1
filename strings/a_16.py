import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(40, 40, 200, 150)
canvas.create_rectangle(10, 10, 260, 180)
window.mainloop()
