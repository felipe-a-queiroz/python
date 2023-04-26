
current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
for movie in current_movies:
    print(movie)
movie = input('What movie do you want the showtime for?\n')

show_time = current_movies.get(movie)

if show_time == None:
    print("Requested movie isn't playing")
else:
    print(movie,'is playing at',show_time)