IDE for Pretend
---

This repo hosts the single file required to run an IDE to test your programs made 
in the pretend language that we create in CSE 3341 at OSU. This will make 
development faster and make it more fun.

Let me know if anythin seems to be broken

GUI Structure
---

There are 3 text boxes, the first is the code box where you should write your code.

The second, on the right of the first is the user input box, where you should 
write the data you want to supply to simulate user input to your program.

The third is where the output of running your Main.py file is displayed.

To run the program, click "RUN".
To close the window, click "QUIT".


Dependencies
---

In order to run, you will not need any dependencies as tkinter, the GUI library 
I am using, is already installed in modern python releases. To run the gui:

First add gui.py from this repo to your project and then run:

$ python gui.py

This should open a window where you can enter code from pretend language and simulated
user input and run Main.py using the RUN button.

I have tested with python 3.7.0 and it works. In case it doesn't work for you let me know and we can find out why :)

The GUI, runs the following command(s) and displays the output of running the command:

$ python Main.py test.code test.data (If user input is present)

$ python Main.py test.code (If user input is not present)


Future Plans
---

I plan to add more features and make this look better, but this passes my expectations of
the MVP that I had in mind. Feel free to fork and contribute your additions!


