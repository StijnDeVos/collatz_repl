def parse_input(arg):
	arg = arg.split(" ")
	if arg[0] == "plot" and len(arg) >= 2:
		try:
			n = int(arg[1])
		except Exception as e:
			print(f"Error: {e}")
		else:
			plot_sequence(n)

	if len(arg) == 1 and arg[0] != "h":
		try:
			n = int(arg[0])
		except Exception as e:
			print(f"Error: {e}")		
		else:
			c = collatz(n).sequence()
			print_sequence(c)

	if len(arg) == 1 and arg[0] == "h":
		print("\t- Enter a number n to print the Collatz sequence, starting from n.")
		print("\t- Type \'plot <n>\' to view a plot of the Collatz sequence.")

