class Book:
  """
  Class: Book contains the details of the book. It allows comparing
  two instances according to the rank.
  for example b1 < b2 if  b1.rank < b2.rank
  """
  def __init__(self, key, title, group, rank, similar):
      self.key = key
      self.title = title
      self.group = group
      self.rank = int(rank)
      self.similar = similar
  def __lt__(self, a):
      """
      This function allows to make direct comparison using the operator <
      between two Book objects based on their ranks
      """
      return self.rank < a.rank
  def __gt__(self, a):
      """
      This function allows to make direct comparison using the operator >
      between two Book objects based on their ranks
      """
      return self.rank > a.rank
  def __str__(self):
      """
      returns a string containing the book information
      """
      return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"
  def getKey(self):
      """
      Returns the key of the book.
      """
      return self.key
  def getTitle(self):
      """
      Returns the title of the book.
      """
      return self.title