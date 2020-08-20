#fungsi biasa
def hello():
    print ("Hello ini Fungsi")
hello()

#fungsi dengan parameter
def salam(ucapan):
    print(ucapan)
salam("selamat sore")

#fungsi dengan return

def kuadrat(argument):
    total = argument**2
    print("nilai kuadrat dari ", argument, 'adalah', total)
    return total

hasil= kuadrat(3)
print(hasil)

def angka(n, m):
    total = n + m
    return total

hasil = angka(7, 10)
print(hasil)

def jumlah(angka):
    nilai = angka
    if 80 <= nilai <= 100:
        print("nilai anda adalah A")
    elif 70 <= nilai < 80:
        print("nilai anda adalah B")
    elif 60 <= nilai < 70:
        print("nilai anda adalah C")
    elif 50 <= nilai < 60:
        print("nilai anda adalah D")
    else :
        print("anda GAGAL")
    return nilai
print(jumlah(80)) 