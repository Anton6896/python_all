class Bitmap:
    def __init__(self, name) -> None:
        self.name = name
        print('Loading >> Loading')

    def draw(self):
        print(f'drawing some image : {self.name}')

class LazyImage(Bitmap):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.bitmap: Bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.name)
        self.bitmap.draw()

def draw_image(image: Bitmap):
    print('before draw image')
    image.draw()
    print('after draw image')

if __name__ == '__main__':
    # only one load for image data

    bp = LazyImage('some.name.pp')
    draw_image(bp)
    draw_image(bp)