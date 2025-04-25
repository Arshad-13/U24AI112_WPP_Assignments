# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.

# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.

class RPS:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.player_wins = 0
        self.computer_wins = 0
        
    def get_computer_choice(self):
        import random
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'
        elif player_choice == 'rock':
            if computer_choice == 'scissors':
                return 'player'
            else:
                return 'computer'
        elif player_choice == 'paper':
            if computer_choice == 'rock':
                return 'player'
            else:
                return 'computer'
        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                return 'player'
            else:
                return 'computer'
            
    def check_game_over(self):
        if self.player_wins == self.rounds:
            return 'player'
        elif self.computer_wins == self.rounds:
            return 'computer'
        else:
            return None
    
    def play_round(self, player_choice):
        computer_choice = self.get_computer_choice()
        winner = self.find_winner(player_choice, computer_choice)
        if winner == 'player':
            self.player_wins += 1
        elif winner == 'computer':
            self.computer_wins += 1
        self.current_round += 1
        return winner
        
    def play_game(self):
        while True:
            player_choice = input("Enter your choice (rock, paper, scissors): ")
            winner = self.play_round(player_choice)
            if winner == 'tie':
                print("It's a tie!")
            elif winner == 'player':
                print("You win the round!")
            elif winner == 'computer':
                print("The computer wins the round!")
            if self.check_game_over() is not None:
                break
        if self.check_game_over() == 'player':
            print("You win the game!")
        elif self.check_game_over() == 'computer':
            print("The computer wins the game!")
        else:
            print("The game is a tie!")

def main():
    x = int(input("Enter how many rounds for win: "))
    game = RPS(x)
    game.play_game()
    
    
if __name__ == "__main__":
    main()