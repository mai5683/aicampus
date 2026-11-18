import tkinter as tk

window = tk.Tk()
window.title("이미지 불러오기")
window.geometry("500x400")

label_viewer = tk.Label(window, bg="lightblue")
label_viewer.pack(fill="both", expand=True)

window.mainloop()
