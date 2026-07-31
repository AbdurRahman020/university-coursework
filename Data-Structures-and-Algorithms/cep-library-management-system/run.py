from test_suite import run_tests
from menu import main

if __name__ == "__main__":
    print("\nWelcome to UET Library Management System!")
    print("Would you like to:")
    print("1. Run Interactive Mode")
    print("2. Run Test Suite Only")

    mode = input("\nEnter choice (1 or 2): ").strip()

    if mode == "2":
        run_tests()
    else:
        main()
