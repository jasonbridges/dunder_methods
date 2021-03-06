# Dunder Methods
1. Special methods in python that enable classes to be used in a pythonic way
2. Basics
  * Class instantiation
  ```python
  __new__(cls) # Useful for creating singletons
  ```
  * Class initialization
  ```python
  __init__(self, color) # Initializing instance variables after allocated by new
  ```
  * Operators
  ```python
  __add__(self, y) # x - y
  __radd__(self, y) # y - x
  __sub__(self, y) # x - y
  __rsub__(self, y) # y - x
  ```
  * builtin functions
  ```python
  __str__(self) # executed when str, print
  __repr__(self) # execute when repr or str, print without str defined
  ```
3. Play with hash and eq
# Demo
[Run python code live](http://www.pythontutor.com/live.html#mode=edit)

```python
#! /usr/bin/python
import random
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
            return {'blue': Color('purple') ,
                    'yellow' : Color('orange')}[color.color]

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

    def __eq__(self, other):
        return self.color is other.color

    def __hash__(self):
        #return 0
        return random.randint(1, 3)

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

    colors = {red : 'red', blue: 'blue', yellow: 'yellow'}

    print(repr(colors[red]))

```
```
red
red
Color('red')
purple
purple
Color('purple')
red
red
Color('red')
white
white
Color('white')
```
