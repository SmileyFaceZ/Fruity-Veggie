import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Graph:
    def __init__(self, df=None, nutrient=None, title=None):
        self.__fontsize = 4

        self.df = df
        self.nutrient = nutrient
        self.title = title

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        self.fig.set_size_inches(7, 6)
        self.fig.subplots_adjust(bottom=0.4)

        plt.title(self.title)

    def energy_process(self):
        pass

    def fat_process(self):
        pass

    def bar_processor(self):
        sns.barplot(data=self.df, x='name', y=self.nutrient)

        plt.xticks(rotation=90, fontsize=self.__fontsize)
        plt.xlabel("hello")

        plt.ylabel(self.nutrient)
        # plt.axhline(y=self.df[self.nutrient].mean(), color='red', ls='--')

    def hist_processor(self):
        sns.histplot(data=self.df, x=self.nutrient)

    def boxplot_processor(self):
        sns.boxplot(data=self.df, x=self.nutrient)

    def scatter_processor(self):
        sns.scatterplot(data=self.df, x='name', y=self.nutrient)
        plt.xticks(rotation=90, fontsize=self.__fontsize)

    def pie_processor(self):
        plt.pie(list(self.df['value']), labels=list(self.df['label']), autopct='%1.2f%%')
        plt.title(self.df['name'][0])

    def network_processor(self):
        pass

    def mean_line(self):
        sns.scatterplot(data=self.df, x='name', y=self.nutrient)
        plt.axhline(y=self.df[self.nutrient].mean(), color='red', ls='--')

    def get_fontsize(self):
        return self.__fontsize


class ChartDecorator(Graph):

    def __init__(self):
        super().__init__()

    def change_fontsize(self, fontsize):
        plt.xticks(fontsize=100)