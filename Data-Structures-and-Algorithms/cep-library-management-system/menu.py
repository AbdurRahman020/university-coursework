from library_system import LibrarySystem
from test_suite import run_tests


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("UET LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1.  Add Book")
    print("2.  Search Book by ISBN")
    print("3.  Search Book by Title")
    print("4.  Search Books by Author")
    print("5.  Add Member")
    print("6.  Borrow Book")
    print("7.  Return Book")
    print("8.  List Member's Borrowed Books")
    print("9.  List Available Books")
    print("10. List All Books (Sorted by ISBN)")
    print("11. Load Books from CSV")
    print("12. Run Test Suite")
    print("\n- REPORTS -")
    print("13. Generate Author Report")
    print("14. Generate Member Report")
    print("15. Generate Availability Report")
    print("16. Generate Full Catalog Report")
    print("17. Export Report to File")
    print("\n0.  Exit")
    print("=" * 60)


def main():
    """Main interactive program."""
    library = LibrarySystem()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            # add book
            print("\nAdd Book: ")
            isbn = input("ISBN (13 digits): ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            year = int(input("Year: "))
            category = input("Category: ").strip()
            copies = int(input("Total Copies: "))

            success, msg = library.add_book(
                isbn, title, author, year, category, copies)
            print(f"\n{msg}")

        elif choice == "2":
            # search by ISBN
            isbn = input("\nEnter ISBN: ").strip()
            book = library.search_by_isbn(isbn)
            if book:
                print("\nBook Found:")
                print(f"  Title: {book['title']}")
                print(f"  Author: {book['author']}")
                print(f"  Year: {book['year']}")
                print(f"  Category: {book['category']}")
                print(f"  Available: {
                      book['available_copies']}/{book['total_copies']}")
            else:
                print("\nBook not found")

        elif choice == "3":
            # search by title
            title = input("\nEnter Title: ").strip()
            book = library.search_by_title(title)
            if book:
                print("\nBook Found:")
                print(f"  Title: {book['title']}")
                print(f"  Author: {book['author']}")
                print(f"  Available: {
                      book['available_copies']}/{book['total_copies']}")
            else:
                print("\nBook not found")

        elif choice == "4":
            # search by author
            author = input("\nEnter Author: ").strip()
            books = library.search_by_author(author)
            if books:
                print(f"\nFound {len(books)} book(s):")
                for book in books:
                    print(f"  - {book['title']} ({book['isbn']})")
            else:
                print("\nNo books found by this author")

        elif choice == "5":
            # add member
            print("\nAdd Member:")
            member_id = input("Member ID (e.g., 2024-EE-001): ").strip()
            name = input("Name: ").strip()
            member_type = input("Type (student/faculty): ").strip()

            success, msg = library.add_member(member_id, name, member_type)
            print(f"\n{msg}")

        elif choice == "6":
            # borrow book
            member_id = input("\nMember ID: ").strip()
            isbn = input("Book ISBN: ").strip()

            success, msg = library.borrow_book(member_id, isbn)
            print(f"\n{msg}")

        elif choice == "7":
            # return Book
            member_id = input("\nMember ID: ").strip()
            isbn = input("Book ISBN: ").strip()

            success, msg = library.return_book(member_id, isbn)
            print(f"\n{msg}")

        elif choice == "8":
            # list member's books
            member_id = input("\nMember ID: ").strip()
            borrowed = library.list_member_books(member_id)
            if borrowed is not None:
                if borrowed:
                    print(f"\nBorrowed Books ({len(borrowed)}):")
                    for book in borrowed:
                        print(f"  - {book['title']} ({book['isbn']})")
                else:
                    print("\nNo borrowed books")
            else:
                print("\nMember not found")

        elif choice == "9":
            # list available books
            available = library.list_available_books()
            print(f"\nAvailable Books ({len(available)}):")
            for book in available[:20]:  # show first 20
                print(f"  - {book['title']} by {book['author']} "
                      f"({book['available_copies']} available)")
            if len(available) > 20:
                print(f"  ... and {len(available) - 20} more")

        elif choice == "10":
            # list all books
            all_books = library.list_all_books_sorted()
            print(f"\nAll Books ({len(all_books)}):")
            for isbn, book in all_books[:20]:  # show first 20
                print(f"  {isbn}: {book['title']}")
            if len(all_books) > 20:
                print(f"  ... and {len(all_books) - 20} more")

        elif choice == "11":
            # load from CSV
            filename = input(
                "\nEnter CSV filename (e.g., books.csv): ").strip()
            success, msg = library.load_books_from_csv(filename)
            print(f"\n{msg}")

        elif choice == "12":
            # run tests
            run_tests()

        elif choice == "13":
            # author report
            author = input("\nEnter Author Name: ").strip()
            report = library.generate_report_by_author(author)

            if report:
                print("\n" + "=" * 60)
                print(f"REPORT: Books by {report['author']}")
                print("=" * 60)
                print(f"Total Books: {report['total_books']}")
                print(f"Total Copies: {report['total_copies']}")
                print(f"Available: {report['available_copies']}")
                print(f"Borrowed: {report['borrowed_copies']}")
                print("\nBooks:")
                for book in report['books']:
                    print(f"  - {book['title']} (ISBN: {book['isbn']})")
                    print(f"    Available: {
                          book['available_copies']}/{book['total_copies']}")
            else:
                print("\nNo books found by this author")

        elif choice == "14":
            # member report
            member_id = input("\nEnter Member ID: ").strip()
            report = library.generate_report_by_member(member_id)

            if report:
                print("\n" + "=" * 60)
                print(f"REPORT: Member {report['member_id']}")
                print("=" * 60)
                print(f"Name: {report['member_name']}")
                print(f"Type: {report['member_type']}")
                print(f"Borrowed: {report['total_borrowed']}/5 books")
                print(f"Remaining Limit: {report['remaining_limit']}")

                if report['books']:
                    print("\nBorrowed Books:")
                    for book in report['books']:
                        print(f"  - {book['title']} by {book['author']}")
                        print(f"    ISBN: {book['isbn']}")
                else:
                    print("\nNo books currently borrowed")
            else:
                print("\nMember not found")

        elif choice == "15":
            # availability report
            report = library.generate_availability_report()

            print("\n" + "=" * 60)
            print("LIBRARY AVAILABILITY REPORT")
            print("=" * 60)
            print(f"Total Unique Books: {report['total_unique_books']}")
            print(f"Total Copies: {report['total_copies']}")
            print(f"Books Available: {report['books_available']}")
            print(f"Total Borrowed: {report['total_borrowed']}")
            print(f"Availability Rate: {
                  report['availability_percentage']:.2f}%")

            print("\nCategory Breakdown:")
            for category, stats in report['category_breakdown'].items():
                print(f"\n  {category}:")
                print(f"    Books: {stats['total_books']}")
                print(f"    Total Copies: {stats['total_copies']}")
                print(f"    Available: {stats['available_copies']}")
                print(f"    Borrowed: {
                      stats['total_copies'] - stats['available_copies']}")

        elif choice == "16":
            # full catalog report
            catalog = library.generate_full_catalog_report()

            print("\n" + "=" * 60)
            print("FULL CATALOG REPORT (Sorted by ISBN)")
            print("=" * 60)
            print(f"Total Books: {len(catalog)}\n")

            # Show first 20
            for book in catalog[:20]:
                print(f"ISBN: {book['isbn']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Category: {book['category']}")
                print(f"Status: {book['availability_status']} "
                      f"({book['available_copies']}/{book['total_copies']})")
                print()

            if len(catalog) > 20:
                print(f"... and {len(catalog) - 20} more books")

        elif choice == "17":
            # export report
            print("\n Export Report:")
            print("1. Author Report")
            print("2. Member Report")
            print("3. Availability Report")
            print("4. Full Catalog Report")

            report_choice = input("\nSelect report type (1-4): ").strip()
            filename = input(
                "Enter output filename (e.g., report.txt): ").strip()

            if report_choice == "1":
                author = input("Enter Author Name: ").strip()
                success, msg = library.export_report_to_file(
                    'author', filename, author=author)
            elif report_choice == "2":
                member_id = input("Enter Member ID: ").strip()
                success, msg = library.export_report_to_file(
                    'member', filename, member_id=member_id)
            elif report_choice == "3":
                success, msg = library.export_report_to_file(
                    'availability', filename)
            elif report_choice == "4":
                success, msg = library.export_report_to_file(
                    'catalog', filename)
            else:
                success, msg = False, "Invalid report type"

            print(f"\n{msg}")

        elif choice == "0":
            print("\nThank you for using UET Library Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")
