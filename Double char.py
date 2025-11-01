while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue

    result = ""
    for char in text:
        result += char * 2
    print(result)
