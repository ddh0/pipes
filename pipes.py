# Python 3.8.2
# Written by Dylan Halladay

class EmptyPipeline(Exception):
    """Error thrown when .get() is called on an empty Pipeline object"""
    pass

class Pipeline:
    """A class for sending and recieving data
       in a queue."""

    class PipeObject:
        """Used for ordering items in the pipeline array.

           Changing the .FIFO attribute may cause unexpected behaviour."""

        def __init__(self, pos, data):
            """Give the object a position and contents."""
            self.pos = int(pos)
            self.data = data

    def __init__(self, mode="FIFO"):
        if mode.upper() == "FIFO":
            self.FIFO = True

        elif mode.upper() == "LIFO":
            self.FIFO = False

        else:
            raise ValueError("Keyword argument 'mode' must be 'FIFO' or 'LIFO'.")

        self.last_pos = 0    # Most recently filled position
        self.array = []      # Holds PipeObjects
        self.positions = []  # All positions currently filled

    def add(self, data):
        """Place an object into the pipeline."""

        pos = len(self.array) + 1

        self.last_pos = pos
        obj = self.PipeObject(pos, data)

        if pos in self.positions:
            raise IndexError("An object with that position aleady exists in this Pipeline")

        else:
            self.array.append(obj)
            self.positions.append(pos)

        self.array = sorted(self.array, key=lambda x: x.pos)

    def get(self):
        """Get the next object from the queue."""

        if len(self.array) < 1:
            raise EmptyPipeline

        if not self.FIFO:
            item = self.array.pop()        # Remove and return last item
        else:
            item = self.array[::-1].pop()  # Same, but with reversed list
            self.array.remove(item)

        if item.pos not in self.positions:
            raise IndexError("This item's position is no longer in the Pipeline")
        else:
            self.positions.remove(item.pos)  # Remove from position list

        return item.data

    def flush(self):
        """Reset the Pipeline to it's original state."""

        self.last_pos = 0    # Most recently filled position
        self.array = []      # Holds PipeObjects
        self.positions = []  # All positions currently filled
