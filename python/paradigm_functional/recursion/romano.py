#Develop a function that allows you to convert
#a Roman numeral into a decimal number.

def romanoADecimal(romano):
    if len(romano) == 0:
        return 0
    else:
        if romano[0] == 'I':
            return 1 + romanoADecimal(romano[1:])
        if romano[0] == 'V':
            return 5 + romanoADecimal(romano[1:])
        if romano[0] == 'X':
            return 10 + romanoADecimal(romano[1:])
        if romano[0] == 'L':
            return 50 + romanoADecimal(romano[1:])
        if romano[0] == 'C':
            return 100 + romanoADecimal(romano[1:])
        if romano[0] == 'D':
            return 500 + romanoADecimal(romano[1:])
        if romano[0] == 'M':
            return 1000 + romanoADecimal(romano[1:])
        
print(romanoADecimal('XXVI')) #10
