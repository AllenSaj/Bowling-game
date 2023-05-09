import game
import tkinter as tk
game = game.BowlingGame()

class GUI:
    def __init__(self):
        self.values = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.root = tk.Tk()
        self.boxes = []
        self.output_text = tk.StringVar()
        self.selected_value = tk.StringVar()
        self.selected_value.set('Select roll')
        self.dropdown_menu = tk.OptionMenu(self.root, self.selected_value, *self.values, command = lambda value: self.roll(value))
        self.output = tk.Label(self.root, text= self.output_text.get(), font=('Arial', 16))  
        self.label = tk.Label(self.root, text= 'Enter your roll :', font=('Arial', 16))
    
    def run(self):
        for i in range(11):
            label = i + 1 if i < 10 else "Total"
            frame = tk.LabelFrame(self.root, text = label,  width=120, height=120, bd=1, relief=tk.SOLID)
            frame.grid(row=0, column=i, padx=1)
            self.boxes.append(frame)
            frame.pack_propagate(False)

        self.label.grid(row=2, column=1, columnspan=3, pady=10)
        self.output.grid(row=2, column=5, columnspan=3, pady=10)
        self.dropdown_menu.grid(row=2, column=3, columnspan=3, pady=10)
        self.root.mainloop()

    def roll(self, roll):
        try:
            roll = int(roll) 
        except ValueError:
            print("Please select an integer value.")
        if (roll < 0 or roll > game.frames[game.frameNumber].pins): 
            print('Roll out of range!')
            return
        label = tk.Label(self.boxes[game.frameNumber], text= str(roll), font=('Arial', 16))
        label.pack()
        game.rollBall(roll)
        if (game.bonus and roll > 0):
            label = tk.Label(self.boxes[game.frameNumber-1], text= str(roll), font=('Arial', 12))
            label.pack()
        if (game.isFinished):
            final_label = tk.Label(self.boxes[-1], text= 'Total score:\n'+str(game.score()), font=('Arial', 16))
            final_label.pack()

    def setText(self, type, text):
        if (type == 0):
            self.output_text.set (text)


