def spam():
	global eggs
	eggs = 'spam'  # This is the global
def bacon():
	eggs = 'bacon' # This is a local
def ham():
	print(eggs)    # This is the local
eggs = 42              # This is the global
spam()
print(eggs)
