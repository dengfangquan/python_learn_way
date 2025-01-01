from tkinter import *
class Win(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("140x240")
        self.button_distinct()
        self.resizable(False,False)
        self.mainloop()

    def button_distinct(self):
        i = 1
        self.t = StringVar()
        self.entry = Entry(self,textvariable = self.t,width = 12,font= ("Arial",15))

        for row in range(3):
            for column in range(3):
                button = Button(self,text = i,font = ('Arial',13),width = 4,height = 2,command = lambda x=i:(self.entry.insert('end',int(x))))
                button.place(x =column *46,y =row *46)
                i+=1
        char_lsit = ['+','-','*','/']
        char_position_x , char_position_y= 0,145
        for char_num in char_lsit:
            button_char = Button(self,text = char_num,font = ('Arial',13),width = 3,height = 1,command = lambda x=char_num:self.entry.insert('end',x))
            button_char.place(x=char_position_x*33,y=char_position_y)
            char_position_x+=1
        resualt_get = Button(self, text="=", width = 6 ,command=lambda : self.set_value(self.entry.get()))
        self.entry.place(y=180)
        clear = Button(self,text = "C",command = self.clearing,width = 6)
        resualt_get.place(x=5,y=210)
        clear.place(x=80,y=210)
    def set_value(self, value):
        a=eval(value)
        self.t.set(a)
    def clearing(self):
        self.t.set('')
w=Win()