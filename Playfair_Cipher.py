def playfair_cipher():  
    #Input phrases with replacement of J for I
    phrase = input("Enter phrase: ").upper()  
    key = input("Enter key for phrase (letters only): ").upper()   

    if " " in phrase or " " in key: 
        phrase = phrase.replace(" ", "")   
        key = key.replace(" ", "")

    if "J" in phrase or "J" in key: 
        phrase = phrase.replace("J", "I") 
        key = key.replace("J", "I") 

    ls = [] 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    key += alphabet 
    ls += key   
    matrix = []
    for i in ls: 
        if i not in matrix: 
            matrix.append(i)   

    matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]   
    # reference https://www.geeksforgeeks.org/python/python-program-to-construct-nm-matrix-from-list/ 

    pairs = []
    i = 0
    while i < len(phrase):
        a = phrase[i]
        if i + 1 < len(phrase):
            b = phrase[i+1]
            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "X")
            i += 1 
    # reference https://www.nashruddinamin.com/blog/playfair-cipher-in-python
    # finding letters function
    def find_pos(letter):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c

    # encrypt
    cipher = ""
    for p in pairs:
        r1, c1 = find_pos(p[0])
        r2, c2 = find_pos(p[1])

        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]  

    print("Encrypted:", cipher)

    # decrypt
    decrypted = "" 
    i = 0
    while i < len(cipher):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_pos(a)
        r2, c2 = find_pos(b)

        if r1 == r2:
            decrypted += matrix[r1][(c1-1) % 5]
            decrypted += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            decrypted += matrix[(r1-1) % 5][c1]
            decrypted += matrix[(r2-1) % 5][c2]
        else:
            decrypted += matrix[r1][c2]
            decrypted += matrix[r2][c1]

        i += 2

    print("Decrypted:", decrypted)

playfair_cipher()