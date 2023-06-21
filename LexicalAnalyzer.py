import FiniteAutomata as FA

def getTokens(kata):
    if FA.checkString(kata,'if') :
        return "1"
    elif FA.checkString(kata,'else'):
        return "2"
    elif FA.checkString(kata,'true'):
        return "3"
    elif FA.checkString(kata,'false'):
        return "4"
    elif FA.checkString(kata,'x'):
        return "5"
    elif FA.checkString(kata,'y'):
        return "5"
    elif FA.checkString(kata,'z'):
        return "5"
    elif FA.checkString(kata,'>'):
        return "6"
    elif FA.checkString(kata,'<'):
        return "7"
    elif FA.checkString(kata,'>='):
        return "8"
    elif FA.checkString(kata,'<='):
        return "9"
    elif FA.checkString(kata,'+'):
        return "10"
    elif FA.checkString(kata,'-'):
        return "11"
    elif FA.checkString(kata,'*'):
        return "12"
    elif FA.checkString(kata,'/'):
        return "13"
    elif FA.checkString(kata,'='):
        return "14"
    elif FA.checkString(kata,'=='):
        return "15"
    elif FA.checkString(kata,'!='):
        return "16"
    elif FA.checkString(kata,':'):
        return "17"
    else:
        return "error"

def lexyzer(strings):
    print("hasil split:",strings)
    hasil = []
    for kata in strings:
        hasil.append(getTokens(kata))
        
    hasil.append("#")
    
    return hasil