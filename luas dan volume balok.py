print(f"{'PROGRAM UNTUK  MENGHITUNNG LUAS & VOLUME BALOK':^50}")
print(f"{'='*50 : ^50}")

p = int(input("Masukkan Panjang Balok : "))
l = int(input("Masukkan Lebar Balok   : "))
t = int(input("Masukkan Tinggi Balok  : "))

#menghitung luas permukaan
def luas_permukaan(p,l,t):
    L = 2 * ((p*1) + (p*t) + (l*t))
    return L

#menghitung volume balok
def volume_balok(p,l,t):
    V = p * l * t
    return V

print(f"{'='*50:^50}")
print(f"{'LUAS & VOLUME BALOK':^50}")
print(f"{'='*50:^50}")

print(f"Panjang Balok : {p}")
print(f"Lebar Balok   : {l}")
print(f"Tinggi Balok  : {t}")

print(f"Luas Balok    : {luas_permukaan(p,l,t)}")
print(f"Volume Balok  : {volume_balok(p,l,t)}")
