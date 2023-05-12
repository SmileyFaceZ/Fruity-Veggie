from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from processor import Graph
from processor import ChartDecorator
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from PIL import Image, ImageTk
import matplotlib
matplotlib.use('TkAgg')


class Widget:

    def __init__(self, root, bg, label='', df='', element=''):
        self.status_treeview = True
        self.another_nutrient_value_list = None
        self.graph_df_to_process = None
        self.lbf_another_nutrient = None
        self.graph_type = "Bar Graph"
        self.nutrient = "energy (kcal/kJ)"
        self.another_nutrient = "water (g)"
        self.__fm_cb = None
        self._BG_COLOR = '#B9EDDD'

        self.nutrient_value_list = []
        self.menu = []
        self.graph_list = ["Bar Graph", "Histogram Graph", "Box Plot", "Scatter Plot", "Pie Chart", "Network"]

        self.__root = root
        self.__label = label
        self.__bg = bg
        self.__df = df
        self.__element = element

        self.cd = ChartDecorator()

    def create_topic_label(self):
        self.topic_label = tk.Label(
            text="Fruity & Veggies",
            font=('arial', 90, 'bold'),
            width=28,
            background='#EEEEEE',
            foreground='#577D86')
        self.topic_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

    def image_homepage(self):
        self.fm_img = tk.Frame(width=600, height=400)
        self.fm_img.grid(row=1, column=0, columnspan=2, pady=60)

        self.bg_image = ImageTk.PhotoImage(Image.open("fruitveg.jpg"))
        self.label_img = tk.Label(self.fm_img, image=self.bg_image)
        # self.label_img.pack()
        self.label_img.grid(row=0, column=0)

    def create_label(self):
        self.label = tk.Label(self.__root,
                              text=self.__label,
                              font=('arial', 50, 'bold'),
                              bg=self.__bg,
                              width=49)
        self.label.grid(row=1, column=0, columnspan=2, pady=10)

    def create_listbox(self):
        self.nutrient_value_list = []
        self.menu = []

        self.fm = tk.Frame(self.__root, bd=2, highlightbackground="black", highlightthickness=3)
        self.fm.grid(row=2, column=0, padx=30, pady=20)

        # Create Listbox and Scroll bar
        self.scrollbar = tk.Scrollbar(self.fm)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(self.fm,
                                  height=13,
                                  width=40,
                                  font=("Arial", 20),
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack()

        for item in self.__df['name']:
            self.listbox.insert("end", item)

        self.listbox.bind("<<ListboxSelect>>", self.text_display)

        self.listbox.bind("<<ListboxSelect>>")  # test
        self.listbox.focus_set()  # auto display listbox
        self.listbox.pack()

    def create_treeview(self):
        self.fm2 = tk.Frame(self.__root, bd=2, highlightbackground="black", highlightthickness=3)
        self.fm2.grid(row=2, column=1, padx=30, pady=20)

        self.scrollbar2 = tk.Scrollbar(self.fm2)
        self.scrollbar2.pack(side="right", fill="y")

        self.treeview = ttk.Treeview(self.fm2,
                                     columns=("name", "nutrient"),
                                     show="headings",
                                     height=16,
                                     yscrollcommand=self.scrollbar2.set,
                                     )

        self.scrollbar2.config(command=self.treeview.yview)
        self.scrollbar2.pack(side="right", fill="y")

        self.treeview.heading("name", text="Name")
        self.treeview.heading("nutrient", text=self.nutrient)

        self.treeview.column("name", width=500)
        self.treeview.column("nutrient", width=100)

        self.treeview.pack()

    def create_clear_button(self):
        self.fm_bt1 = tk.Frame(self.__root, bg=self.__bg)
        self.fm_bt1.grid(row=3, column=1, pady=20)

        self.clear_bt1 = tk.Button(self.fm_bt1, text="Clear", font=('arial', 30, 'bold'), command=self.clear_item)
        self.clear_bt1.grid(row=0, column=0, padx=30)

    def create_select_button(self):
        self.select_bt1 = tk.Button(self.fm_bt1,
                                    text="Select All",
                                    font=('arial', 30, 'bold'),
                                    command=self.select_item)
        self.select_bt1.grid(row=0, column=1, padx=30)

    def create_lbf_nutrient(self):
        self.nutrient_name_list = list(self.__df.columns[1:])
        self.__fm_cb = tk.Frame(self.__root, bg=self.__bg)

        self.labelFrame1 = tk.LabelFrame(self.__fm_cb, text="Select Nutrient Type", bg=self.__bg)

        self.cb_type = ttk.Combobox(self.labelFrame1, values=self.nutrient_name_list)
        self.cb_type.current(0)
        self.cb_type.bind('<Key>', 'break')
        self.cb_type.bind('<<ComboboxSelected>>', self.cb_selected_nutrient)
        self.cb_type.pack()

        self.labelFrame1.grid(row=0, column=1, padx=15)

        self.__fm_cb.grid(row=3, column=0)

    def cb_selected_nutrient_another(self, event):
        self.another_nutrient = self.cb_type_remove.get()
        self.treeview.heading("another_nutrient", text=self.another_nutrient)

    def create_lbf_chart(self):
        self.lbf_chart = tk.LabelFrame(self.__fm_cb, text="Select Chart Type", bg=self.__bg)

        self.cb_type2 = ttk.Combobox(self.lbf_chart, values=self.graph_list)
        self.cb_type2.current(0)
        self.cb_type2.bind('<Key>', 'break')  # ไม่ให้พิมใน combobox
        self.cb_type2.bind('<<ComboboxSelected>>', self.cb_selected_chart)
        self.cb_type2.pack()

        self.lbf_chart.grid(row=0, column=0, padx=15)

    def create_lbf_chart2(self):
        self.lbf_chart2 = tk.LabelFrame(self.__root, text="Select Chart Type", bg=self.__bg)

        self.cb_type2 = ttk.Combobox(self.lbf_chart, values=self.graph_list)
        self.cb_type2.current(0)
        self.cb_type2.bind('<Key>', 'break')  # ไม่ให้พิมใน combobox
        self.cb_type2.bind('<<ComboboxSelected>>', self.cb_selected_chart)
        self.cb_type2.pack()

        self.lbf_chart2.grid(row=1, column=1, padx=15)

    def create_lbf_descriptive_statistics(self, nutrient, value_df=None, min=None, max=None, mean=None, graph=None):
        self.lbf_stat = tk.LabelFrame(self.__root, text=f"Descriptive Statistics {nutrient}", bg=self.__bg)
        if graph == "Pie Chart":
            min = round(min, 5)
            max = round(max, 5)
            mean = round(mean, 5)

            var_min = tk.DoubleVar()
            var_min.set(min)

            var_max = tk.DoubleVar()
            var_max.set(max)

            var_mean = tk.DoubleVar()
            var_mean.set(mean)

            min_lbf = tk.LabelFrame(self.lbf_stat, text="Min", bg=self.__bg)
            min_text = tk.Entry(min_lbf, textvariable=var_min, state='disabled', width=15)
            min_text.pack()
            min_lbf.grid(row=0, column=0, padx=10, pady=10)

            max_lbf = tk.LabelFrame(self.lbf_stat, text="Max", bg=self.__bg)
            max_text = tk.Entry(max_lbf, textvariable=var_max, state='disabled', width=15)
            max_text.pack()
            max_lbf.grid(row=0, column=1, padx=10, pady=10)

            mean_lbf = tk.LabelFrame(self.lbf_stat, text="Mean", bg=self.__bg)
            mean_text = tk.Entry(mean_lbf, textvariable=var_mean, state='disabled', width=15)
            mean_text.pack()
            mean_lbf.grid(row=0, column=2, padx=10, pady=10)

        else:
            stats = value_df.describe()

            min = round(stats.loc['min'], 5)
            max = round(stats.loc['max'], 5)
            mean = round(stats.loc['mean'], 5)

            total = round(value_df.sum(), 5)
            std = round(stats.loc['std'], 5)
            var = round(std ** 2, 5)

            # corr = round(value_df.corr(), 3)
            corr = 99999
            q1 = round(stats.loc['25%'], 5)
            q3 = round(stats.loc['75%'], 5)

            iqr = round(q3 - q1, 5)
            out_min = round(q1 - 1.5 * iqr, 5)
            out_max = round(q3 + 1.5 * iqr, 5)

            var_min = tk.DoubleVar()
            var_min.set(min)

            var_max = tk.DoubleVar()
            var_max.set(max)

            var_mean = tk.DoubleVar()
            var_mean.set(mean)

            var_total = tk.DoubleVar()
            var_total.set(total)

            var_std = tk.DoubleVar()
            var_std.set(std)

            var_var = tk.DoubleVar()
            var_var.set(var)

            var_corr = tk.DoubleVar()
            var_corr.set(corr)

            var_q1 = tk.DoubleVar()
            var_q1.set(q1)

            var_q3 = tk.DoubleVar()
            var_q3.set(q3)

            var_iqr = tk.DoubleVar()
            var_iqr.set(iqr)

            var_out_min = tk.DoubleVar()
            var_out_min.set(out_min)

            var_out_max = tk.DoubleVar()
            var_out_max.set(out_max)

            min_lbf = tk.LabelFrame(self.lbf_stat, text="Min", bg=self.__bg)
            min_text = tk.Entry(min_lbf, textvariable=var_min, state='disabled', width=15)
            min_text.pack()
            min_lbf.grid(row=0, column=0, padx=20)

            max_lbf = tk.LabelFrame(self.lbf_stat, text="Max", bg=self.__bg)
            max_text = tk.Entry(max_lbf, textvariable=var_max, state='disabled', width=15)
            max_text.pack()
            max_lbf.grid(row=0, column=1, padx=20)

            mean_lbf = tk.LabelFrame(self.lbf_stat, text="Mean", bg=self.__bg)
            mean_text = tk.Entry(mean_lbf, textvariable=var_mean, state='disabled', width=15)
            mean_text.pack()
            mean_lbf.grid(row=0, column=2, pady=10)

            total_lbf = tk.LabelFrame(self.lbf_stat, text="Total", bg=self.__bg)
            total_text = tk.Entry(total_lbf, textvariable=var_total, state='disabled', width=15)
            total_text.pack()
            total_lbf.grid(row=1, column=0, padx=20, pady=10)

            std_lbf = tk.LabelFrame(self.lbf_stat, text="Standard Deviation", bg=self.__bg)
            std_text = tk.Entry(std_lbf, textvariable=var_std, state='disabled', width=15)
            std_text.pack()
            std_lbf.grid(row=1, column=1, padx=20)

            var_lbf = tk.LabelFrame(self.lbf_stat, text="Variance", bg=self.__bg)
            var_text = tk.Entry(var_lbf, textvariable=var_var, state='disabled', width=15)
            var_text.pack()
            var_lbf.grid(row=1, column=2, padx=20)

            corr_lbf = tk.LabelFrame(self.lbf_stat, text="Correlation", bg=self.__bg)
            corr_text = tk.Entry(corr_lbf, textvariable=var_corr, state='disabled', width=15)
            corr_text.pack()
            corr_lbf.grid(row=2, column=0, padx=20, pady=10)

            q1_lbf = tk.LabelFrame(self.lbf_stat, text="Quartile 1", bg=self.__bg)
            q1_text = tk.Entry(q1_lbf, textvariable=var_q1, state='disabled', width=15)
            q1_text.pack()
            q1_lbf.grid(row=2, column=1, padx=20)

            q3_lbf = tk.LabelFrame(self.lbf_stat, text="Quartile 3", bg=self.__bg)
            q3_text = tk.Entry(q3_lbf, textvariable=var_q3, state='disabled', width=15)
            q3_text.pack()
            q3_lbf.grid(row=2, column=2, padx=20)

            iqr_lbf = tk.LabelFrame(self.lbf_stat, text="Inter Quartile Range (IQR)", bg=self.__bg)
            iqr_text = tk.Entry(iqr_lbf, textvariable=var_iqr, state='disabled', width=15)
            iqr_text.pack()
            iqr_lbf.grid(row=3, column=0, padx=20, pady=10)

            out_min_lbf = tk.LabelFrame(self.lbf_stat, text="Outlier Min", bg=self.__bg)
            out_min_text = tk.Entry(out_min_lbf, textvariable=var_out_min, state='disabled', width=15)
            out_min_text.pack()
            out_min_lbf.grid(row=3, column=1, padx=20)

            out_max_lbf = tk.LabelFrame(self.lbf_stat, text="Outlier Max", bg=self.__bg)
            out_max_text = tk.Entry(out_max_lbf, textvariable=var_out_max, state='disabled', width=15)
            out_max_text.pack()
            out_max_lbf.grid(row=3, column=2, padx=20)

        self.lbf_stat.grid(row=2, column=1)

    def create_lbf_setting(self, func_check, bg, font):
        self.var = tk.IntVar()
        self.var.set(font)
        self.lbf_setting = tk.LabelFrame(self.__root, text='Setting', bg=self.__bg)

        self.lbf_spinbox = tk.LabelFrame(self.lbf_setting, text='Font Size', bg=bg)

        spin = tk.Spinbox(self.lbf_spinbox, from_=1, to=100, width=10, justify='center', textvariable=self.var,
                          command=self.change_font_size)
        spin.pack()

        self.lbf_spinbox.grid(row=0, column=0, pady=5)

        display = tk.BooleanVar()

        mean_line = tk.Checkbutton(self.lbf_setting, text='Display Mean Line', variable=display, command=func_check,
                                   bg=bg)
        mean_line.grid(row=1, column=0, pady=5)

        self.lbf_setting.grid(row=3, column=1)

    def page1(self):
        self.create_topic_label()
        self.image_homepage()

    def page2(self):
        self.create_label()

        self.create_listbox()

        self.create_treeview()

        self.create_clear_button()

        self.create_select_button()

        self.create_lbf_nutrient()

        self.create_lbf_chart()

    def page3(self):
        """
                                    name                energy (kcal/kJ)
        0                   Apple nutrition facts             4.167
        1                 Apricot nutrition facts             4.188
        2                       Avocado nutrition             4.188
        3                  Banana nutrition facts             4.169
        4                  Blackberries nutrition             4.209
        5               Blueberry nutrition facts             4.211

        energy (kcal/kJ)
        Bar Graph
        """
        new_df, nutrient, graph = self.get_df_treeview()
        # print(new_df)
        # new_df = new_df[float(new_df['value'])]
        # print(new_df['value'].tolist())
        # print(new_df['value'].tolist())
        # print(type(new_df['value'].min()))

        self.graph_maker = Graph(df=new_df,
                                 nutrient=nutrient,
                                 title=self.__label)
        if graph == "Pie Chart":
            x = [float(i) for i in new_df['value'].tolist()]
            self.create_lbf_descriptive_statistics(min=min(x),
                                                   max=max(x),
                                                   mean=sum(x)/len(x),
                                                   nutrient=nutrient,
                                                   graph=graph)
        else:
            self.create_lbf_descriptive_statistics(value_df=new_df[self.nutrient],
                                                   nutrient=nutrient,
                                                   graph=graph)

        if graph == "Bar Graph":
            self.graph_maker.bar_processor()
        elif graph == "Histogram Graph":
            self.graph_maker.hist_processor()
        elif graph == "Pie Chart":
            self.graph_maker.pie_processor()
        elif graph == "Network":
            self.graph_maker.network_processor()
        elif graph == "Scatter Plot":
            self.graph_maker.scatter_processor()
        elif graph == "Box Plot":
            self.graph_maker.boxplot_processor()

        self.fig_hist = Figure()
        self.ax_hist = self.fig_hist.add_subplot()

        self.fig_canvas = FigureCanvasTkAgg(self.graph_maker.fig, master=self.__root)
        self.fig_canvas.get_tk_widget().grid(row=1, column=0, rowspan=4,
                                             sticky="news", padx=10, pady=10)

    def change_font_size(self):
        self.cd.change_fontsize(self.var.get())
        print(self.var.get())

    def text_display(self, event):
        menu = self.listbox.get(self.listbox.curselection())
        for index, item in enumerate(self.__df['name']):
            if menu == item:
                result = self.__df[self.nutrient][index]
                if self.nutrient == "energy (kcal/kJ)":
                    number = self.__df[self.nutrient][index]
                    kcal, kj = number.split("/")
                    result = round(int(kj) / int(kcal), 3)

                if self.graph_type == "Scatter Plot":
                    result2 = self.__df[self.another_nutrient][index]
                    self.treeview.insert(parent='', index=tk.END, values=(menu, result, result2))
                    self.nutrient_value_list.append(result2)
                    self.another_nutrient_value_list.append(result)
                elif self.graph_type == "Pie Chart":
                    if self.nutrient == "Energy":
                        pass
                    elif self.nutrient == "Total Fat":
                        pass
                    elif self.nutrient == "Mineral":
                        pass
                    elif self.nutrient == "Vitamins":
                        pass

                else:
                    self.treeview.insert(parent='', index=tk.END, values=(menu, result))
                    self.nutrient_value_list.append(result)
                    self.menu.append(menu)
                break

        selected_item = self.listbox.curselection()
        if selected_item:
            self.listbox.delete(selected_item)

    def clear_item(self):
        self.nutrient_value_list = []
        self.menu = []
        self.listbox.delete(0, tk.END)
        for item in self.__df['name']:
            self.listbox.insert("end", item)
        self.treeview.delete(*self.treeview.get_children())

    def select_item(self):
        self.nutrient_value_list = []
        self.menu = []
        self.listbox.delete(0, tk.END)
        self.treeview.delete(*self.treeview.get_children())

        for index, item in enumerate(self.__df['name']):

            if self.nutrient == "energy (kcal/kJ)":
                result = self.__df[self.nutrient][index]
                number = self.__df[self.nutrient][index]
                kcal, kj = number.split("/")
                result = round(int(kj) / int(kcal), 3)
            else:
                result = float(self.__df[self.nutrient][index])

            self.treeview.insert(parent='', index=tk.END, values=(item, result))
            self.menu.append(item)
            self.nutrient_value_list.append(result)

        self.listbox.selection_set(0, tk.END)

    def cb_selected_nutrient(self, event):
        self.nutrient = self.cb_type.get()
        if self.status_treeview:
            self.treeview.heading("nutrient", text=self.nutrient)
            self.treeview.delete(*self.treeview.get_children())

    def cb_selected_chart(self, event):
        self.graph_type = self.cb_type2.get()

        if self.graph_type == "Scatter Plot":
            remove_choose_nutrient = [x for x in self.nutrient_name_list if x != self.nutrient]
            self.lbf_another_nutrient = tk.LabelFrame(self.__fm_cb, text="Select Another Nutrient Type", bg=self.__bg)
            self.cb_type_remove = ttk.Combobox(self.lbf_another_nutrient, values=remove_choose_nutrient)
            self.cb_type_remove.current(0)
            self.cb_type_remove.bind('<Key>', 'break')
            self.cb_type_remove.bind('<<ComboboxSelected>>', self.cb_selected_nutrient_another)
            self.cb_type_remove.pack()

            self.lbf_another_nutrient.grid(row=0, column=2, padx=15)

            self.treeview.config(columns=("name", "nutrient", "another_nutrient"))
            self.treeview.heading("name", text="Name")
            self.treeview.heading("nutrient", text=self.nutrient)
            self.treeview.heading("another_nutrient", text=self.another_nutrient)

        elif self.graph_type == "Pie Chart":
            self.fm_bt1.destroy()
            self.status_treeview = False
            if self.lbf_another_nutrient is not None:
                self.lbf_another_nutrient.destroy()
            self.cb_type.config(values=['Macronutrients', 'Minerals', 'Vitamins'])
            self.cb_type.set("Choose a Nutrient Type")

            self.treeview.destroy()
            self.scrollbar2.destroy()

            self.cb_menu = ttk.Combobox(self.fm2, values=list(self.__df['name']), width=50, font=("Arial", 20, "bold"))
            self.cb_menu.set(f'Choose a {self.__label}')
            self.cb_menu.bind('<Key>', 'break')
            self.cb_menu.bind('<<ComboboxSelected>>', self.cb_selected_menu)

            self.cb_menu.grid(sticky='news')
            self.__fm_cb.config(pady=10)

        else:
            if self.lbf_another_nutrient is not None:
                self.lbf_another_nutrient.destroy()
            self.cb_type.config(values=self.nutrient_name_list)
            self.cb_type.current(0)

            self.treeview.config(columns=("name", "nutrient"))

            self.treeview.heading("name", text="Name")
            self.treeview.heading("nutrient", text=self.nutrient)

            self.treeview.column("name", width=500)
            self.treeview.column("nutrient", width=100)

            self.treeview.config(height=16)

    def cb_selected_menu(self, event):
        menu = self.cb_menu.get()
        menu_df = self.__df[self.__df['name'] == menu]
        _list = []
        self.pie_df = {'label': [], 'value': [], 'name': menu}
        if self.nutrient == "Macronutrients":
            _list = ['protein (g)', 'carbohydrates (g)', 'sugars (g)']

        elif self.nutrient == "Minerals":
            _list = ['calcium (mg)', 'iron (mg)', 'magnessium (mg)', 'phosphorus (mg)',
                     'potassium (mg)', 'sodium (g)']

        elif self.nutrient == "Vitamins":
            _list = ['vitamin A (IU)', 'vitamin C (mg)', 'vitamin B1 (mg)', 'vitamin B2 (mg)',
                     'vitamin B3 (mg)', 'vitamin B5 (mg)', 'vitamin B6 (mg)', 'vitamin E (mg)']

        self.pie_df['value'] = menu_df[_list].values.tolist()[0]
        self.pie_df['label'] = _list

    def clear_page1(self):
        for child in self.__root.winfo_children():
            child.destroy()

    def delete_widget_page2(self):
        self.label.destroy()
        self.listbox.destroy()
        self.fm2.destroy()
        self.fm_bt1.destroy()
        self.__fm_cb.destroy()
        self.fm.destroy()

    def get_df_treeview(self):
        graph_df_to_process = None
        if self.graph_type == "Scatter Plot":
            graph_df_to_process = pd.DataFrame(
                {'name': self.menu,
                 self.nutrient: self.nutrient_value_list,
                 self.another_nutrient: self.another_nutrient_value_list})

        elif self.graph_type == "Pie Chart":
            graph_df_to_process = pd.DataFrame(self.pie_df)

        else:
            graph_df_to_process = pd.DataFrame({'name': self.menu, self.nutrient: self.nutrient_value_list})
            
        return graph_df_to_process, self.nutrient, self.graph_type

    def destroy_page1(self):
        self.fm_img.destroy()

    def display_mean_line(self):
        self.graph_maker.mean_line()

    def destroy_widget_page3(self):
        self.fig_canvas.get_tk_widget().destroy()
        self.lbf_stat.destroy()

    def destroy_widget_page2(self):
        self.label.destroy()
        self.__fm_cb.destroy()
        self.fm.destroy()
        self.fm_bt1.destroy()
        self.fm2.destroy()
