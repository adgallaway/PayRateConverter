#! /usr/bin/Python3

#Created by Aaron Gallaway (c)2023

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import configparser
import calculations
import usedWind

# Set up the Main Window
root = ctk.CTk()
root.title('Pay Rate Converter')
root.geometry('250x410')
# Set the Default Appearance Mode
config = configparser.ConfigParser()
config.read('settings.ini')
set_mode = config['ENVIRONMENT']['mode']
show_after_tax = config['TAX']['show_after_tax']
tax_rate = config['TAX']['rate']
hours = float(config['WORK.WEEK']['hours'])
days = int(config['WORK.WEEK']['days'])
work_week = hours * days

if set_mode == 'dark':
    icon = 'assets/dollar-dark2.ico'
else:
    icon = 'assets/dollar.ico'
root.iconbitmap(default=f'{icon}')
ctk.set_appearance_mode(f'{set_mode}')

def error_msg(value):   # Displays the Appropriate Error Message
    if value == 0:
        msg = 'You must make a valid selection to convert to'
        error = 'INVALID SELECTION!!'
    elif value == 1:
        msg = 'Please enter a number greater than 0'
        error = 'INVALID ENTRY!!'
    elif value == 2:
        msg = 'ERROR writing to settings file!\nPlease try again.'
        error = 'CONFIG FILE ERROR!!'
    messagebox.showwarning('Pay Rate Converter Error', + error + '\n\n' + msg)
    main()

def error_handling(frequency, selection, enter):   # Error Handling and Control

    try:    # Verifies that a To selection was made (no longer needed)
        selection = int(selection)
    except:
        error_msg(0)
    else:
        try:    # Verifies Entry
            pay = abs(float(enter.get()))    # Verifies that a Number was Entered
            _ = 24 / pay             # Verifies that the Entered Number is Not 0
        except:
            error_msg(1)
        else:
            msg_text = calculations.case(frequency, selection, pay)
            results(msg_text)
            clear_entry()

# Change show tax setting
def set_show_tax():
    config['TAX']['show_after_tax'] = str(show_tax.get())
    with open('settings.ini', 'w') as configfile:
            config.write(configfile)

# Save custom settings (hours/day, days/week, & est. tax rate)
def settings(hours, days, tax_rate):
    try:
        config['WORK.WEEK']['hours'] = hours
        config['WORK.WEEK']['days'] = days
        config['TAX']['rate'] = tax_rate
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
    except:
        error_msg(2)
    return

# Changes the Default Mode (light, dark)
def mode(value, icon):

    set_mode = value

    match set_mode:
        case 'light': 
            icon = 'assets/dollar.ico'
        case 'dark': 
            icon = 'assets/dollar-dark2.ico'
    ctk.set_appearance_mode(set_mode)
    root.iconbitmap(f'{icon}')
    
    config['ENVIRONMENT']['mode'] = set_mode
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def results(msg_text):  # Displays the Final Results in a New Window
    show_taxed = config['TAX']['show_after_tax']
    AMT = '{0:,.2f}'
    i = 0
    result = ctk.CTkToplevel()
    result.title('PayCalc Results')
    result.after(200, lambda: result.iconbitmap(bitmap=icon))
    ctk.CTkLabel(result, text= 'Before Estimated Tax').grid(row=0, column=1, sticky='w', padx=20)
    if show_taxed == '1':
        ctk.CTkLabel(result, text= 'After Estimated Tax').grid(row=0, column=2, sticky='w', padx=20)
    for text, amt, taxed in msg_text:  # Creates Labels for the Results
        i = i + 1
        ctk.CTkLabel(result, text= text).grid(row=i, column=0, sticky='w', padx=20)
        ctk.CTkLabel(result, text= '$' + AMT.format(amt)).grid(row=i, column=1, sticky='w', padx=20)
        if show_taxed == '1':
            ctk.CTkLabel(result, text= '$' + AMT.format(taxed)).grid(row=i, column=2, sticky='w', padx=20)
        i = i + 1
    result_label = ctk.CTkLabel(result, text= 'Do you want to continue?')
    continue_btn = ctk.CTkButton(result, text='yes', command=result.destroy)
    quit_btn = ctk.CTkButton(result, text='No', command=root.destroy)
    result_label.grid(row=i, column=0, columnspan=2)
    continue_btn.grid(row=i + 1, column=0, sticky='w', padx=10, pady=10)
    quit_btn.grid(row=i + 1, column=1, sticky='e', padx=10, pady=10)
    result.grab_set()

def do_nothing():
    pass

# Clears the Entry Box and Resets
def clear_entry():
    ctk.CTkEntry(root, width=90).delete(0, 'end')
    main()

def main():  # Set up the gui

    def enable_to():    # Enables the Buttons to Convert To
        i = 2   # Designates the Starting Row Number (the first button will be in the third row, or row=2)
        match int(from_btns.get()):    # Disables the Button that equals the Converting From Selection
            case 1:
                for text, value in SELECT:
                    if value == 1:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
            case 2:
                for text, value in SELECT:
                    if value == 2:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
            case 3:
                for text, value in SELECT:
                    if value == 3:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
            case 4:
                for text, value in SELECT:
                    if value == 4:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
            case 5:
                for text, value in SELECT:
                    if value == 5:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
            case 6:
                for text, value in SELECT:
                    if value == 6:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disable').grid(row=i, column=1, sticky='w')
                        i = i + 1
                    else:
                        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='normal').grid(row=i, column=1, sticky='w')
                        i = i + 1
        to_all = ctk.CTkRadioButton(root, text='All', variable=to_btns, value=0, state='normal')
        to_all.invoke(1)   # Sets Default Selection
        to_all.grid(row=i, column=1, sticky='w')

        # Enables the Enter Button 
        enter_btn = ctk.CTkButton(root, text='ENTER', width=20, state='normal', command=lambda: error_handling(from_btns.get(), to_btns.get(), enter))
        enter_btn.grid(row=i+1, column=0, columnspan=2, padx=10, pady=10, sticky='we')
    
    SELECT = [
        ('Hourly', 1),
        ('Weekly', 2),
        ('Bi-Weekly', 3),
        ('Semi-Monthly', 4),
        ('Monthly', 5),
        ('Annually', 6)]

# Set up Labels and the Entry Box
    label = ctk.CTkLabel(root, text='Enter the amount:')
    label.grid(row=0, column=0, padx=10, pady=10)
    enter = ctk.CTkEntry(root, width=90)
    enter.grid(row=0, column=1, pady=10, sticky='w')
    from_label = ctk.CTkLabel(root, text='From:')
    to_label = ctk.CTkLabel(root, text='To:')
    from_label.grid(row=1, column=0, padx=10, sticky='w')
    to_label.grid(row=1, column=1, sticky='w')

# Set up the Convert From Buttons (frequency) and Convert To Buttons (selection)
    from_btns = ctk.StringVar()
    to_btns = ctk.StringVar()
    i = 2
    for text, value in SELECT:
        ctk.CTkRadioButton(root, text=text, variable=from_btns, value=value, state='normal', command=enable_to).grid(row=i, column=0, sticky='w', padx=10, pady=5)
        ctk.CTkRadioButton(root, text=text, variable=to_btns, value=value, state='disabled').grid(row=i, column=1, sticky='w')
        i = i + 1    
    to_all = ctk.CTkRadioButton(root, text='All', variable=to_btns, value=0, state='disabled')
    to_all.grid(row=i, column=1, sticky='w')

# Set up the Clear, Enter, and Cancel Buttons
    clear_btn = ctk.CTkButton(root, text='CLEAR', width=10, command=clear_entry)
    clear_btn.grid(row=i, column=0, sticky='w', padx=10, pady=5)
    enter_btn = ctk.CTkButton(root, text='ENTER', state='disabled')
    enter_btn.grid(row=i+1, column=0, columnspan=2, padx=10, pady=10, sticky='we')
    cancel_btn = ctk.CTkButton(root, text='CANCEL', command= root.destroy)
    cancel_btn.grid(row=i+2, column=0, columnspan=2, padx=10, sticky='we')

show_tax = tk.IntVar(root, show_after_tax)
# Set up the Menu
menu_bar = tk.Menu(root)
# Set up the File Menu <New, Exit>
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=clear_entry)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)
# Set up the View Menu <Light, Dark>
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_radiobutton(label='Light', state='normal', value='light', command=lambda: mode('light', icon))
view_menu.add_radiobutton(label='Dark', state='active', value='dark', command=lambda: mode('dark', icon))
view_menu.add_checkbutton(label= 'Show After Tax', state='active', onvalue= 1, offvalue= 0, variable= show_tax, command= set_show_tax)
menu_bar.add_cascade(label='View', menu=view_menu)

settings_menu = tk.Menu(menu_bar, tearoff=0)
work_menu = tk.Menu(menu_bar, tearoff=0)
tax_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_cascade(menu= work_menu, label= 'Work Week')
settings_menu.add_cascade(menu= tax_menu, label= 'Tax Rate')
work_menu.add_command(label= f'{hours} Hours per Day')
work_menu.add_command(label= f'{days} Days per Week')
work_menu.add_command(label= f'{work_week} Hours per Week')
work_menu.add_separator()
work_menu.add_command(label= 'Change Settings', command= do_nothing)
settings_menu.add_separator()
tax_menu.add_command(label= f'Tax Rate: {tax_rate}')
tax_menu.add_separator()
tax_menu.add_command(label= 'Change Tax Rate', command= do_nothing)
menu_bar.add_cascade(label='Settings', menu=settings_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label='Help', command=lambda: usedWind.help(icon))
help_menu.add_separator()
help_menu.add_command(label='About...', command=lambda: usedWind.about(icon))
menu_bar.add_cascade(label='Help', menu=help_menu)

main()
root.config(menu=menu_bar)
root.mainloop()