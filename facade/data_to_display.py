class circle_show:
    def __init__(self, root):
        self.root = root

    def image(self):
        root = self.root
        circle = root.create_oval(int(root['width'])/2 - 25,
                                  int(root['height'])/2 - 25,
                                  int(root['width'])/2 + 25,
                                  int(root['height'])/2 + 25,
                                  fill='black')
        return circle

class square_show:
    def __init__(self, root):
        self.root = root

    def image(self):
        root = self.root
        square = root.create_rectangle(int(root['width'])/2 - 25,
                                  int(root['height'])/2 - 25,
                                  int(root['width'])/2 + 25,
                                  int(root['height'])/2 + 25,
                                  fill='black')
        return square
