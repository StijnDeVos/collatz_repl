from collatz import collatz, plot_sequence
from colorama import Fore, init

init(autoreset = True)

even = lambda n: f"{Fore.GREEN}{n}"
odd = lambda n: f"{Fore.RED}{n}"
check_color = lambda n: even(n) if n % 2 == 0 else odd(n)

def parse_input(n):
	try:
		n = int(n)
	except Exception as e:
		if n == "plot":
			print("Plot functionality coming soon.")
		print(f"Error: {e}")
	else:
		if n <= 0:
			print("Collatz(n) not defined for n <= 0.")
		else:
			c = collatz(n).nr_iters_to_one()
			print(" -> ".join([check_color(n) for n in c]))

def collatz_repl():
	try:
		while True:
			n = input("collatz_repl > ")
			parse_input(n)
	except KeyboardInterrupt as e:
		print("\nExiting...")

if __name__ == '__main__':
	print("Collatz REPL")
	print("Please enter an integer.\n")
	collatz_repl()
