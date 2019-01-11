# These test cases make the assumption that the compute_triangular_form() method
# operates according to the following rules:
#   1. Swap with topmost row below current row
#   2. Don't multiply row by numbers
#   3. Only add a multiple of a row to rows underneath

from decimal import Decimal, getcontext
from vector import Vector
from plane import Plane
from linsys import LinearSystem

getcontext().prec = 30

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
        r[1] == p2):
    print('test case 1 failed')
else:
    print('test case 1 passed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(constant_term='1')):
    print('test case 2 failed')
else:
    print('test case 2 passed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
        r[1] == p2 and
        r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
        r[3] == Plane()):
    print('test case 3 failed')
else:
    print('test case 3 passed')

p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
s = LinearSystem([p1,p2,p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
        r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
        r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
    print('test case 4 failed')
else:
    print('test case 4 passed')
