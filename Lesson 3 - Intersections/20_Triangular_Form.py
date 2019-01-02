# These test cases make the assumption that the compute_triangular_form() method
# operates according to the following rules:
#   1. Swap with topmost row below current row
#   2. Don't multiply row by numbers
#   3. Only add a multiple of a row to rows underneath

from vector import Vector
from plane import Plane
from linsys import LinearSystem

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print('test case 1 failed')
else:
    print('test case 1 passed')

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print('test case 2 failed')
# else:
#     print('test case 2 passed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
s = LinearSystem([p1,p2,p3,p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
        t[3] == Plane()):
    print('test case 3 failed')
else:
    print('test case 3 passed')

# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print('test case 4 failed')
# else:
#     print('test case 4 passed')
