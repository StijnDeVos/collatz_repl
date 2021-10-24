from collatz import collatz
import matplotlib.pyplot as plt

def plot_sequence(n):
	c = collatz(n).nr_iters_to_one()

	x = list(range(len(c)))

	plt.plot(c)
	plt.show()

