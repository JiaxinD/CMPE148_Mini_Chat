from tkinter import Tk
from tkinter import Label
from tkinter import *

class WindowLogin(Tk):
    #login interface


    def __init__(self):
        #initial window
        super(WindowLogin, self).__init__()

        # window attribute
        self.window_init()


        #component
        self.add_widgets()

        # self.on_reset_click(lambda :self.clear_password())


    def window_init(self):
        #initial

        #window tittle
        self.title('User Login')

        window_width = 285
        window_height = 105


        #unable to stretch window
        self.resizable(False,False)
        #get screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width - window_width)/2
        position_y =  (screen_height-window_height)/2

        # size and position
        #width x height + x + y
        self.geometry('%dx%d+%d+%d' %(window_width,window_height,position_x,position_y))

    def add_widgets(self):
        #add component



        #username label


        username_label = Label(self)
        username_label['text'] = 'Username:'
        username_label.grid(row=0,column=0,padx=10,pady=5)

        username_entry = Entry(self,name='username_entry')
        username_entry['width'] = 25
        username_entry.grid(row=0,column=1)






        # password label

        password_label = Label(self)
        password_label['text'] = 'Password:'
        password_label.grid(row=1,column=0,padx=10,pady=5)

        password_entry = Entry(self,name='password_entry')
        password_entry['width'] = 25
        password_entry.grid(row=1,column=1)
        password_entry['show'] = '*'


        #Button
        button_frame = Frame(self,name='button_frame')

        #reset
        reset_button = Button(button_frame,name='reset_button')
        reset_button['text'] = ' Reset '
        reset_button.pack(side=LEFT,padx=15)




        #login

        login_button = Button(button_frame, name='login_button')
        login_button['text'] = ' Login '
        login_button.pack(side=LEFT)

        button_frame.grid(row=2,columnspan=2,pady=2)


        login_button['command'] = lambda :print("")


    def get_username(self):
        #get username from textbox
        return self.children['username_entry'].get()

    def get_password(self):
        #get password
        return self.children['password_entry'].get()


    def clear_username(self):
        #clear username
        self.children['username_entry'].delete(0,END)

    def clear_password(self):
        # clear username
        self.children['password_entry'].delete(0, END)

    def on_reset_click(self,command):
        reset_button = self.children['button_frame'].children['reset_button']
        reset_button['command'] = command

    def on_login_click(self,command):
        #login button click event response
        login_button = self.children['button_frame'].children['login_button']
        login_button['command'] = command


    def on_window_closed(self,command):
        #close window event
        self.protocol('WM_DELETE_WINDOW',command)

# if __name__ == '__main__':
#     window = WindowLogin()
#     window.mainloop()