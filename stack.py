"""Stack implemented as a linked list"""

class Item(object):
    """The items that go in the stack. They only know about the next item and their own content."""
    def __init__(self, content=None, below=None):
        self.content = content
        self.below = below


class Stack(object):
    """Stack object. First in first out implemented as a linked list."""
    def __init__(self, items=None):
        # items should be a list of content attributes
        self.top = None
        try:
            for item in items:
                self.add(item)
        except TypeError:
            # if passed a non-iterable
            self.add(items)
    
    def add(self, content):
        """Adds an item to the stack"""
        new = Item(content)
        if self.top is None:
            self.top = new
        else:
            new.below = self.top
            self.top = new      

    def pop(self):
        """Removes an item from the top of the stack and returns it."""
        target = self.top
        try:
            below_item = self.top.below
            self.top = below_item
            return target
        except AttributeError:
            raise AttributeError("Stack is empty.")