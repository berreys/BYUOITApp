def main():
    valid = True
    while(valid):
        print("Would you like to convert")
        print("\"1\" = Roman Numeral to Decimal? or")
        print("\"2\" = Decimal to Roman Numeral? or")
        print("\"3\" = quit")
        input1 = int(input(""))

        if(input1 == 1):
            print("Please enter your Roman numeral:")
            inputRomanNumeral = input("")
            result = 0
            print(RNtoD(inputRomanNumeral, result))
            print()

        elif(input1 == 2):
            print("Please enter your integer:")
            inputDecimal = int(input(""))
            result = ""
            print(DtoRN(inputDecimal, result))
            print()
        
        elif(input1 == 3):
            break

        else:
            valid = False

def DtoRN(decimal, roman):
    print("INPUT:",decimal)
    if(decimal == 0):
        return ""


    hunRemainder = int(decimal % 1000 / 100)
    tenRemainder = int(decimal % 100 / 10)
    oneRemainder = int(decimal % 10)
    
    #THOUSANDS PLACE
    remainder = int(decimal / 1000)
    decimal %= 1000
    for i in range(remainder):
        roman += "M"
    
    #HUNDREDS PLACE
    if(hunRemainder == 9):
        roman += "CM" 
        roman = DtoRN(decimal - 900, roman)
        return roman

    if(hunRemainder == 4):
        roman += "CD" 
        roman = DtoRN(decimal - 400, roman)
        return roman
    if(hunRemainder > 4):
        roman += "D"
        roman = DtoRN(decimal - 500, roman)
        return roman
    else:
        for i in range(hunRemainder):
            roman += "C"
            decimal -= 100
        
    #TENS PLACE
    if(tenRemainder == 9):
        roman += "XC"
        roman = DtoRN(decimal - 90, roman)
        return roman
    if(tenRemainder == 4):
        roman += "XL"
        roman = DtoRN(decimal - 40, roman)
        return roman
    if(tenRemainder > 4):
        roman += "L" 
        roman = DtoRN(decimal - 50, roman)
        return roman
    else:
        for i in range(tenRemainder):
            roman += "X"
            decimal -= 10
    
    #ONES PLACE
    if(oneRemainder == 9):
        return roman + "IX"
    if(oneRemainder == 4):
        return roman + "IV"
    if(oneRemainder > 4):
        roman += "V"
        roman = DtoRN(decimal - 5, roman)
        return roman
    else:
        for i in range(oneRemainder):
            roman += "I"
        return roman

def RNtoD(roman, decimal):
    if(len(roman) == 0):
        return decimal
    if(len(roman) == 1):
        return decimal + getValue(roman)
    
    firstVal = getValue(roman[0])
    secondVal = getValue(roman[1])

    if(secondVal <= firstVal):
        return decimal + firstVal + RNtoD(roman[1:], decimal)
    
    return decimal + (secondVal - firstVal) + RNtoD(roman[2:], decimal)

def getValue(roman):
    if(roman == "I"): return 1
    if(roman == "V"): return 5
    if(roman == "X"): return 10
    if(roman == "L"): return 50
    if(roman == "C"): return 100
    if(roman == "D"): return 500
    if(roman == "M"): return 1000


main()