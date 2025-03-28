result = []

def divider(a, b):
    if a < b:
        raise ValueError("a має бути більшим за b")
    if b > 100:
        raise IndexError("b не може бути більшим за 100")
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as a:
        print(type(a),"---", a)

print("Результат: ", result)