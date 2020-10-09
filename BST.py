class NodeTree:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None

class Bst:
  def __init__(self, root = None):
    self.root = root
    self.height = 0


  def insert(self, key, cont = 0 ):
    tree = self.root
    if self.root is None:
        self.root = NodeTree(key)
        self.root.right = Bst()
        self.root.left = Bst()

        return(cont)

    elif key < tree.key:
      return self.root.left.insert(key, cont +1 )

    else: 
      return self.root.right.insert(key, cont +1)

  

  def calc_height(self, recursion=True):
    if not self.root is None:
        if recursion:
            if self.root.left != None:
                self.root.left.calc_height()
            if self.root.right != None:
                self.root.right.calc_height()

        self.height = max(self.root.left.height, self.root.right.height) + 1
    else:
        self.height = -1


  def search(self, key):
    cont = 0
    if self.root.key == key:
      return 0
    else:
      pointer = self.root 

      while pointer != None:

        if pointer.key == key:
          return cont
        elif pointer.key > key:
          pointer = pointer.left.root 
          cont += 1
        elif pointer.key < key:
          pointer = pointer.right.root
          cont += 1
      return (-1)



  def search2(self, key):
    cont = 0
    cont2 = 0

    if self.root.key == key:
      return 0
    else:
      pointer = self.root 

      while pointer != None:

        if pointer.key == key:
          cont2 = cont

        if pointer.key > key:
          pointer = pointer.left.root 
          cont += 1
        elif pointer.key <= key:
          pointer = pointer.right.root
          cont += 1

      if cont == 0:
        return (-1)
      return(cont2)

  def sucessor(self, root):
        root = root.right.root
        if root != None:
            while root.left != None:
                if root.left.root is None:
                    return root
                else:
                    root = root.left.root
        return root


  def delete (self, key):

    if self.root is not None:
        if self.root.key == key:
            if (self.root.left.root is None) and (self.root.right.root is None):
                self.root = None
            elif self.root.left.root is None:

                self.root = self.root.right.root
            elif self.root.right.root is None:

                self.root = self.root.left.root
            else:
                sucessor = self.sucessor(self.root)
                if sucessor is not None:
                    self.root.key = sucessor.key
                    self.root.right.delete(sucessor.key)
            return
        elif key < self.root.key:
            self.root.left.delete(key)
        elif key > self.root.key:
            self.root.right.delete(key)
    else:
      pass

