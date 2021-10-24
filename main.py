from collatz import collatz, plot_sequence
from colorama import Fore, init

init(autoreset = True)

even = lambda n: f"{Fore.GREEN}{n}"
odd = lambda n: f"{Fore.RED}{n}"
check_color = lambda n: even(n) if n % 2 == 0 else odd(n)

def parse_input(arg):
	arg = arg.split(" ")
	if len(arg) == 2 and arg[0] == "plot":
		try:
			n = int(arg[1])
		except Exception as e:
			print(f"Error: {e}")
		else:
			plot_sequence(n)

	if len(arg) == 1:
		try:
			n = int(arg[0])
		except Exception as e:
			print(f"Error: {e}")		
		else:
			c = collatz(n).nr_iters_to_one()
			print(" -> ".join([check_color(n) for n in c]))

def collatz_repl():
	try:
		while True:
			arg = input("collatz_repl > ")
			parse_input(arg)
	except KeyboardInterrupt as e:
		print("\nExiting...")

if __name__ == '__main__':
	print("Collatz REPL")
	print("Please enter an integer.\n")
	collatz_repl()
