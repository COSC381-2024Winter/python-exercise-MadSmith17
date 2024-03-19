from movies import Movies

class Query:
    def __init__(self):
        self.movies = Movies('./movies.txt')

    def menu(self):
        while True:
            print("Menu:")
            print("1. List all movie names")
            print("2. Search movies by names")
            print("3. Search movies by cast")
            print("q. Quit")
            
            choice = input("Enter your choice: ")
            if choice == 'q':
                print("Exiting program...")
                break
            elif choice == '1':
                self.list_movie_names()
            elif choice == '2':
                self.search_by_name()
            elif choice == '3':
                self.search_by_cast()
            else:
                print("Invalid choice. Please try again.")

    def list_movie_names(self):
        movies = self.movies.get_movie_names()
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")

    def search_by_name(self):
        search_term = input("Enter a partial name of the movie: ")
        results = self.movies.search_by_name(search_term)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No results found.")

    def search_by_cast(self):
        search_term = input("Enter a partial name of the cast member: ")
        results = self.movies.search_by_cast(search_term)
        if results:
            print("Search results:")
            for movie, cast in results.items():
                print(movie)
                print(cast)
        else:
            print("No results found.")

if __name__ == "__main__":
    query = Query()
    query.menu()