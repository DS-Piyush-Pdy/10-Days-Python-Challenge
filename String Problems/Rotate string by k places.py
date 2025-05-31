s = input("Enter your string: ")
k = int(input("Enter how many positions to rotate: "))

k = k % len(s)

rotated = s[-k:] + s[:-k]

print("Rotated String:", rotated)
