# 1-misol
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}! Python dunyosiga xush kelibsiz!")

#2-misol
tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
yosh = 2026 - tugilgan_yil
print("Sizning yoshingiz:", yosh)

#3-misol
son = int(input("Biror son kiriting: "))

if son % 2 == 0:
    print("Bu son juft")
else:
    print("Bu son toq")

#4-misol
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

eng_katta = max(a, b, c)
print("Eng katta son:", eng_katta)

#5-misol
c = float(input("Selsiy darajasini kiriting: "))
f = (c * 9/5) + 32
print("Farengeyt:", f)
