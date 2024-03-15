two_last_digits = int(input("Dua digit terakhir dari NIM : "))

for i in range(1, 51):
    if i % 100 != two_last_digits:
        print(i, end=" ")
print()
