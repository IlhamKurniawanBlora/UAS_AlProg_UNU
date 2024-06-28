# continue, pass, break
#pass dia berfungsi sebagai dummy, tidak akan melakukan aksi apapun

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak akan dieksekusi

    print(angka)

#continue

angka = 0

print(f"angka sekarang {angka}")

while angka < 5:        
    angka += 1
    print(f"angka sekarang --> {angka}") #aksi I

    if angka == 3:                 
        print("nice!")
        continue # ini akan membuat loop meloncat 

    print("whassup!") # aksi 2

print("Pinish!")

