# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
	def __init__(self, iterator):
		"""
		Initialize your data structure here.
		:type iterator: Iterator
		"""
		self.iterator=iterator
		self.cache=[]


	def peek(self):
		"""
		Returns the next element in the iteration without advancing the iterator.
		:rtype: int
		"""
		if not self.cache:
			self.cache.append(self.iterator.next())
		return self.cache[0]


	def next(self):
		"""
		:rtype: int
		"""
		if self.cache:
			return self.cache.pop()
		return self.iterator.next()


	def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.cache or self.iterator.hasNext():
			return True
		return False