#userNumber = 5
#userNumber = float(input("What is your number?"))
# 1 in = 25.4 mm
# Conver from in to mm
#   userNumber *25.4 mm = converted number

# convertedNumber = userNumber * 25.4
# convertedString = "{0:.4f}in is {1:.4f}mm"
# print (convertedString.format(userNumber, convertedNumber))

# #reversed
# convertedNumber = userNumber / 25.4
# convertedString = "{0:.4f}mm is {1:.4f}in"
# print (convertedString.format(userNumber, convertedNumber))

#Combined
userConversionType = int(input('type 1 for Inches to mm or type 2 mm to inches?'))
userNumber = float(input("What is your number?"))

#1 = in to mm; 2 = mm to in
if userConversionType == 1:
    convertedNumber = userNumber * 25.4
    convertedString = "{0:.4f}mm is {1:.4f}in"

#2 = mm to in
if userConversionType == 2:
    convertedNumber = userNumber / 25.4
    convertedString = "{0:.4f}in is {1:.4f}mm"


print (convertedString.format(userNumber, convertedNumber))
