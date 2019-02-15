class Stack(list):
    """Stack implemented as a list. Top of the stack is the end of the list."""
    def __init__(self, content):
        list.__init__(self) # initialize this as a list
        self.add(content)

    def add(self, content):
        """Add an item or multiple to the stack."""
        if type(content) is list:
            self.extend(content)
        else:
            # does not support a stack of lists
            self.append(content)

    def view_top(self):
        """View the item at the top of the stack without removing it."""
        return self[-1]