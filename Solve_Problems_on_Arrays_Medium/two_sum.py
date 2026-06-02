class TwoSum(object):
	"""docstring for TwoSum"""
	def __init__(self, n, arg, target):
		super(TwoSum, self).__init__()
		self.n = n
		self.arg = arg
		self.target = target
		self.dic = {}

	# broot force method 
	def two_sum(self):
		for i in range(self.n):
			for j in range(i, self.n):
				result = self.arg[i] + self.arg[j]
				if(result == target):
					return self.arg[i], self.arg[j]
		return "NO"

	# optimal approach 

	def better_two_sum(self):
		for i in self.arg:
			if(i in self.dic[i]):
				return i, self.dic[i]



n = 5
arr= [2,6,5,8,11]
target = 20

two_sum_object = TwoSum(n,arr, target)

print(two_sum_object.two_sum())