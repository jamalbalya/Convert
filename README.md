# Convert
Converter python file into .dmg or .exe

This code is a Python script that creates a GUI (Graphical User Interface) using the tkinter library. The GUI contains two radio buttons, each with a "Browse File" button next to it, an "Execute" button, and a "Close" button.

The first radio button is for converting a Python file into a DMG file, and the second radio button is for converting the Python file into an EXE file. When the user selects a radio button and clicks on the corresponding "Browse File" button, a file dialog window appears where the user can select the Python file to be converted.

When the user clicks on the "Execute" button, the Python script checks which radio button is selected and executes the corresponding PyInstaller command to convert the selected Python file into a DMG or an EXE file. If the conversion is successful, a message box appears with the path of the output file. If there is an error during conversion, an error message box appears.

The GUI is structured using frames, which allow the components to be grouped together and positioned in a specific location within the window. The frames are positioned using the grid() method, which allows the components to be positioned in rows and columns.

The window is centered on the screen every time the program is run using the geometry() method, and the root.mainloop() method is used to start the main event loop of the GUI.
