import re
import LexicalAnalyzer as LA
import Parser as parse

def splitter(sentence):
    pattern = r'(\w+|[<>=+/*-]+|:)'

    result = re.findall(pattern, sentence)
    return result

def invalid1():
    input = open("input_invalid1.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

def invalid2():
    input = open("input_invalid2.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

def invalid3():
    input = open("input_invalid3.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

def valid1():
    input = open("input_valid1.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

def valid2():
    input = open("input_valid2.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

def valid3():
    input = open("input_valid3.txt", "r").read()
    tokens = LA.lexyzer(splitter(input))
    print("tokens:",tokens)
    print(" ")
    hasilPARSE = parse.doParser(tokens)
    print("Hasil Parser")
    print("Inputan VALID karena sesuai dengan grammar") if hasilPARSE == True else print("Inputan INVALID karena tidak sesuai dengan grammar")

print("----------------------------Case Valid 1----------------------------")
valid1()
print("")
print("----------------------------Case Valid 2----------------------------")
valid2()
print("")
print("----------------------------Case Valid 3----------------------------")
valid3()
print("")
print("----------------------------Case Invalid 1----------------------------")
invalid1()
print("")
print("----------------------------Case Invalid 2----------------------------")
invalid2()
print("")
print("----------------------------Case Invalid 3----------------------------")
invalid3()