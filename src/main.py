from colorama import init
from parse_input import parse_input

init(autoreset = True)

def collatz_repl():
	history = {}
	count = 1
	try:
		while True:
			arg = input("collatz_repl> ")
			if arg == "exit" or arg == "quit":
				return None
			else:
				history.update({count : arg})
				count += 1
				parse_input(arg)
	except KeyboardInterrupt as e:
		print("\nExiting...")

if __name__ == '__main__':
	print("Collatz REPL")
	print("Type \'h\' for help.\n")
	collatz_repl()
	print("Exiting Collatz REPL...")