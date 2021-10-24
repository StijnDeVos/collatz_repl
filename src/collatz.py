import matplotlib.pyplot as plt

class collatz:
	def __init__(self, n):
		self.n = n
	
	def __str__(self):
		return f"Current n = {self.n}"

	def sequence(self):
		n = self.n

		if n == 0:
			print(f"nr_steps = 0\tn = {n}")
			return 0

		nr_steps = 0
		out = list()

		out.append(n)
		while n != 1:
			n = (n // 2) if n % 2 == 0 else (3 * n + 1)
			nr_steps += 1
			out.append(n)
		
		return out

def plot_sequence(n):
	c = collatz(n).sequence()
	max_value = max(c)
	max_ind = c.index(max_value)

	plt.plot(c, label='line & marker - no line because only 1 point')
	plt.plot(c.index(max_value), max_value, '-ro')
	plt.plot(len(c), 1, "-g", markersize=40)
	plt.text(
		max_ind + 1, 
		max_value + 1, 
		f"Maximum {max_value} at step {max_ind}", 
		bbox=dict(facecolor='red', alpha=0.2)
	)
	plt.axhline(y = 1, color = "grey", linestyle = "--")
	plt.xticks([])
	plt.yticks([])
	plt.title(f"Collatz sequence starting at {n}", horizontalalignment = "right")
	plt.axis('off')
	plt.show()