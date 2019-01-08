import sys
sys.path.append('./Game')
sys.path.append('./Game/Block Types')

from tetris import Tetris

game = Tetris()

game.run_game()
