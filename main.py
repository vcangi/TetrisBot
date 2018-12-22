import sys

sys.path.append('./Game')
sys.path.append('./Game/Block Types')


from tetris import tetris

game = tetris()

game.runGame()
