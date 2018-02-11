
class Calculatrice:

    def __init__(self, a, b):

       self.ina = a;
       self.inb = b;

    def add(self):
        return self.ina + self.inb

    def mult(self):
        return  self.ina * self.inb


Calc = Calculatrice(10, 4)

print 'Resultat addition : %d' %Calc.add()
print 'Resultat multiplication %d ' %Calc.mult()