def movie_organizer(*movies):
    result = ""
    movies_genre = {}

    for movie, genre in movies:
        if genre not in movies_genre:
            movies_genre[genre] = []
        movies_genre[genre].append(movie)

    for genre, all_movies in sorted(movies_genre.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{genre} - {len(all_movies)}\n"
        for current_movie in sorted(all_movies, key=lambda x:x):
            result += f"* {current_movie}\n"

    return result




print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))