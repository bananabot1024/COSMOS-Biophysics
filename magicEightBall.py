import sys, random
while True:
	question = raw_input("Ask a question or press enter to quit: ")
	answer = random.randint(1, 8)
	if question == "":
		sys.exit()
	x = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say yes"]
	print x[answer - 1]

