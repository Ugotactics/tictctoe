# IMPORTS THE MODULES TKINTER WHICH WILL BE USED EXTENSIVELY AND THE ITERTOOLS WHICH WILL HELP IN COMBINATION LATER
import tkinter as tk
import itertools

# CREATES THE TK OBJECT AND DEFINES THE METHODS
window = tk.Tk()
window.title("TicTacToe")
window.geometry("400x400")
window.minsize(height=400, width=400)
# THE FRAMES ARE CREATED BECAUSE WE ARE MIXING GRID WITH PACK AND THEY DO NOT HAVE THE SAME MASTER
# SO THIS HELPS TO FIX THAT BY CREATING SEPERATE MASTERS
frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP)
frame2 = tk.Frame(window, width=300, height=300)
frame2.pack(side=tk.TOP)
frame3 = tk.Frame(window, width=5)
frame3.pack(side=tk.TOP)
current_character = 'X'
game_label = tk.Label(frame1, text="X's turn to play", bg="sky blue", fg="black", font=("Arial", 15, "bold"))
game_label.pack()

# THE EMPTY LISTS WILL BE POPULATED ONCE THE CODE STARTS RUNNING
button_list_p = []
entry_list = []
x_list = []
o_list = []
winning_list = []
new_list_o = []
new_list_x = []

# THE WINNING_LIST_P CONTAINS A LIST OF ALL THE POSSIBLE COMBINATIONS THAT WILL RESULT IN A WIN
winning_list_prev = [[(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 1), (2, 0)], [(0, 2), (1, 2), (2, 2)],
                     [(2, 0), (2, 1), (2, 2)], [(1, 0), (1, 1), (1, 2)]]

# THE WINNING_LIST HELPS TO MAKE SURE THAT ORDER DOES NOT MATTER BY MAKING THE SET A LIST
for w in winning_list_prev:
    winning_list.append(set(w))


# THE LABEL MIGHT BE A POOR CHOICE OF NAME BUT IT HELPS TO INITIATE THE OBJECT
# THE NAME WAS CHOSEN BECAUSE MY INITIAL CHOICE OF WIDGET WAS A LABEL AND NOT A BUTTON
class Label:
    def __init__(self, x, y):
        self.restart_button = tk.Button(frame3, width=10, text='Restart',
                                        command=self.restart_game, bg="pink", font=('Italic', 8, "bold"), pady=5)
        self.bg = "#999881"
        self.font = "bold"
        self.label_no = None
        self.button = tk.Button(frame2, text='', height=1, width=3, font=(self.font, 40),
                                bg=self.bg, command=self.button_clicked, state=tk.NORMAL)
        self.x = x
        self.y = y

    # THE GRID_GEOMETRY HELPS TO RETURN THE GEOMETRY OF THE GRID AS A TUPLE BY GIVING BACK THE ROW AND COLUMN
    def return_grid_geometry(self):
        entry_list.append((self.x, self.y))

    # THIS CREATES A BUTTON ELEMENT AND IS TRIGGERED FROM THE CREATE_GRID() FUNCTION
    def create_button(self):
        self.button.grid(row=self.x, column=self.y)
        button_list_p.append(self.button)
        self.return_grid_geometry()

    # THIS DOES NOTHING, IT WAS JUST TO REMOVE A SQIBBLY LINE THAT KEPT DISTURBING IN THE SELF.RESTART_GAME()
    # THAT THE FUNCTION MIGHT BE STATIC
    def do_nothing(self):
        pass

    # THIS METHOD IS TRIGGERED WHEN WE CLICK ON THE BUTTON AND IS THE COMMAND FOR THE SELF.BUTTON IN THE INIT FUNCTION
    # IT CONFIGURES THE BUTTON TO X WHEN O IS CLICKED AND VICE VERSA
    # AND IT ALSO SWITCHES THE GAME LABEL TO WHOSE TURN TO PLAY
    # IT ALSO CHECKS IF THE GAME HAS BEEN WON
    def button_clicked(self):
        global current_character
        if not self.label_no:
            self.button.config(text=current_character)
            self.label_no = current_character
            if current_character == 'X' and len(x_list) < 5:
                current_character = 'O'
                x_list.append((self.x, self.y))
                game_label.config(text="O's turn to play")
            elif current_character == 'O' and len(o_list) < 4:
                current_character = 'X'
                o_list.append((self.x, self.y))
                game_label.config(text="X's turn to play")
            else:
                game_label.config(text="It's a Draw")
            self.check_winning()

    # THIS CHECKS IF THE GAME HAS BEEN WON AND IS TRIGGERED WHEN THE BUTTON IS CLICKED
    # IT MAKES USE OF COMBINATION BY CHECKING THE POSSIBLE COMBINATION FOR THE X_LIST
    # AND CHECKING TO SEE IF IT IS IN THE ENTRY_LIST
    # IT DOES THE SAME FOR THE O_LIST AND DISABLES THE GAME IF THE CONDITIONS ARE MET
    def check_winning(self):
        if len(x_list) >= 3:
            combination_list_x = list(itertools.combinations(x_list, 3))
            for x in combination_list_x:
                new_list_x.append(list(x))
            for new_list1 in new_list_x:
                if set(new_list1) in winning_list:
                    game_label.config(text='Game Over, X wins')
                    self.game_disabled()

        if len(o_list) >= 3:
            combination_list_o = list(itertools.combinations(o_list, 3))
            for o in combination_list_o:
                new_list_o.append(list(o))
            for new_list2 in new_list_o:
                if set(new_list2) in winning_list:
                    game_label.config(text='Game Over, O wins')
                    self.game_disabled()
        if len(o_list) + len(x_list) == 9:
            game_label.config(text="It's a Draw")
            self.game_disabled()

    # THIS STARTS THE GAME FROM THE SCRATCH AND CLEARS THE PREVIOUS WIDGETS EXCEPT THE LABEL
    # IT ALSO DISABLES THE BUTTONS  WITH THE GRID_FORGET FUNCTION
    # THE ELEMENT.DESTROY FUNCTION CLEARS THE WIDGETS WITHOUT DELETING THE ENTIRE FRAME
    def restart_game(self):
        game_label.config(text="X's turn to play")
        self.do_nothing()
        global entry_list
        global button_list_p
        global x_list
        global o_list
        global new_list_o
        global new_list_x
        global current_character
        for b in button_list_p:
            b.grid_forget()
        entry_list = []
        button_list_p = []
        entry_list = []
        x_list = []
        o_list = []
        new_list_o = []
        new_list_x = []
        for element in frame2.winfo_children():
            element.destroy()
        for element in frame3.winfo_children():
            element.destroy()
        current_character = 'X'
        create_grid()

    # THIS BRINGS UP THE RESTART BUTTON ONCE THERE IS WINNER OR A DRAW
    def game_restarts(self):
        self.restart_button.pack()

    # THIS DISABLES THE GAME BY CHECKING IF THE BUTTON HAS BEEN CLICKED ON OR NOT
    # IT RESTARTS THE GAME BY BRINGING UP THE RESTART BUTTON
    def game_disabled(self):
        global current_character
        current_character = ''
        for n in o_list:
            if n not in entry_list:
                self.button.config(text=current_character, state=tk.DISABLED, bg="#000000")
        for n in x_list:
            if n not in entry_list:
                self.button.config(text=current_character, state=tk.DISABLED, bg="#000000")
        self.game_restarts()


# THIS CREATED THE GRID BY USING A FOR LOOP TO BRING UP X AND Y GEOMETRY WHICH WILL BE PASSED INTO THE LABEL CLASS
def create_grid():
    for a in range(0, 3):
        for i in range(0, 3):
            created_label = Label(a, i)
            created_label.create_button()


create_grid()

window.mainloop()
