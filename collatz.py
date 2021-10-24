import matplotlib.pyplot as plt

class collatz:
	def __init__(self, n):
		self.initial_n, self.n = n, n
	
	def __str__(self):
		return f"Current n = {self.n}"

	def __add__(self):
		return NotImplementedError

	def set(self, n):
		self.n = n
		return(self)

	def nr_iters_to_one(self, print_n = False):
		n = self.n

		if n == 0:
			print(f"nr_steps = 0\tn = {n}")
			return 0

		nr_steps = 0
		out = list()
		if print_n is True:
			print(f"nr_steps = {nr_steps}\tn = {n}")

		out.append(n)
		while n != 1:
			n = (n // 2) if n % 2 == 0 else (3 * n + 1)
			nr_steps += 1
			out.append(n)
			if print_n is True:
				print(f"nr_steps = {nr_steps}\tn = {n}")		
		
		if print_n is True:
			print(f"Needed {nr_steps} steps to reach 1")
		
		return out

def plot_sequence(n):
	c = collatz(n).nr_iters_to_one()
	plt.plot(c)
	plt.show()