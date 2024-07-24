class Teacher:
    def __init__(self, id="", name="", lastname="", hours=0, pph=0):  # pay per hour
        self._id = id
        self._name = name
        self._lastname = lastname
        self._hours = hours
        self._pph = pph

@property
def id(self):
    return self._id

@property
def name(self):
    return self._name

@property
def lastname(self):
    return self._lastname

@property
def hours(self):
    return self._hours

@hours.setter
def hours(self, value):
    if value > 0:
        self._hours = value
    else:
        self._hours = 0

@property
def pph(self):
    return self._pph

@pph.setter
def pph(self, value):
    if value > 0:
        self._pph = value
    else:
        self._pph = 0

def pay(self):
    return self._hours * self._pph

p = Teacher(123, 'fatemeh', 'chimeh', 170, 7000)
print(p.pay())