import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play_again = True

while play_again:
    print("Play rock paper scissors with the computer!!\n")
    
    #Select option from user
    print("1. Rock\n2. Paper\n3. Scissors")
    user_option = int(input("Choose your option: ")) - 1  

    
    choices = [rock, paper, scissors]

    #Generate a random number to select the choice of the computer
    comp_option = random.randint(0, 2)

    #Display choices of both players
    print("\nYour Choice:\n")
    print(choices[user_option])
    print("\nComputer's Choice:\n")
    print(choices[comp_option])

    #Implement the logic to choose the winner
    if user_option == comp_option:
        print("\nDraw!!")
    elif (user_option - comp_option) % 3 == 1:
        print("\nYou win!!")
    else:
        print("\nComputer wins!!")
    
#Ask user if they wish to play again
    play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again_input != 'yes':
        play_again = False

print("\nThanks for playing!")
