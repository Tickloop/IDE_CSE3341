import tkinter as tk
from tkinter import ttk
import os

class IDE:
    def __init__(self) -> None:
        # initialize the root
        self.root = tk.Tk()

        # set the size for the window
        self.root.geometry("800x600")

        # even though we can add things directly to the root, let's create a Frame for keeping things
        self.holder_frame = ttk.Frame(self.root)

        # now add some children to it, 2 frames
        self.top_frame = ttk.Frame(self.holder_frame)
        self.bot_frame = ttk.Frame(self.holder_frame)

        # now create the code box and the input box for the top fram
        self.code_input_box = tk.Text(self.top_frame)
        self.user_input_box = tk.Text(self.top_frame)

        # and the output box and the control box with buttons, let's place the buttons is frame of itself
        self.output_box = tk.Text(self.bot_frame)
        self.control_frame = ttk.Frame(self.bot_frame)

        # and the buttons
        self.start_btn = ttk.Button(self.control_frame, text="RUN", command=self.run)
        self.quit_btn = ttk.Button(self.control_frame, text="QUIT", command=self.root.destroy)

        # and now display everything
        self.holder_frame.pack()
        self.top_frame.pack()
        self.bot_frame.pack()
        
        # the input boxes
        self.code_input_box.pack(side=tk.LEFT, pady=10, padx=10)
        self.user_input_box.pack(side=tk.LEFT, pady=10, padx=10)
        
        # the output
        self.output_box.pack(side=tk.LEFT, pady=10, padx=10)
        self.control_frame.pack(side=tk.LEFT, pady=10, padx=10)
        
        # and the btns
        self.start_btn.pack(side=tk.TOP, pady=15)
        self.quit_btn.pack(side=tk.TOP, pady=15)

        # initialize with last test.code and test.data saved
        self.initText()

        # and of course, run the loop
        self.root.mainloop()

    def initText(self):
        # check if file is present and readable
        if os.path.isfile('./test.code'):
            # display in code box
            self.setTextFromFile(self.code_input_box, "test.code")
        
        if os.path.isfile('./test.data'):
            # display in data box
            self.setTextFromFile(self.user_input_box, "test.data")

    
    def getText(self, widget):
        return widget.get("1.0", "end")
    
    def setTextFromFile(self, widget, file):
        # open the file and read
        with open(file, "r") as f:
            # read all the lines at once
            lines = f.read()
            
            # now set the text of the widget
            widget.delete(1.0, "end")
            widget.insert(1.0, lines)

    def showOutput(self, command, output):
        # first delete the current output,
        self.output_box.delete(1.0, "end")

        # dispaly the command that was run
        self.output_box.insert(1.0, f"$user: {command}\n")

        # and now dispaly the output of the command
        self.output_box.insert(float(len(f"$user: {command}\n")), output)


    def run(self):
        # get the text
        code = self.getText(self.code_input_box).strip()
        user_input = self.getText(self.user_input_box).strip()

        # empty check
        if code != "":
            # save code to test.code file    
            with open("test.code", "w") as file:
                file.writelines(code)
            
            # empty check
            if user_input != "":
                with open("test.data", "w") as file:
                    file.writelines(user_input)

                # run with user input
                command = 'python Main.py test.code test.data'
            else:
                # run without user input
                command = 'python Main.py test.code'
            
            output = os.popen(command).read()
            
            # now display the output of running the code
            self.showOutput(command, output)
    

def main():
    IDE()

if __name__ == "__main__":
    main()
        