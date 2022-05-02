from tkinter import Toplevel
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from time import *



class WindowChat(Toplevel):


    def __init__(self):
        super(WindowChat, self).__init__()
        #setting window size
        self.geometry('%dx%d+500+250'%(795,505))

        #unable to change size
        self.resizable(False,False)

        self.add_widget()

        self.set_title('personA')

        # self.on_send_click(lambda : self.append_message('personA','hello'))

        #add componment
    def add_widget(self):
        #chart area
        chat_text_area = ScrolledText(self)
        chat_text_area['width'] = 110
        chat_text_area['height'] = 31
        chat_text_area.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

        chat_text_area.tag_config('green',foreground="#008B00")
        chat_text_area.tag_config('system',foreground="red")

        self.children['chat_text_area'] = chat_text_area


        #input area
        chat_input_area = Text(self, name='chat_input_area')
        chat_input_area['width'] = 100
        chat_input_area['height'] = 5
        chat_input_area.grid(row=1,column=0,pady=3)

        #send button
        send_button = Button(self,name='send_button')
        send_button['text'] = 'send'
        send_button['width'] = 5
        send_button['height'] = 2
        send_button.grid(row=1,column=1)

    def set_title(self,title):
        self.title('%s Enter Chat Room' %title)

    def on_send_click(self,command):
        #send button click event
        self.children['send_button']['command'] = command


    def get_inputs(self):
        #get user input
        return self.children['chat_input_area'].get(0.0,END)


    def clear_input(self):
        #clear input textbox
        self.children['chat_input_area'].delete(0.0,END)


    def append_message(self,sender,message):
        #add message in chat area
        send_time = strftime('%d-%m-%y %H:%M:%S',localtime(time()))
        send_info = '%s :  %s  \n' %(sender,send_time)
        self.children['chat_text_area'].insert(END, send_info, 'green')
        self.children['chat_text_area'].insert(END, '' + message + '\n')

        #roll down screen
        self.children['chat_text_area'].yview_scroll(3,UNITS)

    def on_window_close(self,command):
        self.protocol("WM_DELETE_WINDOW", command)

# if __name__ == '__main__':
#     WindowChat().mainloop()
