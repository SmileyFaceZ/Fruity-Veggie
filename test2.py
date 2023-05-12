# import customtkinter as ctk
import tkinter as tk

window = tk.Tk()

window.title("Fruity & Veggies")
window.geometry("1000x800")

def click():
    global x
    x += 2
    # bt.place(x=x, rely=0.5, anchor=tk.CENTER)
    if x < 1000:
        bt.place(x=x)
        window.after(10, click)

def click2():
    global x
    x -= 10

    bt.place(x=x, rely=0.5, anchor=tk.CENTER)


fm = tk.Frame(window, width=600, height=400)
x = 100
bt = tk.Button(fm, text="Start1", font=('arial', 20, 'bold'), width=10, height=3, command=click)
bt.place(x=x, rely=0.5, anchor=tk.CENTER)
bt2 = tk.Button(window, text="Start2", font=('arial', 20, 'bold'), width=10, height=3, command=click2)
bt2.grid(row=0, column=0, padx=50)

label = tk.Label(window, text="Hello", font=('arial', 20, 'bold'))
label.grid(row=0, column=50, padx=50)

fm.grid(row=0, column=1)

window.mainloop()
#
# class SlidePanel(ctk.CTkFrame):
#     def __init__(self, parent, start_pos, end_pos):
#         super().__init__(master=parent)
#
#         self.start_pos = start_pos
#         self.end_pos = end_pos
#         self.width = abs(start_pos - end_pos)
#
#         self.pos = start_pos
#         self.in_start_pos = True
#
#         self.grid(column=0, row=0, sticky="nsew")
#
#     def animate_forward(self):
#         if self.pos > self.end_pos:
#             self.pos -= 0.005
#             self.grid(column=0, row=0, padx=int(self.pos*600), sticky="nsew")
#             self.after(10, self.animate_forward)
#         else:
#             self.in_start_pos = False
#
#     def animate_backward(self):
#         if self.pos < self.start_pos:
#             self.pos += 0.005
#             self.grid(column=0, row=0, padx=int(self.pos*600), sticky="nsew")
#             self.after(10, self.animate_backward)
#         else:
#             self.in_start_pos = True
#
#
# # class SlidePanel(ctk.CTkFrame):
# #     def __init__(self, parent, start_pos, end_pos):
# #         super().__init__(master=parent)
# #
# #         self.start_pos = start_pos
# #         self.end_pos = end_pos
# #         self.width = abs(start_pos - end_pos)
# #
# #         self.pos = start_pos
# #         self.in_start_pos = True
# #
# #
# #         self.place(relx=self.start_pos, rely=0.05, relwidth=0.3, relheight=0.9)
# #
# #     def animate(self):
# #         if self.in_start_pos:
# #             self.animate_forward()
# #         else:
# #             self.animate_backward()
# #
# #     def animate_forward(self):
# #         if self.pos > self.end_pos:
# #             self.pos -= 0.005
# #             self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
# #             self.after(10, self.animate_forward)
# #         else:
# #             self.in_start_pos = False
# #
# #     def animate_backward(self):
# #
# #         if self.pos < self.start_pos:
# #             self.pos += 0.005
# #             self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
# #             self.after(10, self.animate_backward)
# #         else:
# #             self.in_start_pos = True
# #
# window = ctk.CTk()
# window.title("Custom Tkinter")
# window.geometry("600x400")
#
# animated_panel = SlidePanel(window, 0, -0.3)
#
# button_x = 0.5
# button = ctk.CTkButton(window, text="toggle sidebar", command=animated_panel.animated)
# button.place(relx=button_x, rely=0.5, anchor="center")
#
# window.mainloop()
