from movies import Movies

class Query:
    def __init__(self):
        self.movies = Movies()

    def menu(self):
        while True:
            print("Menu:")
            print("1. List all movie names")
            print("q. Quit")
            
            choice = input("Enter your choice: ")
            if choice == 'q':
                print("Exiting program...")
                break
            elif choice == '1':
                self.list_movie_names()
            else:
                print("Invalid choice. Please try again.")

    def list_movie_names(self):
        movies = self.movies.get_movie_names()
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")

if __name__ == "__main__":
    query = Query()
    query.menu()