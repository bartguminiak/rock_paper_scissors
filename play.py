from game import Game

def main():
    cmd = input('Do you want to start the rock, paper, scissors game? [y/n] ')
    if cmd == 'y':
        game = Game()
        roundCount = 0
        print("Let's start the game 🔥")
        print("------------------------------------------")
        while game.isGameOn:
            roundCount += 1
            result = game.fight()
            nameResult = ""
            if result == -1:
                nameResult = "You lost :("
            if result == 0:
                nameResult = "Draw"
            if result == 1:
                nameResult = "You Win!"
            print("round {} -> ".format(roundCount) + game.player.name + "(me) VS " + game.opponent.name)
            print(nameResult + " result: " + str(game.currentScore))
            if game.isGameOn:
                input('next round?')

        print("------------------------------------------")
        print("Congratulations YOU WON! 🤑🏅🥳" if game.currentScore == 3 else "GAME OVER - You lost 😭")
    else:
        print("Good bye")

if __name__ == '__main__':
    main()