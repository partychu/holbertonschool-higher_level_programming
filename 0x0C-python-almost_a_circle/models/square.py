#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str repr"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))

    def update(self, *args, **kwargs):
        """Method: Update Square"""
        if len(args) != 0:
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            for arg in kwargs.values():
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Method: Square Dictionary"""
        return {"id": self.id,  "size": self.size,
                "x": self.x, "y": self.y}

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value
