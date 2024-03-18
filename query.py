from movies import Movies

class Query:
    def __init__(self):
        self.movies = Movies()

    def menu(self):
        while True:
            print("Menu:")
            print("q. Quit")
            
            choice = input("Enter your choice: ")
            if choice == 'q':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    query = Query()
    query.menu()