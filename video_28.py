# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# 2. Menggunakan while

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir dari program")
# 3. hanya ganjil saja

print("awal program")
count = 1

while True:
    
    if (count%2):
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
 
print("akhir dari program")

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2181095959.
print("akhir dari program")
# 4. hanya ganjil saja

print("awal program")
count = 1
spasi = int(sisi/2)

while True:
    
    if (count%2):
        # Print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
 
print("akhir dari program")

#