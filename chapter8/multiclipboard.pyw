#! python3
# Multiclipboard.pyw - saves and loads pieces of text to the clipboard
# Usage : multiclipboard.pyw save <keyword> - saves clipboard to keywords.
# multiclipboard.pyw <keywords> - loads keyword to clipboard
# multiclipboard.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbshelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
