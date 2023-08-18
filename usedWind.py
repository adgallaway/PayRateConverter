import customtkinter as ctk

# Displays the About Information in a New Window
def about(icon):
    ABOUT_TXT = ['Pay Rate Converter', 'by Aaron Gallaway', '(c)2023', 'Version: 1.0']
    about_win = ctk.CTkToplevel()
    about_win.geometry('250x175')
    about_win.title('About Pay Rate Converter')
    about_win.after(200, lambda: about_win.iconbitmap(bitmap=icon))
    for i in range(len(ABOUT_TXT)):
        txt = ABOUT_TXT[i]
        ctk.CTkLabel(about_win, text=txt).pack(padx=40)
    about_btn = ctk.CTkButton(about_win, text='OK', width=135, command=about_win.destroy)
    about_btn.pack(padx=50, pady=10)
    about_win.grab_set()

# Displays the Help Information in a New Window
def help(icon):
    help_win = ctk.CTkToplevel()
    help_win.geometry('250x200')
    help_win.title('Pay Rate Converter Help')
    help_win.after(200, lambda: help_win.iconbitmap(bitmap=icon))
    help_txt ='''Enter the amount of pay in the entry box.
    Make a selection in the To column.
    The From Column will become available.
    Make a selection in the From column.
    All is selected by default.
    Clicking Clear will reset.
    Clicking Cancel will close the app.
    Click Enter.
    The results will display in a new window.
    To continue, click Yes. To quit, click No.'''
    help_lable = ctk.CTkLabel(help_win, text=help_txt)
    help_lable.pack()
    help_btn = ctk.CTkButton(help_win, text='OK', command=help_win.destroy)
    help_btn.pack(pady=10)
    help_win.grab_set()