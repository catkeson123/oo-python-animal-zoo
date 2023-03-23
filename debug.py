import ipdb
from lib.animal import *
from lib.zoo import *

# code here

# e.g.
z1 = Zoo('Micke Grove Zoo', 'Lodi, CA')
z2 = Zoo('The Bronx Zoo', 'The Bronx')
z3 = Zoo('The Bronx Zoo 2.0', 'The Bronx')

a1 = Animal('Lion', 75, 'Luke', z1)
a2 = Animal('Tiger', 120, 'Tom', z1)
a3 = Animal('Tiger', 130, 'Tony', z2)
a4 = Animal('Lion', 70, 'Lea', z2)
a5 = Animal('Tiger', 150, 'Chunk', z2)
a6 = Animal('Rhino', 300, 'Big', z1)
a7 = Animal('Elephant', 500, 'Biggums', z3)


# do not remove
ipdb.set_trace()
