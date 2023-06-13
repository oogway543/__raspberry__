import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('hello')
        self.resizable(False, False)
        s = ttk.Style()
        s.configure('Title.TLabl',foreground='red', background='black',font=('Arial',20))
        s.configure('Title.TButton',foreground='red', background='black',font=('Arial',20))
        s.theme_use('clam')        
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabl')
        print(title_label.winfo_class())
        title_label.pack(pady=25,padx=100)

        led_btn = ttk.Button(self,text="LED 開")
        led_btn.pack(pady=(10,50))

if __name__ == "__main__":
    window = Window()   
    window.mainloop()