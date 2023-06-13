import tkinter as tk
from tkinter import ttk
from gpiozero import LED



class Window(tk.Tk):
    def __init__(self,redled):
        super().__init__()
        self.redled = redled
        self.title('hello')
        self.resizable(False, False)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Title.TLabel',foreground='red',background='black',font=('Arial',20))
        s.configure('Led.TButton',
                    foreground='red',
                    background='yellow',
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20)
                    )
        s.configure('Led.TButton',
                    background='yellow',
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20),
                    )
        #print(s.layout('TButton'))
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabel')        
        title_label.pack(pady=25,padx=100)

        self.led_btn = ttk.Button(self,text="LED on",style='Led.TButton',command=self.user_click)   
             
        self.led_btn.pack(pady=(10,50))

    def user_click(self):
        self.state = not self.state
        if self.state:
            self.led_btn.config(text='LED off')
            self.led_btn.config(style='LEDOpen.TButton')
            led.on()
        else:
            self.led_btn.config(text='LED on')
            self.led_btn.config(style='LEDClose.TButton')
            led.off()   


if __name__ == "__main__":
    led = LED(23)
    led.off()
    window = Window(led)   
    window.mainloop()
   