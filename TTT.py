#Proj 1
import tkinter as tk
from tkinter import messagebox


def Game():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Tic Tac Toe')

    #create grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=3)
    root.rowconfigure(3, weight=3)
    turn_track = 0
 
    def winner():
        if but1['text'] == but2['text'] == but3['text'] != '':
            but1.configure(bg = 'red')
            but2.configure(bg = 'red')
            but3.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but1['text']} Wins!')
        elif but4['text'] == but5['text'] == but6['text'] != '':
            but4.configure(bg = 'red')
            but5.configure(bg = 'red')
            but6.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but4['text']} Wins!')
        elif but7['text'] == but8['text'] == but9['text'] != '':
            but7.configure(bg = 'red')
            but8.configure(bg = 'red')
            but9.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but7['text']} Wins!')

        elif but1['text'] == but4['text'] == but7['text'] != '':
            but1.configure(bg = 'red')
            but4.configure(bg = 'red')
            but7.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but1['text']} Wins!')
        elif but2['text'] == but5['text'] == but8['text'] != '':
            but2.configure(bg = 'red')
            but5.configure(bg = 'red')
            but8.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but2['text']} Wins!')
        elif but3['text'] == but6['text'] == but9['text'] != '':
            but3.configure(bg = 'red')
            but6.configure(bg = 'red')
            but9.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but3['text']} Wins!')
        
        elif but1['text'] == but5['text'] == but9['text'] != '':
            but1.configure(bg = 'red')
            but5.configure(bg = 'red')
            but9.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but1['text']} Wins!')
        elif but3['text'] == but5['text'] == but7['text'] != '':
            but3.configure(bg = 'red')
            but5.configure(bg = 'red')
            but7.configure(bg = 'red')
            messagebox.showinfo('icon', f'{but3['text']} Wins!')
        
        else:
            pass


    def onClick(but):
        nonlocal turn_track
        turn_track += 1
        if turn_track%2 == 0:
            but.configure(text = 'x', state = 'disabled')
            winner()
        else:
            but.configure(text = 'o', state = 'disabled')
            winner()


    titlelabel = tk.Label(root, text = 'Tic Tac Toe')
    titlelabel.grid(row=0,column = 1)

#Top row
    but1 = tk.Button(root, text = '', command = lambda: onClick(but1))
    but1.grid(row=1, column=0, sticky='nswe')

    but2 = tk.Button(root, text='', command = lambda: onClick(but2))
    but2.grid(row=1, column=1, sticky='nswe')

    but3 = tk.Button(root, text='', command = lambda: onClick(but3))
    but3.grid(row=1, column=2, sticky='nswe')

#Middle row
    but4 = tk.Button(root, text='', command = lambda: onClick(but4))
    but4.grid(row=2, column=0, sticky='nswe')
    
    but5 = tk.Button(root, text='', command = lambda: onClick(but5))
    but5.grid(row=2, column=1, sticky='nswe')

    but6 = tk.Button(root, text='', command = lambda: onClick(but6))
    but6.grid(row=2, column=2, sticky='nswe')

#Bottom row
    but7 = tk.Button(root, text='', command = lambda: onClick(but7))
    but7.grid(row=3, column=0, sticky='nswe')
    
    but8 = tk.Button(root, text='', command = lambda: onClick(but8))
    but8.grid(row=3, column=1, sticky='nswe')

    but9 = tk.Button(root, text='', command = lambda: onClick(but9))
    but9.grid(row=3, column=2, sticky='nswe')


    root.mainloop()


Game()