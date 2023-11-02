#home work
#level 1
#1, #2
transports = ["car", "bus", "bike", "train", "plane"]
#3
print(len(transports))
#4
print(transports[0]) #первый элемент
print(transports[2]) #средний элемент
print(transports[4]) #последний элемент
#5
mixed_data_types = ["Zhanibek", 15, 171, "all right", "Карабулак 2"]
#6
companies = ["facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"]
#7
print(companies)
#8
print(len(companies))
#9
print(companies[0]) #первый элемент
print(companies[3]) #средний элемент
print(companies[6]) #последний элемент
#10
companies[2] = "samsung "
print(companies)
#11
# companies.append("IT company")
# print(companies)
#12
companies.insert(3, "IT company")
print(companies)
#13
companies = ["facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"]
print(companies[5].upper())
#14
companies = ["facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"]
#15
print("rebmi" in companies)
#16
companies.sort()
print(companies)
#17
companies.reverse()
print(companies)
#18
print(companies[:3])
#19
print(companies[-3:])
#20
companies.pop(3)
print(companies)
#21
del companies[0]
print(companies)
#22
companies.remove("apple")
print(companies)
#23
companies.remove("IBM")
print(companies)
#24, #25
companies.clear()
print(companies)
#26
#27
#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]
print(ages)
#1
min = min(ages) #минимальный возраст
print(min)
max = max(ages) #максимальный возраст
print(max)


