nim = "38"  
two_last_digits = int(nim[-2:])

print("Deret angka dari 1 sampai 50 tanpa dua digit terakhir NIM:")
for i in range(1, 51):
    if i % 100 != two_last_digits:
        print(i, end=" ")
print()
