from matplotlib import pyplot as plt

minutes = [ element for element in range(1, 10)]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Player1', 'Player2', 'Player3']

plt.style.use('fivethirtyeight')
plt.stackplot(minutes, player1, player2, player3, labels=labels)
plt.title('Stack Plot Of Employee Switch')
plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.savefig('plots/stackPlot.png')
plt.show()