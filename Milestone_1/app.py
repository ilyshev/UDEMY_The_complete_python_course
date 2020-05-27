'''

'''

movies = []
'''
movie = {
    'name' = ....(str),
    'director' = ...(str),
    'year' = ... (int)
}

'''


def menu():
    user_input = input('Please enter "a" for add a movie, "l" to watch your movies, "f" to find a movie, "q" for exit: ')
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command - please try again.')

        user_input = input('\nPlease enter "a" for add a movie, "l" to watch your movies, "f" to find a movie, "q" for exit: ')


def add_movie():
     name = input('Enter the movie name: ')
     director = input('Enter the movie director: ')
     year = input('Enter the movie release year: ')

     movies.append({
         'name': name,
         'director': director,
         'year': year
     })


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    find_by = input('What property of the movie are you looking for? ')
    looking_for = input('What are you searching for? ')

    found = []
    for movie in movies:
        if movie[find_by] == looking_for:
            found.append(movie)
    show_movies(found)


menu()