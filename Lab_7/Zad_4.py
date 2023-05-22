from Zad_1 import Stack

def ONP(działanie):
    s = Stack()
    index = 0
    while index<len(działanie)-1:
        symbol = działanie[index]
        if symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/" and symbol!="^":
            s.push(int(symbol))
            index = index+1
        else:
            pierwsza = s.pop()
            druga = s.pop()
            if symbol == "+":
                w = druga+pierwsza
                s.push(w)
            elif symbol=="-":
                w = druga-pierwsza
                s.push(w)
            elif symbol=="*":
                w = druga*pierwsza
                s.push(w)
            elif symbol=="/":
                w = druga/pierwsza
                s.push(w)
            elif symbol=="^":
                w = druga**pierwsza
                s.push(w)

            index=index+1
    return s.pop()

print(ONP("73+52-2^*="))
