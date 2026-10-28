for i in range(1,6):
    nome = input(f"{i} nome: ")
    p1 = float(input("prova 01: "))
    p2 = float(input("prova 02: "))
    p3 = float(input("prova 03: "))
    md = (p1+p2+p3) /3
    if md >= 6:
        sit = "ap"
    elif md >= 6:
        sit = "rc"
    else:
        sit = "rp" 
    print("\n ------resultado------")
    print(f"aluno:{i}")       
    print(f"nome:{nome}")       
    print(f"prova 1: {p1}")       
    print(f"prova 2: {p2}")       
    print(f"prova 3: {p3}")       
    print(f"media: {md}")       
    print(f"situaçaõ: {sit}")       
    print("\n")       
