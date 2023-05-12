import processor as pc


class ChartDecorator:

    def __init__(self):
        self.graph = pc.Graph()
        pass

    def change_fontsize(self, fontsize):
        self.__fontsize = fontsize

