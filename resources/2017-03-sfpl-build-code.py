#!/usr/bin/env python
# San Francisco Public Library - Learn, Design and Build Software!
#
# Sample program created by Louis Rawlins (louis@bonfireschool.com)
# Copyright 2016, Bonfire School, covered under GPLv3
#

# ##############################################################################
# READ ME FIRST
#
# Before anything else, know that '#' is a comment in this program.
#
# When you run a program in Python, any line that begins with '#' is ignored.
# This allows us to write notes and comments to ourselves while we program, and
# others (like yourself) who made read the program once it is written.
#
# Explore, change things, look around. This file is meant to be run repeatedly,
# broken and used as a playground.
#
# To run this file, type: 'python sfpl-classroom-code.py' in your terminal.
#
# If it's already running in a system like repl.it, then you're all set.
#
# ###

# ##############################################################################
# BACKGROUND
#
# Some history about the type of interface that inspired this program. While
# this program is a terminal-based search program, it has a history in more
# complicated (yet simple) programs, like Gopher.
#
# Gopher was popular in the early 1990s, before HTTP and the World Wide Web
# became popular. The websites you know today are all built on technology that
# is roughly similar to Gopher.
#
# Read About Gopher
# http://www.brebru.com/isgopher2.html
#
# Floodgap Public Gopher Proxy
# http://gopher.floodgap.com/gopher/
#
# Qualitative Ideosyncratic Xenodochium Gopherene
# http://home.quix.us:70/
#
# The Web may have won, but Gopher tunnels on (2009)
# https://arstechnica.com/tech-policy/2009/11/the-web-may-have-won-but-gopher-tunnels-on/
#
# ###

# ##############################################################################
# EXERCISES
#
# Pair up with another student. One of you can 'drive' and write code while the
# other person 'navigates' by calling out things you're looking for or might
# have missed. Working together facilitates learning because computer 
# programming is a complex subject. Don't worry, you'll have time to work on
# your own as well.
#

# ##############################################################################
# TOPICS
#
# ## Variables (assignment, comparison)
#
#    How do we store values?
#    How do we know what value something is? Does it change?
#
# ## Types (string, integer)
#
#    What is a type?
#    Why does it matter to know which type is which?
#    What can we do when we find a type we don't expect?
#
# ## Print (string, integer)
#
#    What does print() do?
#    Is there a difference between print strings and integers? Why?
#
# ## Input (type conversion)
#
#    How do we store values?
#    What can we do when we find a type we don't expect?
#
# ## Lists (storage, retrieval, array notation)
#
#    If we know how to store values, how can we store lists?
#    How do we get information OUT of the list?
#    What's an array? Why is it important?
#
# ## Conditionals (if, else, while, for)
#
#    What is a 'conditional'?
#    Why is this important? Isn't there an easier way?
#    What are the different types of conditionals? What do they do?
#
# ## Functions (definition, calling)
#
#    What is a 'function'?
#    What is a 'return value'?
#    How do we use functions?
#    When do we use functions?
#

# LIST - Lists of strings
books_with_titles = [
    'Where the Wild Things Are',
    'Over in the Meadow',
    'Goodnight Moon',
    'Little Bear',
    'The Giving Tree'
]

# EXTRA - Lists of lists
# books_with_dates_and_authors = [
#     ('Where the Wild Things Are', 'Maurice Sendak', 1963),
#     ('Over in the Meadow', 'Ezra Jack Keats', 1971),
#     ('Goodnight Moon', 'Margaret Wise Brown', 1947),
#     ('Little Bear', 'Else Holmelund Minarek', 1957),
#     ('The Giving Tree', 'Shel Silverstein', 1964)
# ]

# FUNCTION - Function Definition
def greeting():
    # We use the print function to display our interface to the user.
    # - What does '\n' mean and why is it useful?
    # - How could we improve this menu?
    print('\n--------------------------------------------------------------------------------')
    print('San Francisco Public Library - Children\'s Book Catalog')
    print('--------------------------------------------------------------------------------\n')
    print('What would you like to do?\n')
    print('  1. List all books')
    print('  2. Search books by title')
    print('  3. Exit')

# FUNCTION - Function Calls
greeting()

# CONDITIONAL - Conditional Statements
while True:
    user_choice = input('\nPlease select (? for help): ')

    # CONDITIONAL - Conditional Statements: if, elif and else
    if user_choice == '1':
        # How could we improve the readability of this book list?
        print('\n--------------------------------------------------------------------------------')
        print('All books')
        print('--------------------------------------------------------------------------------')
        for item in books_with_titles:
            print('  - ' + item)

    elif user_choice == '2':
        print('\n--------------------------------------------------------------------------------')
        print('Search books by title')
        print('--------------------------------------------------------------------------------')
        search_term = input('Enter title to search: ')
        matching_books = []

        print('\n--------------------------------------------------------------------------------')
        print('Search results for "' + search_term + '"')
        print('--------------------------------------------------------------------------------')
        for item in books_with_titles:
            # EXTRA - Search is case sensitive
            # - What happens when you search for "the" or "The"?
            # - How could you change this to find both?
            if search_term in str(item):
                title_position = books_with_titles.index(item)
                matching_books.append(books_with_titles[title_position])

        if matching_books == []:
            print('No Results\n')
        else:
            for item in matching_books:
                print('  - ' + item)

    elif user_choice == '3':
        break
    else:
        greeting()

###
