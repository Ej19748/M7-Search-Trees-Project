from schedule import Schedule

DATA_FILE = "schedule_data.txt"


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("     COURSE SCHEDULE TREE SYSTEM")
    print("=" * 50)
    print("1. Load data into BST")
    print("2. Load data into AVL Tree")
    print("3. Search by Class Number")
    print("4. Search by Subject")
    print("5. Search by Instructor")
    print("6. Search by Course (Subject + Catalog)")
    print("7. Display all items (BST)")
    print("8. Display all items (AVL)")
    print("9. Display Tree Heights (BST vs AVL)")
    print("10. Display Height Comparison Report")
    print("0. Exit")
    print("=" * 50)


def search_by_class_number(bst_schedule, avl_schedule):
    """Search for a class by its class number."""
    class_nbr = input("Enter Class Number to search: ").strip()

    print("\n--- BST Search Result ---")
    result = bst_schedule.search_by_class_nbr(class_nbr)
    if result:
        print(result)
    else:
        print("Not found in BST.")

    print("\n--- AVL Search Result ---")
    result = avl_schedule.search_by_class_nbr(class_nbr)
    if result:
        print(result)
    else:
        print("Not found in AVL.")


def search_by_subject(bst_schedule, avl_schedule):
    """Search for all classes in a subject."""
    subject = input("Enter Subject Code (e.g., BIO, CSC): ").strip().upper()

    print(f"\n--- Classes in {subject} (from BST) ---")
    results = bst_schedule.search_by_subject(subject)
    if results:
        for item in results[:10]:
            print(item)
        if len(results) > 10:
            print(f"... and {len(results) - 10} more items")
    else:
        print("No classes found.")


def search_by_instructor(bst_schedule, avl_schedule):
    """Search for classes by instructor name."""
    name = input("Enter Instructor Name (partial match): ").strip()

    print(f"\n--- Classes taught by '{name}' (from BST) ---")
    results = bst_schedule.search_by_instructor(name)
    if results:
        for item in results[:10]:
            print(item)
        if len(results) > 10:
            print(f"... and {len(results) - 10} more items")
    else:
        print("No classes found.")


def search_by_course(bst_schedule, avl_schedule):
    """Search for a specific course."""
    subject = input("Enter Subject Code: ").strip().upper()
    catalog = input("Enter Catalog Number: ").strip()

    print(f"\n--- Sections of {subject} {catalog} (from BST) ---")
    results = bst_schedule.search_by_course(subject, catalog)
    if results:
        for item in results:
            print(item)
    else:
        print("No sections found.")


def display_tree_heights(bst_schedule, avl_schedule):
    """Display the heights of both trees."""
    bst_height = bst_schedule.get_height()
    avl_height = avl_schedule.get_height()
    bst_count = bst_schedule.get_count()
    avl_count = avl_schedule.get_count()

    print("\n" + "=" * 50)
    print("         TREE HEIGHT COMPARISON")
    print("=" * 50)
    print(f"BST (Binary Search Tree):")
    print(f"  - Items: {bst_count}")
    print(f"  - Height: {bst_height}")
    print()
    print(f"AVL Tree (Self-Balancing):")
    print(f"  - Items: {avl_count}")
    print(f"  - Height: {avl_height}")
    print("=" * 50)

    if bst_height > avl_height:
        diff = bst_height - avl_height
        print(f"\nThe AVL tree is {diff} level(s) shorter than the BST.")
    elif avl_height > bst_height:
        diff = avl_height - bst_height
        print(f"\nThe BST is {diff} level(s) shorter than the AVL tree.")
    else:
        print("\nBoth trees have the same height.")


def display_height_report(bst_schedule, avl_schedule):
    """Display a detailed height comparison report."""
    bst_height = bst_schedule.get_height()
    avl_height = avl_schedule.get_height()
    count = bst_schedule.get_count()

    import math
    optimal_height = math.ceil(math.log2(count + 1)) - 1 if count > 0 else -1

    print("\n" + "=" * 60)
    print("         BST vs AVL TREE HEIGHT ANALYSIS REPORT")
    print("=" * 60)
    print(f"\nTotal items loaded: {count}")
    print(f"\nTree Heights:")
    print(f"  BST Height:      {bst_height}")
    print(f"  AVL Height:      {avl_height}")
    print(f"  Optimal Height:  {optimal_height} (for perfectly balanced tree)")

    print("\n--- Analysis ---")
    print("""
Height represents the number of edges on the longest path from root to leaf.
An empty tree has height -1, and a tree with only a root has height 0.

BST (Binary Search Tree):
- Does not self-balance during insertions
- Height depends on insertion order
- Worst case: O(n) height for sorted insertions
- Average case: O(log n) height for random insertions

AVL Tree:
- Self-balances after every insertion using rotations
- Guarantees height is always O(log n)
- Height difference between left/right subtrees is at most 1

For this dataset:""")

    if bst_height > avl_height:
        improvement = ((bst_height - avl_height) / bst_height * 100) if bst_height > 0 else 0
        print(f"- The AVL tree is more balanced ({improvement:.1f}% improvement)")
        print(f"- Searches in AVL would visit fewer nodes on average")
    elif bst_height == avl_height:
        print("- Both trees have equal height")
        print("- The insertion order may have been relatively balanced")
    else:
        print("- BST happens to be shorter (unusual case)")

    print("\nConclusion:")
    print("AVL trees provide consistent O(log n) search performance through")
    print("self-balancing, making them preferable for datasets where")
    print("insertion order might be sorted or partially sorted.")
    print("=" * 60)


def main():
    """Main program loop."""
    print("\nCourse Schedule Trees Project")
    print("Loading schedule data...")

    bst_schedule = Schedule('bst')
    avl_schedule = Schedule('avl')

    bst_count = bst_schedule.load_from_csv(DATA_FILE)
    avl_count = avl_schedule.load_from_csv(DATA_FILE)

    print(f"Loaded {bst_count} items into BST (Height: {bst_schedule.get_height()})")
    print(f"Loaded {avl_count} items into AVL (Height: {avl_schedule.get_height()})")

    while True:
        display_menu()
        choice = input("\nEnter your choice (0-10): ").strip()

        if choice == '0':
            print("\nThank you for using the Course Schedule System. Goodbye!")
            break
        elif choice == '1':
            bst_schedule = Schedule('bst')
            count = bst_schedule.load_from_csv(DATA_FILE)
            print(f"\nLoaded {count} items into BST. Height: {bst_schedule.get_height()}")
        elif choice == '2':
            avl_schedule = Schedule('avl')
            count = avl_schedule.load_from_csv(DATA_FILE)
            print(f"\nLoaded {count} items into AVL. Height: {avl_schedule.get_height()}")
        elif choice == '3':
            search_by_class_number(bst_schedule, avl_schedule)
        elif choice == '4':
            search_by_subject(bst_schedule, avl_schedule)
        elif choice == '5':
            search_by_instructor(bst_schedule, avl_schedule)
        elif choice == '6':
            search_by_course(bst_schedule, avl_schedule)
        elif choice == '7':
            bst_schedule.display_all()
        elif choice == '8':
            avl_schedule.display_all()
        elif choice == '9':
            display_tree_heights(bst_schedule, avl_schedule)
        elif choice == '10':
            display_height_report(bst_schedule, avl_schedule)
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
