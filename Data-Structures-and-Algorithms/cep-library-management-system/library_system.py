"""
Library Management System
Integrates AVL Tree and Hash Tables for book/member management
All business logic, integration, and features are original work
"""

import csv
from hash_table import HashTable
from avl_tree import AVLTree


class LibrarySystem:
    """Main library management system."""

    def __init__(self):
        # ISBN -> Book data
        self.book_catalog = AVLTree()
        # Title -> ISBN
        self.title_index = HashTable(50)
        # Author -> List of ISBNs
        self.author_index = HashTable(50)
        # Member ID -> Member object
        self.member_database = HashTable(50)

    def add_book(self, isbn, title, author, year, category, total_copies):
        """Add a book to the system."""
        # check if book already exists
        if self.book_catalog.search(isbn):
            return False, "Book with this ISBN already exists"

        # create book data
        book_data = {
            'title': title,
            'author': author,
            'year': year,
            'category': category,
            'total_copies': total_copies,
            'available_copies': total_copies
        }

        # insert into AVL tree
        self.book_catalog.insert(isbn, book_data)

        # insert into title index (normalized)
        normalized_title = title.lower().strip()
        self.title_index.insert(normalized_title, isbn)

        # insert into author index
        normalized_author = author.lower().strip()
        author_books = self.author_index.search(normalized_author)

        if author_books is None:
            author_books = []

        author_books.append(isbn)
        self.author_index.insert(normalized_author, author_books)

        return True, "Book added successfully"

    def search_by_isbn(self, isbn):
        """Search for a book by ISBN."""
        return self.book_catalog.search(isbn)

    def search_by_title(self, title):
        """Search for a book by title."""
        normalized_title = title.lower().strip()
        isbn = self.title_index.search(normalized_title)

        if isbn:
            return self.book_catalog.search(isbn)

        return None

    def search_by_author(self, author):
        """Search for all books by an author (exact or partial match)."""
        normalized_author = author.lower().strip()

        # try exact match first (O(1))
        isbn_list = self.author_index.search(normalized_author)

        # fallback: partial match across all keys (O(n))
        if not isbn_list:
            isbn_list = []
            for key in self.author_index.get_all_keys():
                if normalized_author in key:
                    isbn_list.extend(self.author_index.search(key))

        if isbn_list:
            books = []
            for isbn in isbn_list:
                book_data = self.book_catalog.search(isbn)
                if book_data:
                    books.append({'isbn': isbn, **book_data})

            return books

        return []

    def add_member(self, member_id, name, member_type="student"):
        """Add a member to the system."""
        if self.member_database.search(member_id):
            return False, "Member with this ID already exists"

        member_data = {
            'name': name,
            'type': member_type,
            'borrowed_books': []
        }

        self.member_database.insert(member_id, member_data)

        return True, "Member added successfully"

    def borrow_book(self, member_id, isbn):
        """Process book borrowing."""
        # check if member exists
        member = self.member_database.search(member_id)

        if not member:
            return False, "Member not found"

        # check borrowing limit
        if len(member['borrowed_books']) >= 5:
            return False, "Member has reached borrowing limit (5 books)"

        # check if book exists
        book = self.book_catalog.search(isbn)

        if not book:
            return False, "Book not found"

        # check if book is available
        if book['available_copies'] <= 0:
            return False, "Book not available"

        # check if member already borrowed this book
        if isbn in member['borrowed_books']:
            return False, "Member already borrowed this book"

        # update book availability
        book['available_copies'] -= 1

        # update member's borrowed books
        member['borrowed_books'].append(isbn)

        return True, f"Book borrowed successfully. Available copies: {book['available_copies']}"

    def return_book(self, member_id, isbn):
        """Process book return."""
        # check if member exists
        member = self.member_database.search(member_id)
        if not member:
            return False, "Member not found"

        # check if member has this book
        if isbn not in member['borrowed_books']:
            return False, "Member hasn't borrowed this book"

        # check if book exists
        book = self.book_catalog.search(isbn)
        if not book:
            return False, "Book not found in catalog"

        # update book availability
        book['available_copies'] += 1

        # remove from member's borrowed books
        member['borrowed_books'].remove(isbn)

        return True, f"Book returned successfully. Available copies: {book['available_copies']}"

    def list_all_books_sorted(self):
        """List all books in sorted order by ISBN."""
        return self.book_catalog.inorder_traversal()

    def list_available_books(self):
        """List all books with available copies."""
        all_books = self.book_catalog.inorder_traversal()
        available = []

        for isbn, book_data in all_books:
            if book_data['available_copies'] > 0:
                available.append({'isbn': isbn, **book_data})

        return available

    def list_member_books(self, member_id):
        """List all books borrowed by a member."""
        member = self.member_database.search(member_id)

        if not member:
            return None

        borrowed = []
        for isbn in member['borrowed_books']:
            book_data = self.book_catalog.search(isbn)
            if book_data:
                borrowed.append({'isbn': isbn, **book_data})

        return borrowed

    def load_books_from_csv(self, filename):
        """Load books from CSV file."""
        count = 0
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    isbn = row['ISBN']
                    title = row['Title']
                    author = row['Author']
                    year = int(row['Year'])
                    category = row['Category']
                    total_copies = int(row['TotalCopies'])

                    success, _ = self.add_book(
                        isbn, title, author, year, category, total_copies)
                    if success:
                        count += 1
            return True, f"Successfully loaded {count} books"
        except FileNotFoundError:
            return False, "File not found"
        except Exception as e:
            return False, f"Error loading file: {str(e)}"

    def load_members_from_csv(self, filename):
        """Load members from CSV file."""
        count = 0
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    member_id = row['MemberID']
                    name = row['Name']
                    member_type = row['Type'].lower()

                    success, _ = self.add_member(member_id, name, member_type)
                    if success:
                        count += 1
            return True, f"Successfully loaded {count} members"
        except FileNotFoundError:
            return False, "File not found"
        except Exception as e:
            return False, f"Error loading file: {str(e)}"

    def generate_report_by_author(self, author):
        """
        Generate a detailed report of all books by a specific author.

        Args:
            author: Author name to search for

        Returns:
            Dictionary with report data
        """
        books = self.search_by_author(author)

        if not books:
            return None

        total_copies = sum(book['total_copies'] for book in books)
        available_copies = sum(book['available_copies'] for book in books)
        borrowed_copies = total_copies - available_copies

        report = {
            'author': author,
            'total_books': len(books),
            'total_copies': total_copies,
            'available_copies': available_copies,
            'borrowed_copies': borrowed_copies,
            'books': books
        }

        return report

    def generate_report_by_member(self, member_id):
        """
        Generate a detailed report of books borrowed by a member.

        Args:
            member_id: Member ID to generate report for

        Returns:
            Dictionary with report data
        """
        member = self.member_database.search(member_id)
        if not member:
            return None

        borrowed_books = self.list_member_books(member_id)

        report = {
            'member_id': member_id,
            'member_name': member['name'],
            'member_type': member['type'],
            'total_borrowed': len(borrowed_books),
            'remaining_limit': 5 - len(borrowed_books),
            'books': borrowed_books
        }

        return report

    def generate_availability_report(self):
        """
        Generate a report of book availability statistics.

        Returns:
            Dictionary with availability statistics
        """
        all_books = self.list_all_books_sorted()
        available_books = self.list_available_books()

        total_books = len(all_books)
        total_available = len(available_books)
        total_borrowed = sum(
            book['total_copies'] - book['available_copies']
            for _, book in all_books
        )
        total_copies = sum(book['total_copies'] for _, book in all_books)

        # Category breakdown
        category_stats = {}
        for isbn, book in all_books:
            category = book['category']
            if category not in category_stats:
                category_stats[category] = {
                    'total_books': 0,
                    'total_copies': 0,
                    'available_copies': 0
                }
            category_stats[category]['total_books'] += 1
            category_stats[category]['total_copies'] += book['total_copies']
            category_stats[category]['available_copies'] += book[
                'available_copies']

        report = {
            'total_unique_books': total_books,
            'total_copies': total_copies,
            'books_available': total_available,
            'total_borrowed': total_borrowed,
            'availability_percentage': (total_available / total_books * 100
                                        ) if total_books > 0 else 0,
            'category_breakdown': category_stats
        }

        return report

    def generate_full_catalog_report(self):
        """
        Generate a complete catalog report sorted by ISBN.

        Returns:
            List of all books with full details
        """
        all_books = self.list_all_books_sorted()

        catalog = []
        for isbn, book in all_books:
            catalog.append({
                'isbn': isbn,
                'title': book['title'],
                'author': book['author'],
                'year': book['year'],
                'category': book['category'],
                'total_copies': book['total_copies'],
                'available_copies': book['available_copies'],
                'borrowed_copies': book['total_copies'] - book[
                    'available_copies'],
                'availability_status': 'Available' if book[
                    'available_copies'] > 0 else 'Not Available'
            })

        return catalog

    def export_report_to_file(self, report_type, filename, **kwargs):
        """
        Export a report to a text file.

        Args:
            report_type: Type of report ('author', 'member', 'availability', 'catalog')
            filename: Output filename
            **kwargs: Additional arguments for specific reports

        Returns:
            Tuple of (success, message)
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                if report_type == 'author':
                    author = kwargs.get('author')
                    report = self.generate_report_by_author(author)

                    if not report:
                        return False, f"No books found by author: {author}"

                    f.write("=" * 80 + "\n")
                    f.write(f"BOOKS BY AUTHOR: {report['author']}\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Total Books: {report['total_books']}\n")
                    f.write(f"Total Copies: {report['total_copies']}\n")
                    f.write(f"Available Copies: {
                            report['available_copies']}\n")
                    f.write(f"Borrowed Copies: {
                            report['borrowed_copies']}\n\n")
                    f.write("-" * 80 + "\n")
                    f.write("BOOK DETAILS:\n")
                    f.write("-" * 80 + "\n\n")

                    for book in report['books']:
                        f.write(f"ISBN: {book['isbn']}\n")
                        f.write(f"Title: {book['title']}\n")
                        f.write(f"Year: {book['year']}\n")
                        f.write(f"Category: {book['category']}\n")
                        f.write(f"Available: {
                                book['available_copies']}/{book['total_copies'
                                                                ]}\n")
                        f.write("\n")

                elif report_type == 'member':
                    member_id = kwargs.get('member_id')
                    report = self.generate_report_by_member(member_id)

                    if not report:
                        return False, f"Member not found: {member_id}"

                    f.write("=" * 80 + "\n")
                    f.write("MEMBER BORROWING REPORT\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Member ID: {report['member_id']}\n")
                    f.write(f"Name: {report['member_name']}\n")
                    f.write(f"Type: {report['member_type']}\n")
                    f.write(f"Books Borrowed: {report['total_borrowed']}/5\n")
                    f.write(f"Remaining Limit: {
                            report['remaining_limit']}\n\n")
                    f.write("-" * 80 + "\n")
                    f.write("BORROWED BOOKS:\n")
                    f.write("-" * 80 + "\n\n")

                    if report['books']:
                        for book in report['books']:
                            f.write(f"ISBN: {book['isbn']}\n")
                            f.write(f"Title: {book['title']}\n")
                            f.write(f"Author: {book['author']}\n\n")
                    else:
                        f.write("No books currently borrowed.\n")

                elif report_type == 'availability':
                    report = self.generate_availability_report()

                    f.write("=" * 80 + "\n")
                    f.write("LIBRARY AVAILABILITY REPORT\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Total Unique Books: {
                            report['total_unique_books']}\n")
                    f.write(f"Total Copies: {report['total_copies']}\n")
                    f.write(f"Books with Available Copies: {
                            report['books_available']}\n")
                    f.write(f"Total Borrowed Copies: {
                            report['total_borrowed']}\n")
                    f.write(f"Availability Rate: {
                            report['availability_percentage']:.2f}%\n\n")
                    f.write("-" * 80 + "\n")
                    f.write("CATEGORY BREAKDOWN:\n")
                    f.write("-" * 80 + "\n\n")

                    for category, stats in report['category_breakdown'].items():
                        f.write(f"Category: {category}\n")
                        f.write(f"  Books: {stats['total_books']}\n")
                        f.write(f"  Total Copies: {stats['total_copies']}\n")
                        f.write(f"  Available: {stats['available_copies']}\n")
                        f.write(f"  Borrowed: {
                                stats['total_copies'] - stats['available_copies']}\n\n")

                elif report_type == 'catalog':
                    catalog = self.generate_full_catalog_report()

                    f.write("=" * 80 + "\n")
                    f.write("COMPLETE LIBRARY CATALOG (Sorted by ISBN)\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Total Books: {len(catalog)}\n\n")
                    f.write("-" * 80 + "\n\n")

                    for book in catalog:
                        f.write(f"ISBN: {book['isbn']}\n")
                        f.write(f"Title: {book['title']}\n")
                        f.write(f"Author: {book['author']}\n")
                        f.write(f"Year: {book['year']}\n")
                        f.write(f"Category: {book['category']}\n")
                        f.write(f"Available: {
                                book['available_copies']}/{book['total_copies']}\n")
                        f.write(f"Status: {book['availability_status']}\n")
                        f.write("\n")

                else:
                    return False, f"Unknown report type: {report_type}"

            return True, f"Report exported successfully to {filename}"

        except Exception as e:
            return False, f"Error exporting report: {str(e)}"
