from collatz import collatz
from colorama import Fore, init

init(autoreset = True)

even = lambda n: f"{Fore.GREEN}{n}"
odd = lambda n: f"{Fore.RED}{n}"
check_color = lambda n: even(n) if n % 2 == 0 else odd(n)

def collatz_repl():
	try:
		while True:
			n = input(">> ")
			try:
				n = int(n)				
			except Exception as e:
				print(f"Error: {e}")
			else:
				c = collatz(n).nr_iters_to_one()
				print(" -> ".join([check_color(n) for n in c]))
	except KeyboardInterrupt as e:
		print("\nExiting...")

if __name__ == '__main__':
	print("Collatz REPL")
	print("Please enter an integer.\n")
	collatz_repl()
