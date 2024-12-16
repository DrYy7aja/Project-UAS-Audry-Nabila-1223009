from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, messagebox
import sys


# Fungsi untuk mendapatkan path ke file assets
def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "assets" / "frame0"
    return Path(__file__).parent / "assets" / "frame0"

ASSETS_PATH = get_base_path()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk menampilkan pesan peringatan
def show_warning():
    messagebox.showwarning("Mantapp", "Semangat Menjalani Aktivitasnya!")

# Fungsi untuk mereset semua Text widget
def reset_all():
    """Reset semua Text widget"""
    entry_1.delete(1.0, "end")
    entry_2.delete(1.0, "end")
    entry_3.delete(1.0, "end")
    entry_4.delete(1.0, "end")
    entry_5.delete(1.0, "end")
    entry_6.delete(1.0, "end")
    entry_7.delete(1.0, "end")
    entry_8.delete(1.0, "end")
    entry_9.delete(1.0, "end")
    entry_10.delete(1.0, "end")
    entry_11.delete(1.0, "end")
    entry_12.delete(1.0, "end")
    entry_13.delete(1.0, "end")
    entry_14.delete(1.0, "end")

# Membuat window Tkinter
window = Tk()
window.title("To-Do List Sederhana") 
window.geometry("386x469")
window.configure(bg="#1E7D97")

canvas = Canvas(
    window,
    bg="#1E7D97",
    height=469,
    width=386,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Fungsi untuk membuat shadow pada Text widget
def create_shadow_entry(x, y, width, height, text_widget):
    shadow_offset = 2
    canvas.create_rectangle(
        x + shadow_offset, 
        y + shadow_offset, 
        x + width + shadow_offset, 
        y + height + shadow_offset,
        fill="#555555", 
        outline="#555555"
    )
    
    text_widget.place(
        x=x,
        y=y,
        width=width,
        height=height
    )

# Fungsi untuk membuat shadow pada Button widget
def create_shadow_button(x, y, width, height, button_widget):
    shadow_offset = 2
    canvas.create_rectangle(
        x + shadow_offset, 
        y + shadow_offset, 
        x + width + shadow_offset, 
        y + height + shadow_offset,
        fill="#555555",  
        outline="#555555"
    )
    
    button_widget.place(
        x=x,
        y=y,
        width=width,
        height=height
    )

# Text widgets untuk To-Do List
entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 152.0, 162.0, 27.0, entry_1)

entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 195.0, 162.0, 27.0, entry_2)

entry_3 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 238.0, 162.0, 27.0, entry_3)

entry_4 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 281.0, 162.0, 27.0, entry_4)

entry_5 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 324.0, 162.0, 27.0, entry_5)

entry_6 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 367.0, 162.0, 27.0, entry_6)

entry_7 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(14.0, 410.0, 162.0, 27.0, entry_7)

entry_8 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(195.0, 195.0, 162.0, 27.0, entry_8)

entry_9 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(195.0, 152.0, 162.0, 27.0, entry_9)

entry_10 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(193.0, 238.0, 162.0, 27.0, entry_10)

entry_11 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(193.0, 281.0, 162.0, 27.0, entry_11)

entry_12 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(193.0, 324.0, 162.0, 27.0, entry_12)

entry_13 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(193.0, 367.0, 162.0, 27.0, entry_13)

entry_14 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
create_shadow_entry(193.0, 110.0, 162.0, 27.0, entry_14)

# Tombol submit
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=show_warning,  
    relief="flat"
)
create_shadow_button(204.0, 413.0, 64.0, 40.0, button_1)

# Tombol reset
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=reset_all,  
    relief="flat"
)
create_shadow_button(280.0, 413.0, 64.0, 40.0, button_2)

# Gambar di canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(60.0, 79.0, image=image_image_1)


# Menjalankan window
window.resizable(False, False)
window.mainloop()
