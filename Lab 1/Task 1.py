numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

for i in range(len(numbers)):
    if numbers[i] is None:
        miss: int = i

sr = (sum(numbers[0:miss])+sum(numbers[5:]))/len(numbers)
numbers[4] = sr
print("Измененный список:", numbers)
