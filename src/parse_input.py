from collatz import collatz, plot_sequence, print_sequence, print_help

def parse_input(arg):
	arg = arg.split(" ")
	
	if arg[0] == "":
		return None
	elif arg[0] == "plot" and len(arg) >= 2:
		try:
			ns = [int(n) for n in arg[1:]]
		except Exception as e:
			print(f"Error: {e}")
		else:
			if n < 1:
				print(f"Error: not defined for n < 1.")
			else:
				plot_sequence(ns)
	elif len(arg) == 1 and arg[0] != "h":
		try:
			n = int(arg[0])
		except Exception as e:
			print(f"Error: {e}")		
		else:
			if n < 1:
				print(f"Error: not defined for n < 1.")
			else:
				c = collatz(n).sequence()
				print_sequence(c)

	elif len(arg) == 1 and arg[0] == "h":
		print_help()


