from blackJack import Game

def start():
	game = Game()
	result = game.run()
	return result


if __name__ == "__main__":
	sum = 200
	for i in range(1):
		game = Game()
		result = game.run()
		sum = sum + result

	print('Final ',sum)