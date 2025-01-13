
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("800x450")
window.configure(bg="#fcfcfc")


Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Ciccio",
    font=("undefined", 14),
    text_color="#121212",
    hover=True,
    hover_color="#949494",
    height=30,
    width=125,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id1.place(x=360, y=360)
Checkbox_id3 = customtkinter.CTkCheckBox(
    master=window,
    text="Checkbox3",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    )
Checkbox_id3.place(x=30, y=70)
Checkbox_id2 = customtkinter.CTkCheckBox(
    master=window,
    text="Checkbox2",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    )
Checkbox_id2.place(x=0, y=0)



#run the main loop
window.mainloop()