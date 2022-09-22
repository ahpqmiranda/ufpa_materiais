class structure:
    def __init__(self, dogbreed, dogeyecolor, name):
        self.name = dogbreed
        self.eyecolor = dogeyecolor
        self.name = name


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name


    def __eq__(self, other):
        return self.name == other.name


    def __hash__(self):
        
        return hash(self.name)