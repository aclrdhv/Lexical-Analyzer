
def create_stack():
    return []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        stack.pop()
    else:
        print("Stack is empty")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty")

def is_empty(stack):
    return len(stack) == 0


def doParser(arr_token):
    stack = create_stack()
    i = 0
    state = ""
    
    if "error" in arr_token:
        return False
    
    state = "i"
    push(stack,'#')
    state = "S"
    push(stack,'S')
    
    symbol = arr_token[i]
    top = peek(stack)

# <statement> ::= if <kondisi> : <aksi> else : <aksi> 
# <kondisi> ::= true | false | <variable> <operator_pembanding> <variable>
# <aksi> ::= <variable> = <variable> <operator_aritmatika> <variable> | <statement>
# <variable> ::= x | y | z
# <operator_pembanding> :: > | >=  | < | <=  |  == | !=
# <operator_aritmatika> ::= + | - | * | /
# Simbol non-terminal : 
# <statement> , <kondisi> , <aksi>, <variable>,  <operator_pembanding>, <operator_aritmatika>.
# Simbol terminal :
#  x, y, z, if, else, true, false, +, -, *, /, =, ==, >=, <=, <, >, !=, :

            
    while top != "#":
        # print("stack:",stack,"top:",top,"symbol:",symbol,"index:",i)
        if top == 'S':
            if symbol == "1":
                pop(stack)
                push(stack,"C")
                push(stack,"17")
                push(stack,"2")
                push(stack,"C")
                push(stack,"17")
                push(stack,"B")
                push(stack,"1")
            else:
                return False
            
        elif top == "B":
            if symbol == "3":
                pop(stack)
                push(stack,"3")
            elif symbol == "4":
                pop(stack)
                push(stack,"4")
            elif symbol == "5":
                pop(stack)
                push(stack,"D")
                push(stack,"E")
                push(stack,"D")
            else:
                return False
            
        elif top == "C":
            if symbol == "5": #D = D f D
                pop(stack)
                push(stack,"D")
                push(stack,"F")
                push(stack,"D")
                push(stack,"14")
                push(stack,"D")
            elif symbol == "1": #for nested
                pop(stack)
                push(stack,"S")
            else:
                return False
        
        elif top == "D":
            if symbol == "5":
                pop(stack)
                push(stack,"5")
            else:
                return False
        
        elif top == "E": # comparison
            if symbol == "6":
                pop(stack)
                push(stack,"6")
            elif symbol == "7":
                pop(stack)
                push(stack,"7")
            elif symbol == "8":
                pop(stack)
                push(stack,"8")
            elif symbol == "9":
                pop(stack)
                push(stack,"9")
            elif symbol == "15":
                pop(stack)
                push(stack,"15")
            elif symbol == "16":
                pop(stack)
                push(stack,"16")
            else:
                return False
        
        elif top == "F": 
            if symbol == "10":
                pop(stack)
                push(stack,"10")
            elif symbol == "11":
                pop(stack)
                push(stack,"11")
            elif symbol == "12":
                pop(stack)
                push(stack,"12")
            elif symbol == "13":
                pop(stack)
                push(stack,"13")
            else:
                return False
            
        # elif top == "G":
        #     if symbol == "11":
        #         pop(stack)
        #         push(stack,"11")
        #     elif symbol == "12":
        #         pop(stack)
        #         push(stack,"12")
        
        elif top == "1":
            if symbol != "1":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "2":
            if symbol != "2":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "3":
            if symbol != "3":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "4":
            if symbol != "4":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "5":
            if symbol != "5":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "6":
            if symbol != "6":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "7":
            if symbol != "7":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "8":
            if symbol != "8":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "9":
            if symbol != "9":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "10":
            if symbol != "10":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "11":
            if symbol != "11":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "12":
            if symbol != "12":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "13":
            if symbol != "13":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "14":
            if symbol != "14":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "15":
            if symbol != "15":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "16":
            if symbol != "16":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "17":
            if symbol != "17":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
        else:
            return False
        
        top = peek(stack)
    
    top = peek(stack)
    
    if top == "#":
        if symbol != "#":
            return False
            
        else:
            return True
    else:
        return False
