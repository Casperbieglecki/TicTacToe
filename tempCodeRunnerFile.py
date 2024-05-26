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