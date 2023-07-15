from ..math.simple_attributes import Simple_Attributes

class Element():

    def __init__(self, name):
        self.name = name
        self.attributes = Simple_Attributes()
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        if not isinstance(other, Element):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
