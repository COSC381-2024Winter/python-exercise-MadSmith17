from movies import Movies

class Query:
    def __init__(self):
        self.movies = Movies('./movies.txt')

    def menu(self):
        while True:
            print("Menu:")
            print("list - List all movie names")
            print("search - Search movies by names")
            print("cast - Search movies by cast")
            print("q - Quit")
            
            choice = input("Enter your choice: ")
            if choice == 'q':
                print("Exiting program...")
                break
            elif choice == "list":
                self.list_movie_names()
            elif choice == "search":
                self.search_by_name()
            elif choice == "cast":
                self.search_by_cast()
            else:
                print("Invalid choice. Please try again.")

    def list_movie_names(self):
        movies = self.movies._movies
        if not movies:
            print("No movies found.")
            return
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie['name']}")

    def search_by_name(self):
        search_term = input("Enter a partial name of the movie: ").lower()
        found_movies = []
        for movie in self.movies._movies:
            if search_term in movie['name'].lower():
                found_movies.append(movie['name'])
        if found_movies:
            print("Search results:")
            for movie in found_movies:
                print(movie)
        else:
            print("No results found.")

    def search_by_cast(self):
        search_term = input("Enter a partial name of the cast member: ")
        found_movies = {}
        for movie in self.movies._movies:
            for actor in movie['cast']:
                if search_term.lower() in actor.lower():
                    found_movies.setdefault(movie['name'], []).append(actor)
        if found_movies:
            print("Search results:")
            for movie, cast in found_movies.items():
                print(f"{movie}: {', '.join(cast)}")
        else:
            print("No results found.")

if __name__ == "__main__":
    query = Query()
    query.menu()