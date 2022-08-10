from primefactors import primes
from primeslist import listOf1000Primes

print("THE LEAST COMMON MULTIPLE (LCM) CALCULATOR")

keepAsking = True
while keepAsking:
    LCMInputNumbers = input("Enter two or more integers to find the LCM (space-separated):\n")

    listOfLCMInputNumbers = LCMInputNumbers.split()

    for element in listOfLCMInputNumbers:
        if not element.isdigit():
            keepAsking = True
        else:
            keepAsking = False


listOfLCMInputNumbers = [int(i) for i in listOfLCMInputNumbers]

listOfLCMInputNumbers = list(dict.fromkeys(listOfLCMInputNumbers))


resultListOfPrimeFactors = []
primeFactorsDifference = 0

for k in listOfLCMInputNumbers:
    primeFactorsOfOneInputNumber = primes(k)
    for i in listOf1000Primes:
        primeFactorsDifference = primeFactorsOfOneInputNumber.count(i) - resultListOfPrimeFactors.count(i)
        if primeFactorsDifference > 0:
          for j in range(0, primeFactorsDifference):
            resultListOfPrimeFactors.append(i)


LCMResult = 1

for i in resultListOfPrimeFactors:
    LCMResult = LCMResult * i


print(f"The LCM of " + str(listOfLCMInputNumbers) + " is {:,}.".format(LCMResult))
