import csv
from SearchTrees import BSTMap, AVLTreeMap
from schedule_item import ScheduleItem

COLUMN_NAMES = [
    'Subject', 'Catalog', 'Section', 'Component', 'Session',
    'MinUnits', 'Units', 'TotEnrl', 'CapEnrl', 'Instructor',
    'Capacity', 'Room', 'Mtg Start', 'Mtg End', 'Days',
    'Start Date', 'End Date', 'Term', 'Campus', 'Class Nbr',
    'Total Credits', 'DUP', 'FULL', 'OVER'
]


class Schedule:
    """Course schedule using tree-based storage (BST or AVL)."""

    def __init__(self, tree_type='bst'):
        """Initialize schedule with specified tree backend.

        Args:
            tree_type: 'bst' for Binary Search Tree, 'avl' for AVL Tree
        """
        self.tree_type = tree_type.lower()
        if self.tree_type == 'avl':
            self._tree = AVLTreeMap()
        else:
            self._tree = BSTMap()
        self._count = 0

    def load_from_csv(self, filename):
        """Load schedule items from CSV file using csv.DictReader."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if not lines:
                    return 0
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) < 21:
                        continue
                    row = {
                        'Subject': parts[0],
                        'Catalog': parts[1],
                        'Section': parts[2],
                        'Component': parts[3],
                        'Session': parts[4],
                        'MinUnits': parts[5],
                        'Units': parts[6],
                        'TotEnrl': parts[7],
                        'CapEnrl': parts[8],
                        'Instructor': parts[9],
                        'Capacity': parts[10],
                        'Room': parts[11],
                        'Mtg Start': f"{parts[12]} {parts[13]}" if len(parts) > 13 else '',
                        'Mtg End': f"{parts[14]} {parts[15]}" if len(parts) > 15 else '',
                        'Days': parts[16] if len(parts) > 16 else '',
                        'Start Date': parts[17] if len(parts) > 17 else '',
                        'End Date': parts[18] if len(parts) > 18 else '',
                        'Term': parts[19] if len(parts) > 19 else '',
                        'Campus': parts[20] if len(parts) > 20 else '',
                        'Class Nbr': parts[21] if len(parts) > 21 else '',
                        'Total Credits': parts[22] if len(parts) > 22 else ''
                    }
                    item = ScheduleItem.from_dict(row)
                    key = item.get_key()
                    if key:
                        self._tree.insert(key, item)
                        self._count += 1
            return self._count
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return 0
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return 0

    def add_item(self, item):
        """Add a schedule item to the tree."""
        key = item.get_key()
        self._tree.insert(key, item)
        self._count += 1

    def search_by_class_nbr(self, class_nbr):
        """Search for a schedule item by class number."""
        return self._tree.search(str(class_nbr))

    def get_all_items(self):
        """Return all items in sorted order (inorder traversal)."""
        return list(self._tree.inorder_items())

    def get_height(self):
        """Return the height of the underlying tree."""
        return self._tree.height()

    def get_count(self):
        """Return the number of items in the schedule."""
        return self._count

    def get_tree_type(self):
        """Return the type of tree being used."""
        return self.tree_type.upper()

    def search_by_subject(self, subject):
        """Search for all items matching a subject code."""
        results = []
        for key, item in self._tree.inorder_items():
            if item.subject.upper() == subject.upper():
                results.append(item)
        return results

    def search_by_instructor(self, instructor_name):
        """Search for all items taught by an instructor (partial match)."""
        results = []
        search_term = instructor_name.lower()
        for key, item in self._tree.inorder_items():
            if search_term in item.instructor.lower():
                results.append(item)
        return results

    def search_by_course(self, subject, catalog):
        """Search for a specific course (Subject + Catalog)."""
        results = []
        for key, item in self._tree.inorder_items():
            if (item.subject.upper() == subject.upper() and 
                item.catalog == catalog):
                results.append(item)
        return results

    def display_all(self):
        """Display all schedule items."""
        items = self.get_all_items()
        if not items:
            print("No items in schedule.")
            return
        print(f"\n{'='*80}")
        print(f"Schedule ({self.get_tree_type()} Tree) - {self._count} items")
        print(f"{'='*80}")
        for key, item in items:
            print(item)
        print(f"{'='*80}\n")
