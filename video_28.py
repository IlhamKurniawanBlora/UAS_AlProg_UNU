# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For
print("awal dari program 1")

# dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("akhir dari program 1")

# 2. Menggunakan while
print("awal dari program 2")

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir dari program 2")
# 3. hanya ganjil saja

print("awal program 3")
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
 
print("akhir dari program 3")
# 4. hanya ganjil saja

print("awal program 4")
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
 
print("akhir dari program 4")
