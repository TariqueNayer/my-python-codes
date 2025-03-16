
class Rectangle:
    def __init__(self, wid, hit):
        self.width = wid
        self.height = hit

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, wid):
        self.width = wid
    def set_height(self, hit):
        self.height = hit
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (((self.width**2) + (self.height**2)) ** 0.5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        output = ''
        for line in range(self.height):
            for dot in range(self.width):
                output += '*'
            output += '\n'
        return output

    def get_amount_inside(self, other):
        fh = self.height // other.height
        fw = self.width // other.width
        return fh * fw
        
        

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side,side)

    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'
    def set_side(self, s):
        self.side = s
        self.width = s
        self.height = s
    def set_width(self, wid):
        self.set_side(wid)
    def set_height(self, hit):
        self.set_side(hit)

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    sq.set_width(8)
    print(sq.height)
    print(rect.get_amount_inside(sq))
