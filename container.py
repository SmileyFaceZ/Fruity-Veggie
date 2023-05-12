import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from widget import Widget


class Container(tk.Tk):

    def __init__(self):
        super().__init__()
        self.back_bt1 = None
        self.tp_vegg = None

        self.__tab_fruit_bg = "#FFBF9B"
        self.__tab_vegg_bg = "#B6EADA"

        self.__SCREEN_WIDTH = self.winfo_screenwidth()
        self.__SCREEN_HEIGHT = self.winfo_screenheight()

        self.fruit_df = pd.read_csv("fruits.csv")
        self.veggie_df = pd.read_csv("vegetables.csv")

        self.clear_null_data()

        self.title("Fruity & Veggies")
        self.geometry(f"{self.__SCREEN_WIDTH}x{self.__SCREEN_HEIGHT}")

        self.config(bg='lightgray')  # change background color

        self.home_page()

    def clear_null_data(self):
        self.fruit_df = self.fruit_df.replace('-', None)
        self.fruit_df = self.fruit_df.dropna()
        self.fruit_df = self.fruit_df.reset_index(drop=True)

        self.veggie_df = self.veggie_df.replace('-', None)
        self.veggie_df = self.veggie_df.dropna()
        self.veggie_df = self.veggie_df.reset_index(drop=True)

    def home_page(self):
        self.widget_page1 = Widget(root=self,
                                   bg='lightgray')
        self.widget_page1.page1()
        self.start_bt = tk.Button(self,
                                  text="Start",
                                  font=('arial', 20, 'bold'),
                                  width=10,
                                  height=3,
                                  command=self.home_page2)
        self.start_bt.grid(row=2, column=0, columnspan=2, pady=50)

    def home_page2(self):
        self.widget_page1.destroy_page1()
        self.start_bt.destroy()

        self.notebook = ttk.Notebook(width=self.__SCREEN_WIDTH - 50, height=self.__SCREEN_HEIGHT - 280)
        style = ttk.Style()

        style.configure('CustomNotebook.TNotebook', borderwidth=2)

        self.tab_fruit = tk.Frame(self.notebook, background=self.__tab_fruit_bg)
        self.tab_vegg = tk.Frame(self.notebook, background=self.__tab_vegg_bg)

        self.notebook.add(self.tab_fruit, text='Fruit')
        self.notebook.add(self.tab_vegg, text='Vegetable')

        self.notebook.grid(row=1, column=0)

        self.fruit_tab()
        self.vegg_tab()

        # style = ttk.Style()
        # style.configure('TNotebook.Tab', foreground='green')

    def process_page_fruit(self):
        self.back_bt_fruit.destroy()

        self.process_bt_fruit.destroy()

        self.widget_fruit_tab.destroy_widget_page2()

        self.widget_fruit_tab.page3()

        self.back_bt_fruit2 = tk.Button(self.tab_fruit,
                                       text="Back",
                                       font=('arial', 30, 'bold'),
                                       command=self.back_to_page2_fruit)
        self.back_bt_fruit2.grid(row=4, column=0, padx=30)

    def process_page_vegg(self):
        self.back_bt_vegg.destroy()

        self.process_bt_vegg.destroy()

        self.widget_vegg_tab.destroy_widget_page2()

        self.widget_vegg_tab.page3()

        self.back_bt_vegg2 = tk.Button(self.tab_vegg,
                                        text="Back",
                                        font=('arial', 30, 'bold'),
                                        command=self.back_to_page2_vegg)
        self.back_bt_vegg2.grid(row=4, column=0, padx=30)

    def back_to_page2_fruit(self):
        self.widget_fruit_tab.destroy_widget_page3()
        self.back_bt_fruit2.destroy()
        self.home_page2()

    def back_to_page2_vegg(self):
        self.widget_vegg_tab.destroy_widget_page3()
        self.back_bt_vegg2.destroy()
        self.home_page2()

    def fruit_tab(self):
        self.widget_fruit_tab = Widget(root=self.tab_fruit,
                                       bg=self.__tab_fruit_bg,
                                       label='Fruit',
                                       df=self.fruit_df)
        self.widget_fruit_tab.page2()

        self.back_bt_fruit = tk.Button(self.tab_fruit,
                                 text="Back",
                                 font=('arial', 30, 'bold'),
                                 command=self.back_to_home)
        self.back_bt_fruit.grid(row=4, column=0, padx=30)

        self.process_bt_fruit = tk.Button(self.tab_fruit,
                                    text="Process",
                                    font=('arial', 30, 'bold'),
                                    command=self.process_page_fruit)
        self.process_bt_fruit.grid(row=4, column=1, padx=30)

    def vegg_tab(self):
        self.widget_vegg_tab = Widget(root=self.tab_vegg,
                                      bg=self.__tab_vegg_bg,
                                      label='Vegetable',
                                      df=self.veggie_df)
        self.widget_vegg_tab.page2()

        self.back_bt_vegg = tk.Button(self.tab_vegg,
                                       text="Back",
                                       font=('arial', 30, 'bold'),
                                       command=self.back_to_home)
        self.back_bt_vegg.grid(row=4, column=0, padx=30)

        self.process_bt_vegg = tk.Button(self.tab_vegg,
                                    text="Process",
                                    font=('arial', 30, 'bold'),
                                    command=self.process_page_vegg)
        self.process_bt_vegg.grid(row=4, column=1, padx=30)

    def back_to_home(self):
        print('back from page 2')
        self.notebook.destroy()
        print('delete')
        self.home_page()



