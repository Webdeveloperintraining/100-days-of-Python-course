# Write your code below this line 👇

def prime_checker(number):
  for i in range(1,101):
    if i != 1:
      if number % i == 0 and i != number:
        return print("It's not a prime number.")
  print('It\'s a prime number.')

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)