class Client:
    def __init__(self, n, f):
        self._name = n
        self._telephone = f

    #Method get
    def get_name(self):
        return self._name
    
    #Method set
    def set_name(self, name):
        self._name = name