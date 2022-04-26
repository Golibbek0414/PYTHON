'''
print("begin 22")
a=int(input("a="))
b=float(input("b="))
a,b=b,a
print(f"{a}   {b}")

print("begin 23")
a=int(input("a="))
b=float(input("b="))
c=bool(input("c="))
a,b,c=c,a,b
print(f"a={a},b={b},c={c}")

print("begin 24")
a=str(input("a="))
b=list(input("b="))
c=tuple(input("c="))
a,b,c=b,c,a
print(f"a={a},b={b},c={c}")
print(type(a))
print(type(b))
print(type(c))

print("integer 6")
son=int(input("ikki xonali son kiriting ="))
print(son//10,son%10)

print("integer 7")
son=int(input("ikki xonali son kiriting ="))
print(son//10+son%10)

print("integer 8")
son=int(input("son="))
print(son%10,son//10)

print("integer 9")
son=int(input("uch xonali son kiriting ="))
print(son//100)

print("integer 10")
son= int (input("uch xonali son kiriting ="))
print(son//10%10)

print("integer 11")
son=int(input("son="))
print(son//100+son//10%10+son%10)

print("integer 12")
son=int(input("son="))
print(f"{son%10}{son//10%10}{son//100}")

print("integer 13")
son=int(input("son="))
print(f"{son//10%10}{son%10}{son//100}")

print("integer 14")
son=int(input("son="))
print(f"{son%10}{son//100}{son//10%10}")

print("integer 15")
son=int(input("son="))
print(f"{son//10%10}{son//100}{son%10}")

print("integer 16")
son=int(input("son="))
print(f"{son//100}{son%10}{son//10%10}")

print("integer 17")
son=int(input("uch xonli sondan katta son kiriting ="))
print(f"yuzlar xonasidagi son= {son//100%10}")

print("integer 18")
son=int(input("uch xonali sonda kattaroq son kiriting="))
print(f"minglar xonasida son= {son//1000%10}")

print("integer 23")
sekund=int(input("sekund kiriting: "))
print(f"{sekund//3600} soat {sekund%3600//60} minut {sekund%3600%60} sekund o'tdi")
'''
import numpy as np

screen_size = 40
theta_spacing = 0.07
phi_spacing = 0.02
illumination = np.array([*"......................."])
A = 1
B = 1
R1 = 1
R2 = 2
K2 = 5
K1 = screen_size * K2 * 3 / (8 * (R1 + R2))
def render_frame(A: float, B: float) -> np.ndarray:
    cosA = np.cos(A)
    sinA = np.sin(A)
    cosB = np.cos(B)
    sinB = np.sin(B)
    output = np.full((screen_size, screen_size), " ")
    zbuffer = np.zeros((screen_size, screen_size))
    cosphi = np.cos(phi := np.arange(0, 2 * np.pi, phi_spacing))  # (315,)
    sinphi = np.sin(phi)  # (315,)
    costheta = np.cos(theta := np.arange(0, 2 * np.pi, theta_spacing))  # (90,)
    sintheta = np.sin(theta)  # (90,)
    circlex = R2 + R1 * costheta  # (90,)
    circley = R1 * sintheta  # (90,)
    x = (np.outer(circlex, cosB * cosphi + sinA * sinB * sinphi).T - circley * cosA * sinB).T  
    y = (np.outer(circlex, sinB * cosphi - sinA * cosB * sinphi).T + circley * cosA * cosB).T  
    z = ((K2 + cosA * np.outer(circlex, sinphi)).T + circley * sinA).T  
    ooz = np.reciprocal(z)  # Calculates 1/z
    xp = (screen_size / 2 + K1 * ooz * x).astype(int)  
    yp = (screen_size / 2 - K1 * ooz * y).astype(int)  
    L1 = (((np.outer(cosphi, costheta) * sinB).T - cosA * np.outer(costheta, sinphi)).T - sinA * sintheta).T  
    L2 = cosB * (cosA * sintheta - np.outer(costheta * sinA, sinphi).T).T  
    L = np.around(((L1 + L2) * 8)).astype(int)  
    mask_L = L >= 0  
    chars = illumination[L]  
    for i in range(90):
        mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])  # (315,)
        zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
        output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])
    return output
def pprint(array: np.ndarray) -> None:
    """Pretty print the frame."""
    print(*[" ".join(row) for row in array], sep="\n")
if name == "main":
    for _ in range(screen_size * screen_size):
        A += theta_spacing
        B += phi_spacing
        print("\x1b[H")
        pprint(render_frame(A, B))