# Klassendefinition
class Person():
     # Konstruktor mit Parametern (teils mit Default- Args)
     def __init__(self, name, age=0, sex=""):
          self.name = name
          self.alter = age
          self.sex = sex
          # Methoden können schon im Konstruktor aufgerufen werden
          self.Atmen()
     # Weitere Methoden der Klasse
     def Atmen(self):
          print("Schnauf")
     def Geburtstag(self):
          self.alter +=1
     def __add__(self, other): # Operator +
          return (self.alter + other.alter)/2
     def __gt__(self,other):   # Operator  >
          return self.alter > other.alter
     # Der Operator "<" muss tatsächlich nicht definiert 
     # werden, wenn ">" schon definiert wurde. Der Interpreter 
     # leitet sich diesen Zusammenhang selbst ab. Wir machen es 
     # aber trotzdem: 
     def __lt__(self,other):   # Operator  <
          return self.alter < other.alter

         
Stefan = Person("Stefan", 55, "m") # wird instanziiert und atmet (Zeile 9!)
Stefan.name = "Stefan"
print(Stefan.name, Stefan.alter)
Stefan.Atmen()

# Definition einer abgeleiteten (erbenden) Klasse
# Diese hat alle Attribute und Methoden der 
# vererbenden Klasse Person, überschreibt aber die
# Methode Atmen() und das Attribut 'sex'
class Mann(Person):
    def __init__(self, name, age):
        super().__init__(name, age, sex="m")
    def Atmen(self):
        print("Schnuff") 

Wasim = Mann("Wasim", 30)
print(Wasim.name, Wasim.sex)
Wasim.Atmen()
# Wasim hat Geburtstag und wird ein Jahr älter
Wasim.Geburtstag()
print(Wasim.alter)

print("Durchschnittsalter:",Wasim + Stefan)

# Das Atribut 'name' ist das einzige Pflichtargument 
Baby1 = Person("Schrödinger")
print(Baby1.name, Baby1.alter, Baby1.sex)

# Die anderen Parameter müssen nicht argumentiert werden
Baby2 = Person("Attila", sex = "m")
print(Baby2.name, Baby2.sex)

Baby3 = Person("Merlin", age=300)
print(Baby2.name, Baby2.alter) 