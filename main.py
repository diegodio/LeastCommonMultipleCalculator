from primefactors import primes
from primeslist import LIST_OF_1000_PRIMES

print("THE LEAST COMMON MULTIPLE (LCM) CALCULATOR")
valid_input = False
while not valid_input:
    lcm_input_numbers = input(
        "Enter two or more integers to find the LCM (space-separated):\n"
        )

    list_of_lcm_input_numbers = lcm_input_numbers.split()

    for element in list_of_lcm_input_numbers:
        if not element.isdigit():
            valid_input = False
        else:
            valid_input = True

list_of_lcm_input_numbers = [int(i) for i in list_of_lcm_input_numbers]
list_of_lcm_input_numbers = list(dict.fromkeys(list_of_lcm_input_numbers))
result_list_of_prime_factors = []
prime_factors_difference = 0

for k in list_of_lcm_input_numbers:
    prime_factors_of_one_input_number = primes(k)
    for i in LIST_OF_1000_PRIMES:
        prime_factors_difference = (prime_factors_of_one_input_number.count(i)
                                   - result_list_of_prime_factors.count(i))
        if prime_factors_difference > 0:
          for j in range(0, prime_factors_difference):
            result_list_of_prime_factors.append(i)

lcm_result = 1

for i in result_list_of_prime_factors:
    lcm_result = lcm_result * i

print(f"The LCM of "
      + str(list_of_lcm_input_numbers)
      + " is {:,}.".format(lcm_result))
