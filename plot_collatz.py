from collatz import collatz
import matplotlib.pyplot as plt

def plot_sequence(n):
	c = collatz(n).nr_iters_to_one()
	plt.plot(c)
	plt.show()

