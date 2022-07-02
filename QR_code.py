from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import png
import os
import pyqrcode
from tkinter import Toplevel
root=Tk()
root.geometry('570x400')
root.config(bg='pink')
root.title("QR Code")
root.wm_iconbitmap('Iconsmind-Outline-QR-Code.ico')
# functions
def quit_root():
    res=messagebox.askyesnocancel('Notification',"Are you sure you want to quit?")
    if(res==True):
        root.destroy()
    else:
        pass

def clear():
    qr_id_entrybox.delete(0,END)
    qr_message_entrybox.delete(0,END)
    qr_name_entrybox.delete(0,END)
    qr_notification_message_label.configure(text='')

def generate():
    qr_name=qr_name_entrybox.get()
    qr_id=qr_id_entrybox.get()
    qr_message=qr_message_entrybox.get()
    message_qr='Name: '+qr_name+'\n'+'id: '+qr_id+'\n'+'massage: '+qr_message
    url=pyqrcode.create(message_qr)
    pp=r'G:\python\projects\QR Code\New folder'
    cc=f'{pp}\{qr_id}{qr_name}.png'
    ll=os.listdir(pp)
    if 'f{qr_id}{qr_name}' in ll:
        messagebox.showinfo('Notification','Please Change Id')
    else:
        url.png(cc,scale=8)
        mm=f'QR Code saved as {qr_id}{qr_name}.png'
        qr_notification_message_label.configure(text='mm')
        res=messagebox.askyesno('Notification','QR Code is generated and want to see it than yes')
        if res:
            top=Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img=PhotoImage(file=cc)
            label1=Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()


    # url.png('hh.png',scale=8,background=(0,255,255))
    # url.png('hh.png',scale=8,module_color=(0,255,255))
    
# labels
qr_id_label=Label(master=root,text='Enter Your Id',bg='black',foreground='white',width=20,height=2,font=('arial',10))
qr_id_label.place(x=10,y=10)

qr_name_label=Label(master=root,text='Enter Your Name',bg='black',foreground='white',width=20,height=2,font=('arial',10))
qr_name_label.place(x=10,y=70)

qr_message_label=Label(master=root,text='Enter Your Message',bg='black',foreground='white',width=20,height=2,font=('arial',10))
qr_message_label.place(x=10,y=130)


qr_notification_label=Label(master=root,text='Notification',bg='black',foreground='white',width=20,height=2,font=('arial',12))
qr_notification_label.place(x=10,y=350)

qr_notification_message_label=Label(master=root,text='',bg='white',foreground='white',width=30,height=2,font=('arial',12))
qr_notification_message_label.place(x=250,y=350)
# entry boxes
qr_id_entrybox=Entry(master=root,bg='white',foreground='black',width=25,bd=2,font=('arial',15))
qr_id_entrybox.place(x=250,y=10)

qr_name_entrybox=Entry(master=root,bg='white',foreground='black',width=25,bd=2,font=('arial',15))
qr_name_entrybox.place(x=250,y=70)

qr_message_entrybox=Entry(master=root,bg='white',foreground='black',width=25,bd=2,font=('arial',15))
qr_message_entrybox.place(x=250,y=130)
# buttons
qr_generate_button=Button(master=root,command=generate,text='Generate',bg='white',foreground='black',width=15,height=2,font=('times',11,BOLD),bd=10)
qr_generate_button.place(x=10,y=230)

qr_clear_button=Button(master=root,text='Clear',command=clear,bg='white',foreground='black',width=15,height=2,font=('times',11,BOLD),bd=10)
qr_clear_button.place(x=200,y=230)

qr_quit_button=Button(master=root,command=quit_root,text='Quit',bg='white',foreground='black',width=15,height=2,font=('times',11,BOLD),bd=10)
qr_quit_button.place(x=390,y=230)

root.mainloop()