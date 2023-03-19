import subprocess
from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Python File Converter")

# Set the window size
window_width = 300
window_height = 100
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"+{x_coordinate}+{y_coordinate}")

# Function to show the file dialog and set the file path variable
def browse_file(var):
    file_path = filedialog.askopenfilename()
    var.set(file_path)


# Function to convert the Python file into a DMG or an EXE file
def execute():
    # Get the path of the Python file to convert
    python_file = file_var.get()

    if rb_var.get() == 1:
        # Define the PyInstaller command for converting to DMG
        pyinstaller_cmd = f"pyinstaller --clean --windowed {python_file}"
        output_ext = "dmg"
    else:
        # Define the PyInstaller command for converting to EXE
        pyinstaller_cmd = f"pyinstaller --clean --windowed --onefile {python_file}"
        output_ext = "exe"

    # Run the PyInstaller command
    result = subprocess.run(pyinstaller_cmd, capture_output=True, text=True)

    # Check if the conversion was successful
    if "completed successfully" in result.stdout:
        # Get the name of the output file
        output_file = python_file.replace(".py", "")
        output_file = f"{output_file}.{output_ext}"

        # Show a message box with the path of the output file
        messagebox.showinfo("Conversion Successful", f"Output file: {output_file}")
    else:
        # Show an error message box
        messagebox.showerror("Conversion Error", "An error occurred during conversion.")


# Create the variable to hold the file path
file_var = StringVar()

# Create the radio buttons
rb_var = IntVar()
rb_var.set(1)

rb1_frame = Frame(root)
rb1_frame.grid(row=0, column=0, sticky=W)

rb1 = Radiobutton(rb1_frame, text="Convert Python to DMG", variable=rb_var, value=1)
rb1.grid(row=0, column=0, sticky=W)

rb1_file_btn = Button(rb1_frame, text="Browse File", command=lambda: browse_file(file_var))
rb1_file_btn.grid(row=0, column=1, sticky=E)

rb2_frame = Frame(root)
rb2_frame.grid(row=1, column=0, sticky=W)

rb2 = Radiobutton(rb2_frame, text="Convert Python to EXE", variable=rb_var, value=2)
rb2.grid(row=0, column=0, sticky=W)

rb2_file_btn = Button(rb2_frame, text="Browse File", command=lambda: browse_file(file_var))
rb2_file_btn.grid(row=0, column=1, sticky=E)

# Create the Execute and Close buttons
button_frame = Frame(root)
button_frame.grid(row=2, column=0, pady=10)

execute_btn = Button(button_frame, text="Execute", command=execute)
execute_btn.grid(row=0, column=0)

close_btn = Button(button_frame, text="Close", command=root.destroy)
close_btn.grid(row=0, column=1)

root.mainloop()
