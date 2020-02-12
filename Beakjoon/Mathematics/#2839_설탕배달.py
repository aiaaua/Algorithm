sugar = int(input())
pkg = 0
while True:
    if sugar%5 == 0:
        pkg += sugar//5
        print(pkg)
        break
    sugar = sugar-3
    pkg += 1
    if sugar < 0:
        print("-1")
        break