import tkinter
from tkinter import StringVar, font

#Define window
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('ruler.ico')
root.resizable(0,0)

#Define fonts and colors
field_font = ('Cambria', 12)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg=bg_color)

#Define functions

#Define layout
#Create the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font)
output_field =tkinter.Entry(root, width=20, font=field_font)
equal_label = tkinter.Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0)
equal_label.grid(row=0, column=1)
output_field.grid(row=0, column=2)

input_field.insert(0, 'Enter your quantity')

#Create dropdown for metric values
metric_list = ["femto", "pico", "nano", 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_choice = StringVar()
output_choice = StringVar()
input_dropdown = tkinter.OptionMenu(root, input_choice, *metric_list)
output_dropdown = tkinter.OptionMenu(root, output_choice, *metric_list)
to_label = tkinter.Label(root, text="to", font=field_font, bg=bg_color)

input_dropdown.grid(row=1, column=0)
to_label.grid(row=1, column=1)
output_dropdown.grid(row=1, column=2)

input_choice.set('base value')
output_choice.set('base value')

#Create a conversion button
convert_button = tkinter.Button(root, text="Convert", font=field_font, bg=button_color)
convert_button.grid(row=2, column=0, columnspan=3)

#Run the root window's main loop
root.mainloop()