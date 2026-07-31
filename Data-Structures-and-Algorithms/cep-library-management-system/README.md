# Library Management System
**CEP Project — Data Structures & Algorithms | UET Lahore**

A console-based Library Management System built in Python as part of the DSA course. The goal was to apply data structures we studied in class to a real-world-ish problem — managing books, members, borrowing, and reporting for a library.

---

## Data Structures Used

### AVL Tree (`avl_tree.py`)
Used as the main book catalog, indexed by ISBN. Books are inserted, searched, and listed in sorted order using in-order traversal. The self-balancing property keeps search at O(log n) even as the catalog grows.

### Hash Table with Chaining (`hash_table.py`)
Used for three indexes:
- **Title index** — maps book title → ISBN
- **Author index** — maps author name → list of ISBNs
- **Member database** — maps member ID → member data

Collision resolution is done via chaining (linked list per bucket). The table also auto-resizes when the load factor exceeds 0.75, rehashing all entries into a doubled bucket array. Average case for insert/search/delete is O(1).

---

## Project Structure

```
cep-library-management-system/
│
├── avl_tree.py          # AVL Tree implementation
├── hash_table.py        # Hash Table with chaining
├── library_system.py    # Core logic — integrates both data structures
├── menu.py              # Interactive CLI menu
├── run.py               # Entry point
├── test_suite.py        # Test cases
├── books.csv            # Sample book data
└── members.csv          # Sample member data
```

---

## Features

- Add books and members
- Search by ISBN, title, or author (exact and partial match)
- Borrow and return books with availability tracking
- Borrowing limit of 5 books per member
- Load books/members from CSV
- Generate reports: by author, by member, availability stats, full catalog
- Export any report to a `.txt` file

---

## How to Run

```bash
python run.py
```

You'll be prompted to choose between interactive mode or running the test suite directly.

To load sample data from the provided CSV files, use option `11` from the menu after launching.

---

## Design Decisions

- **Why AVL Tree for books?** ISBNs are unique and we needed sorted listing — AVL gives us O(log n) insert/search and in-order traversal for free.
- **Why Hash Table for indexes?** Title and author lookups don't need ordering, so O(1) average-case hash lookup made more sense than a tree.
- **Why chaining for collision resolution?** Simpler to implement correctly and handles high load gracefully compared to open addressing.

---

## Limitations

- Data is not persistent — everything resets when the program exits (CSV reload workaround exists)
- No due dates or fine tracking
- Partial author search falls back to O(n) scan across all keys

---

---

*CEP project for EE234L — Data Structures and Algorithms, UET Lahore. Full spec in [`cea_dsa.pdf`](./cea_dsa.pdf).*
