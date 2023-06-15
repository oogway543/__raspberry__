import tkinter as tk
from tkinter import ttk
from gpiozero import LED
import datasource

class LEDButton(ttk.Button):
    def __init__(self,master,led,**kwargs):
        super().__init__(master,**kwargs)
        self.led = led
        self.state = False
        self.config(command=self.user_click)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('LedClose.TButton',
                    foreground='red',
                    background='yellow',
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20)
                    )
        s.configure('LedOpen.TButton',
                    background='yellow',
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20),
                    )



    def user_click(self):
        self.state = not self.state
        if self.state:
            self.config(text='LED off')
            self.config(style='LEDOpen.TButton')
            self.led.on()
        else:
            self.config(text='LED on')
            self.config(style='LEDClose.TButton')
            self.led.off()

class Window(tk.Tk):
    def __init__(self,redLed,**kwargs):

        super().__init__(**kwargs)

        self.title('hello')
        self.resizable(False, False)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Title.TLabel',font=('Arial',20))
        
        #print(s.layout('TButton'))
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabel')        
        title_label.pack(pady=25,padx=100)
 
        self.led_btn = LEDButton(self,led=redLed,text="LED on",style='LedClose.TButton')  
        self.led_btn.pack(pady=(10,50))

       


if __name__ == "__main__":
    conn = datasource.create_connection('iot.db')
    datasource.create_table(conn)
    datasource.insert_data(conn,1)
    led = LED(23)
    led.off()
    window = Window(led)   
    window.mainloop()
   