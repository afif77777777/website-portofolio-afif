import tkinter as tk 
root = tk.Tk() 
labell1 = tk.Label(root, text="Label 1") 
labell2 = tk.Label(root, text="Label 2") 
labell3 = tk.Label(root, text="Label 3") 

labell1.grid(row=0, column=0) 
labell2.grid(row=0, column=1) 
labell3.grid(row=1, column=0, columnspan=2) 
root.mainloop()  