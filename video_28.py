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
