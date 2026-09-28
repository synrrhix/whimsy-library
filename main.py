from books import books
from analysis import create_dataframe, count_values, average_rating_by_genre, add_book_age, average_pages_by_genre, \
    top_rated_books, plot_genres, plot_books_by_year, average_rating_genre, plot_ratings, filter_by_whatever
from functions import add_book, remove_book, find_book, show_books, sort_books, \
    get_highest_rated_books, find_books_by_author, get_top_books
from storage import save_books, load_books


def main():
    current_books = books

    while True:
        print("\n===== WHIMSY =====")
        print("1. Show books")
        print("2. Add book")
        print("3. Remove book")
        print("4. Find book")
        print("5. Sort books")
        print("6. Find books by author")
        print("7. Show highest-rated books")
        print("8. Show top N books")
        print("9. Save books")
        print("10. Load books")
        print("11. Analyse library")
        print("12. Exit")

        choice = input("> ").strip()

        if choice == "1":
            show_books(current_books)

        elif choice == "2":
            add_book(current_books)

        elif choice == "3":
            title = input("Enter book title to remove: ").strip()
            remove_book(current_books, title)

        elif choice == "4":
            title = input("Enter book title to find: ").strip()
            book = find_book(current_books, title)

            if book is None:
                print("Book not found.")
            else:
                print(book)

        elif choice == "5":
            sorted_books = sort_books(current_books)

            if sorted_books is not None:
                show_books(sorted_books)

        elif choice == "6":
            result = find_books_by_author(current_books)

            if result is None:
                print("No books found.")
            else:
                print(result)

        elif choice == "7":
            highest = get_highest_rated_books(current_books)

            if not highest:
                print("No highly-rated books found.")
            else:
                show_books(highest)

        elif choice == "8":
            n = int(input("How many books? "))
            top_books = get_top_books(current_books, n)
            show_books(top_books)

        elif choice == "9":
            save_books(current_books)

        elif choice == "10":
            loaded_books = load_books()

            if loaded_books is None:
                print("No save file found.")
            else:
                current_books = loaded_books
                print("Books loaded successfully.")

        elif choice == "11":
            df = create_dataframe(current_books)

            while True:
                print("\n===== ANALYSIS =====")
                print("1. Average rating")
                print("2. Count values")
                print("3. Average rating by genre")
                print("4. Average pages by genre")
                print("5. Top-rated books")
                print("6. Add book age")
                print("7. Visualise")
                print('8. Filter books')
                print("9. Back")

                analysis_choice = input("> ").strip()

                if analysis_choice == "1":
                    print(f"Average rating: {df['rating'].mean():.2f}")

                elif analysis_choice == "2":
                    result = count_values(df)

                    if result is not None:
                        print(result)

                elif analysis_choice == "3":
                    print(average_rating_by_genre(df))

                elif analysis_choice == "4":
                    print(average_pages_by_genre(df))

                elif analysis_choice == "5":
                    print(top_rated_books(df)[["title", "author", "rating"]])

                elif analysis_choice == "6":
                    df = add_book_age(df)
                    print(df[["title", "year", "age"]])

                elif analysis_choice == "7":
                    while True:
                        print("\n===== VISUALISE =====")
                        print("1. Books by genre")
                        print("2. Books by rating")
                        print("3. Average rating by genre")
                        print("4. Books published by year")
                        print("5. Back")

                        visual_choice = input("> ").strip()

                        if visual_choice == "1":
                            plot_genres(df)

                        elif visual_choice == "2":
                            plot_ratings(df)

                        elif visual_choice == "3":
                            average_rating_genre(df)

                        elif visual_choice == "4":
                            plot_books_by_year(df)

                        elif visual_choice == "5":
                            break

                        else:
                            print("Invalid option.")

                elif analysis_choice == "8":
                    result = filter_by_whatever(df)

                    if result is None:
                        print("No matching books found.")
                    else:
                        print(result.to_string(index=False))

                elif analysis_choice == "9":
                    break

                else:
                    print("Invalid option.")

        elif choice == "12":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()