from tkinter import *

window = Tk()
window.title('Temperature Convector')
window.minsize(width=500, height=500)

celcius_var= IntVar
fahrenheit_var =IntVar

l1 = LabelFrame(window,text='Celcius To Fahrenheit',padx=20, pady=20)
l1.grid(row=2, column=0)

Entry1 = Entry(l1,state='disable')
Entry1.grid(row=4, column=0)

def cel_active():
        Entry2.configure(state='disable')
Entry1.configure(state='normal')

btn_active = Button(window,text='Activate -Celcius to Fahrenheit', command=cel_active)
btn_active.grid(row=6, column=0)

l2 = LabelFrame(window, text='Fahrenheit to Celcius',padx=20, pady=20)
l2.grid(row=2, column=5)

Entry2 = Entry(l2,state='disable')
Entry2.grid(row=4, column=5)

def far_active():
        Entry1.configure(state='disable')
        Entry2.configure(state='normal')

btn_active1 = Button(window,text='Activate -Fahrenheit to Celcius', command=far_active)
btn_active1.grid(row=6, column=5)



def exit():
        window.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=9, column=6)

def convert_C():
        if Entry1['state'] == "normal" and Entry1.get() != "":
                celcius = float(Entry1.get())
                fahrenheit = (celcius*9/5)+32
                result_entry.insert(0, str(fahrenheit))

def convert_f():
        if Entry2['state'] == "normal" and Entry2.get() != "":
                fahrenheit = float(Entry2.get())
                celcius = (fahrenheit-32)*5/9
                result_entry.insert(0, celcius)

result_bnt = Button(window, text='Convert C-F',command=convert_C)
result_bnt.grid(row=7, column=2)

result_bnt2 = Button(window, text='Convert F-C',command=convert_f)
result_bnt2.grid(row=7, column=4)

result_entry = Entry(window, bg='light green', state="readonly")
result_entry.place(x=255, y=150)


def Clear():
        Entry1.delete(0, END)
        Entry2.delete(0, END)
        result_entry.delete(0,END)

Clear_btn = Button(window, text='Clear',command=Clear)
Clear_btn.grid(row=8, column=6)

window.mainloop()

