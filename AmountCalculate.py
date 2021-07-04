#!/usr/bin/env python
from tkinter import *
import pandas as pd
def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + '.'.join(reversed(groups))
def clicked ():    
    sl_value=float(txt_value.get())
    entry=float(txt_entry.get())
    sl_price=float(txt_sl.get())
    tp_price = float(txt_tp.get())
    amount = int((sl_value/(1000*(sl_price-entry)))*(-1))
    tp = int(amount*(tp_price-entry)*1000)

    lbl_blank = Label (window, text = "")
    lbl_blank.grid (column=0, row=7) 

    lbl_amount = Label (window, text = "Amount")
    lbl_amount.grid (column=0, row=8) 
    lbl_amount_res = Label (window, text = group(amount))
    lbl_amount_res.grid (column=1, row=8)

    lbl_stoploss = Label (window, text = "Stoploss")
    lbl_stoploss.grid (column=0, row=9) 
    lbl_stoploss_res = Label (window, text = group(sl_value*(-1)))
    lbl_stoploss_res.grid (column=1, row=9)

    lbl_takeprofit = Label (window, text = "Take Profit")
    lbl_takeprofit.grid (column=0, row=10) 
    lbl_takeprofit_res = Label (window, text = group(tp))
    lbl_takeprofit_res.grid (column=1, row=10)

window = Tk()
window.title("Amount Caculate")
window.geometry ('200x300')
# window['background']='#856ff8'
lbl_value = Label (window, text = "Trade Value")
lbl_value.grid (column = 0, row=1)
txt_value = Entry(window,width=10)
txt_value.grid(column=1, row=1)


lbl_entry = Label (window, text = "Entry")
lbl_entry.grid (column = 0, row=2)
txt_entry = Entry(window,width=10)
txt_entry.grid(column=1, row=2)

lbl_sl = Label (window, text = "Stoploss")
lbl_sl.grid (column = 0, row=3)
txt_sl = Entry(window,width=10)
txt_sl.grid(column=1, row=3)

lbl_tp = Label (window, text = "Take Profit")
lbl_tp.grid (column = 0, row=4)
txt_tp = Entry(window,width=10)
txt_tp.grid(column=1, row=4)

btn = Button (window, text = "Submit", bg="orange", fg = "red", command = clicked)
btn.grid(column=1, row = 6)
window.mainloop()
