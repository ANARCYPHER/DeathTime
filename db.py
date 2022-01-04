from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title('When People Die: How long already Dead💀')

root.geometry("500x300")


def death():
	if my_entry.get():
		
		current_year = datetime.now().year
		# Calculate TheDeath Time
		your_death = current_year - int(my_entry.get())
		# Show age in message box
		messagebox.showinfo("Death💀", f"Time Is: {your_death}")

	else:
		# Show Error Message
		messagebox.showerror("Error", "You forgot to enter your date!")

my_label = Label(root, text="Enter Year 💀", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate Death!", font=("Helvetica", 18), command=death)
my_button.pack(pady=20)



root.mainloop()