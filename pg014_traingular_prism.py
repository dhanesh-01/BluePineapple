import math
def volume_of_triangular_prism(a, b, c, h):
    # semi-perimeter
    s = (a + b + c) / 2
    
    # area of triangular base
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # volume
    volume = area * h
    return volume

print(("a, b, c → enter sides of the triangular base"))
a=int(input("a → "))
b=int(input("b → "))
c=int(input("c → "))
h=int(input("h height of the prism → "))
print("Volume of triangular prism is:", volume_of_triangular_prism(a, b, c,h))