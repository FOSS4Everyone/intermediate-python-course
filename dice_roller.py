def main():
  import random
  dice_rolls = int(input('how many dice would you like to roll?'))
  dice_size = int(input('how many sides are the dice'))
  dice_sum = 0
  for i in range(0,dice_rolls): #"for every index in a range starting after 0 until the value is equal to dice_rolls, do this:"
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll
    if roll == 1:
        print(f'you rolled a {roll}! critical fail')
    elif roll == dice_size:
        print(f'your rolled a {roll}! congrats')
    else:
        print(f'you rolled a {roll}')
  print(f"You rolled a total of {dice_sum}")

if __name__== "__main__":
  main()