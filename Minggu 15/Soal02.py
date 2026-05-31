def palidrom(text):
    text = text.replace(" ", "").lower()

    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False
    
    return palidrom(text[1:-1])

#Test Case
print(palidrom("A man a plan a canal Panama"))
print(palidrom("Ini ibu Budi"))
print(palidrom("Katak"))
print(palidrom("Kasur Rusak"))
print(palidrom("B"))