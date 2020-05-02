import random
class Symbol():
	def __init__(self, symbol_in):
		self.symbol_in = symbol_in
		self.symbol_out = ""

	# 生成随机的运算符号
	@staticmethod
	def generat_random_symbol():
		arg = "+-×÷"
		# 返回数据
		re_s = random.choice(arg)
		return re_s

	def generat_symbol(self):
		if self.symbol_in == "":
			self.symbol_out = Symbol.generat_random_symbol()
		elif self.symbol_in == "+":
			self.symbol_out = "+"
		elif self.symbol_in == "-":
			self.symbol_out = "-"
		elif self.symbol_in in "*×":
			self.symbol_out = "×"
		elif self.symbol_in in "/÷":
			self.symbol_out = "÷"
		else:
			print("Symbol-self.symbol_in -- 输入错误")
