# records = [['Harry', 37.21], ['kahrry', 37.2], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
records = [['chi', 20.0], ['Beta', 50.0], ['Alpha', 50.0]]

def takeSecond(elem):
    return elem[1]


records.sort(key=takeSecond)

lowest = records[0][1]
print(records)
second_lowest = 0
results = []

for i in records:
    if not i[1] == lowest:
        second_lowest = i[1]
        break

for i in records:
    if i[1] == second_lowest:
        results.append(i[0])
results.sort()
for i in results:
    print(i)