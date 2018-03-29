#! /usr/bin/python
"""
Code for a presentation on dunder method basics
"""

class Color:
    _primary_colors = ['red', 'yellow', 'blue']
    _secondary_colors = ['orange', 'green', 'purple']

    _instance = None
    
    def __new__(cls, color):
        return super(Color, cls).__new__(cls)

        # Singleton
        if not cls._instance:
            cls._instance = super(Color, cls).__new__(cls)
        return cls._instance



    def __init__(self, color):

        if color in Color._primary_colors:
            self.color = color
        elif color in Color._secondary_colors:
            self.color = color
        elif color is 'white':
            self.color = 'white'
        else:
            self.color = 'black'

    def __str__(self):
        return self.color

    def __repr__(self):
        return "Color('{}')".format(self.color)

    def __add__(self, color):
        if self.color is color.color:
            return Color(self.color)

        if self.color is 'red':
            if color.color is 'blue':
                return Color('purple')
            elif color.color is 'yellow':
                return Color('orange')

        elif self.color is 'blue':
            if color.color is 'red':
                return Color('purple')
            elif color.color is 'yellow':
                return Color('green')

        elif self.color is 'yellow':
            if color.color is 'blue':
                return Color('green')
            elif color.color is 'red':
                return Color('orange')
        else:
            return Color('black')

    def __sub__(self, color):
        if self.color is color.color:
            return Color('white')

        if self.color in Color._primary_colors and color.color in Color._primary_colors:
            return Color(self.color)

        if self.color in Color._secondary_colors:
            if self.color is 'orange':
                if color.color is 'yellow':
                    return Color('red')
                elif color.color is 'purple':
                    return Color('red')
                elif color.color is 'red':
                    return Color('yellow')
                elif color.color is 'green':
                    return Color('red')
                elif color.color is 'blue':
                    return Color('orange')

            elif self.color is 'green':
                if color.color is 'yellow':
                    return Color('blue')
                elif color.color is 'purple':
                    return Color('yellow')
                elif color.color is 'red':
                    return Color('green')
                elif color.color is 'orange':
                    return Color('green')
                elif color.color is 'blue':
                    return Color('yellow')

            elif self.color is 'purple':
                if color.color is 'yellow':
                    return Color('purple')
                elif color.color is 'green':
                    return Color('yellow')
                elif color.color is 'red':
                    return Color('blue')
                elif color.color is 'orange':
                    return Color('blue')
                elif color.color is 'blue':
                    return Color('red')
        else:
            return Color('white')

if __name__ == "__main__":
    red = Color('red')
    blue = Color('blue')
    yellow = Color('yellow')

    print(red)
    print(str(red))
    print(repr(red))

    print(red + blue)
    print(str(red + blue))
    print(repr(red + blue))

    print(red + blue - yellow - blue)
    print(str(red + blue - yellow - blue))
    print(repr(red + blue - yellow - blue))

    print(red + blue - yellow - blue - red)
    print(str(red + blue - yellow - blue - red))
    print(repr(red + blue - yellow - blue - red))
