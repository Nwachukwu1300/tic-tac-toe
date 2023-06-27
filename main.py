from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root= Tk()
root.title("Tic-Tac-Toe")
#root.geometry("400x400")

clicked = True
count = 0



def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Function to check if someone has won, working on making the colours change before message box shows
def check_win():
    global winner

    # Define winning combinations
    winning_combinations = [
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
        [b1, b4, b7],
        [b2, b5, b8],
        [b3, b6, b9],
        [b1, b5, b9],
        [b3, b5, b7]
    ]

    for combination in winning_combinations:
        if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] != " ":
            winner = combination[0]["text"]
            #for cell in combination:
                #cell.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", "CONGRATS "+winner+ " WON!!!")
            return True
    return False
               

def reset():
    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for button in buttons:
        button["text"] = " "


#button to check what's been clicked
def b_click(b):
    global clicked, count, winner
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count = count+1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count = count + 1
    else:
        messagebox.showerror("Tic-Tac-Toe", "That box has already been used you donut!\nPick a different box")
    
    if count>=5:
        if check_win():
            disable()
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!!!")
            disable()

        

#creating buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width=6,bg="White", command= lambda: b_click(b9))

#griding buttons
b1.grid(row=0, column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
b4.grid(row=0, column=1)
b5.grid(row=1, column=1)
b6.grid(row=2, column=1)
b7.grid(row=0, column=2)
b8.grid(row=1, column=2)
b9.grid(row=2, column=2)

#creating menu
menu_ = Menu(root)
root.config(menu=menu_)

#create options menu
options_ = Menu(menu_, tearoff=False)
menu_.add_cascade(label="Options", menu=options_)
options_.add_command(label="Reset Game", command=reset)





root.mainloop()
