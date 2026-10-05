vardnica={
    'a' : 1,
    'ā' : 2,
    'e' : 1,
    'i' : 1,
    'r' : 1,
    's' : 1,
    't' : 1,
    'b' : 4,
    'd' : 3,
    'c' : 4,
    'g' : 4,
    'k' : 2,
    'l' : 2,
    'm' : 2,
    'n' : 2,
    'o' : 2,
    'p' : 2,
    'u' : 2,
    'v' : 4,
    'z' : 3,
    'ē' : 3,
    'ī' : 3,
    'ļ' : 5,
    'ņ' : 8,
    'š' : 8,
    'ž' : 10,
    'f' : 8,
    'h' : 8,
    'ķ' : 10,
    'ū' : 3,
    '' : 0,
    'č' : 10,
    'ģ' : 10,
    'j' : 5
}
vards=input("Īevadi savu vardu :")
def parbaudit(word):
    summa = 0
    for burts in word:
        if burts in vardnica.keys():
           summa+=vardnica[burts]
    return summa

rezultats = parbaudit(vards)          

print(f"Par šo vardu jums ir {rezultats} punkti")