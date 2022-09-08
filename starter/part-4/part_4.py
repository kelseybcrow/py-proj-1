### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def create_new_book():
    title = input('What is your favorite book? ')
    year = input('When was it published? ')
    author = input('Who is the author? ')
    length = input('How many pages is it? ')

    book_dictionary = {
        'title': title,
        'author': author,
        'year': year,
        'length': length

    }

    print(book_dictionary)
    return (book_dictionary)

create_new_book()

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_new_book_types():
    title = input('What is your favorite book? ')
    year = int(input('When was it published? '))
    author = input('Who is the author? ')
    rating = float(input('What rating out of 5 do you give this book? '))
    pages = int(input('How many pages is it? '))

    book_dictionary = {
        'title': title,
        'author': author,
        'rating': rating,
        'year': year,
        'pages': pages

    }

    print(book_dictionary)
    print(type(book_dictionary['pages']))

    return (book_dictionary)

create_new_book()


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book_errors():
    title = input('What is your favorite book? ')
    try:
        year = int(input('When was it published? '))
    except:
        year = int(input('Please type a number for the year. '))
    author = input('Who is the author? ')
    try:
        rating = float(input('What rating out of 5 do you give this book? '))
    except:
        rating = float(input('Please type a number from 1 to 5. '))
    pages = int(input('How many pages is it? '))

    book_dictionary = {
        'title': title,
        'author': author,
        'rating': rating,
        'year': year,
        'pages': pages

    }

    print(book_dictionary)
    print(type(book_dictionary['pages']))

    return (book_dictionary)

create_new_book()

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

