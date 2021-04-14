def main():
  import random
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls): #"for every index in a range starting after 0 until the value is equal to dice_rolls, do this:"
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    print(f'you rolled a {roll}')
  print(f"You rolled a total of {dice_sum}")

if __name__== "__main__":
  main()