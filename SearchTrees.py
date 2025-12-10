class _BSTNode:
  """Node of a Binary Search Tree."""
  __slots__ = "key", "value", "left", "right"

  def __init__(self, key, value):
      self.key = key
      self.value = value
      self.left = None
      self.right = None


class BSTMap:
  """Unbalanced Binary Search Tree Map."""

  def __init__(self):
      self._root = None

  # ------------------------ INSERT ------------------------
  def insert(self, key, value):
      """Insert or update a key-value pair."""
      self._root = self._insert_recursive(self._root, key, value)

  def _insert_recursive(self, node, key, value):
      if node is None:
          return _BSTNode(key, value)
      if key < node.key:
          node.left = self._insert_recursive(node.left, key, value)
      elif key > node.key:
          node.right = self._insert_recursive(node.right, key, value)
      else:
          node.value = value  # update existing key
      return node

  # ------------------------ SEARCH ------------------------
  def search(self, key):
      """Return the value matching key, or None if not found."""
      return self._search_recursive(self._root, key)

  def _search_recursive(self, node, key):
      if node is None:
          return None
      if key < node.key:
          return self._search_recursive(node.left, key)
      elif key > node.key:
          return self._search_recursive(node.right, key)
      else:
          return node.value

  # ------------------- TRAVERSAL (INORDER) -------------------
  def inorder_items(self):
      """Yield (key, value) pairs in sorted order."""
      yield from self._inorder_recursive(self._root)

  def _inorder_recursive(self, node):
      if node is not None:
          yield from self._inorder_recursive(node.left)
          yield (node.key, node.value)
          yield from self._inorder_recursive(node.right)

  # ------------------------ HEIGHT ------------------------
  def height(self):
      """Return the height of the BST.
      Height is defined as the number of edges on the longest root-to-leaf path.
      Empty tree returns -1, tree with only root returns 0.
      """
      return self._height_recursive(self._root)

  def _height_recursive(self, node):
      """Recursively compute height of subtree rooted at node."""
      if node is None:
          return -1
      left_height = self._height_recursive(node.left)
      right_height = self._height_recursive(node.right)
      return 1 + max(left_height, right_height)


# ---------------------------------------------------------
# ---------------------- AVL TREE MAP ---------------------
# ---------------------------------------------------------

class _AVLNode:
  """Node of an AVL Tree."""
  __slots__ = "key", "value", "left", "right", "height"

  def __init__(self, key, value):
      self.key = key
      self.value = value
      self.left = None
      self.right = None
      self.height = 0  # used for AVL balancing


class AVLTreeMap:
  """Self-balancing AVL Tree Map."""

  def __init__(self):
      self._root = None

  # ------------------------ INSERT ------------------------
  def insert(self, key, value):
      self._root = self._insert_recursive(self._root, key, value)

  def _insert_recursive(self, node, key, value):
      if node is None:
          return _AVLNode(key, value)
      if key < node.key:
          node.left = self._insert_recursive(node.left, key, value)
      elif key > node.key:
          node.right = self._insert_recursive(node.right, key, value)
      else:
          node.value = value  # update existing
          return node

      # update height
      node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))

      # compute balance factor
      balance = self._get_balance(node)

      # perform rotations if unbalanced
      # Case 1: Left Left
      if balance > 1 and key < node.left.key:
          return self._rotate_right(node)

      # Case 2: Right Right
      if balance < -1 and key > node.right.key:
          return self._rotate_left(node)

      # Case 3: Left Right
      if balance > 1 and key > node.left.key:
          node.left = self._rotate_left(node.left)
          return self._rotate_right(node)

      # Case 4: Right Left
      if balance < -1 and key < node.right.key:
          node.right = self._rotate_right(node.right)
          return self._rotate_left(node)

      return node

  # ------------------------ SEARCH ------------------------
  def search(self, key):
      return self._search_recursive(self._root, key)

  def _search_recursive(self, node, key):
      if node is None:
          return None
      if key < node.key:
          return self._search_recursive(node.left, key)
      elif key > node.key:
          return self._search_recursive(node.right, key)
      else:
          return node.value

  # ------------------- TRAVERSAL (INORDER) -------------------
  def inorder_items(self):
      yield from self._inorder_recursive(self._root)

  def _inorder_recursive(self, node):
      if node:
          yield from self._inorder_recursive(node.left)
          yield (node.key, node.value)
          yield from self._inorder_recursive(node.right)

  # ------------------- AVL UTILITIES -------------------
  def _get_height(self, node):
      return node.height if node else -1

  def _get_balance(self, node):
      return self._get_height(node.left) - self._get_height(node.right)

  def _rotate_left(self, z):
      y = z.right
      T2 = y.left

      # perform rotation
      y.left = z
      z.right = T2

      # update heights
      z.height = 1 + max(self._get_height(z.left),
                         self._get_height(z.right))
      y.height = 1 + max(self._get_height(y.left),
                         self._get_height(y.right))
      return y

  def _rotate_right(self, z):
      y = z.left
      T3 = y.right

      # perform rotation
      y.right = z
      z.left = T3

      # update heights
      z.height = 1 + max(self._get_height(z.left),
                         self._get_height(z.right))
      y.height = 1 + max(self._get_height(y.left),
                         self._get_height(y.right))
      return y

  # ------------------------ HEIGHT ------------------------
  def height(self):
      """Return the height of the AVL tree.
      Recomputes height recursively based on subtree structure.
      Does NOT use stored node.height field.
      Empty tree returns -1, tree with only root returns 0.
      """
      return self._height_recursive(self._root)

  def _height_recursive(self, node):
      """Recursively compute height of subtree rooted at node."""
      if node is None:
          return -1
      left_height = self._height_recursive(node.left)
      right_height = self._height_recursive(node.right)
      return 1 + max(left_height, right_height)
