import math

class Vector2(object):
	def __init__(self, x=0, y=0):
		self.__x = x
		self.__y = y
		
		if hasattr(x, "__getitem__"):
			x, y, = x
			self._v = [float(x), float(y)]
		else:
			self._v = [float(x), float(y)]
		
	# Para debug, retorna composição do vetor: Vector2(0, 0)	
	def __repr__(self):
		return('Vector2({0}, {1})'.format(self.__x, self.__y))
	
	def __getitem__(self, index):
		return self._v[index]
		
	def __setitem__(self, index, value):
		self._v[index] = 1.0 * value
		
	# rhs: Right Hand Side (lado direito)
	def __add__(self, rhs):
		return Vector2(self.__x + rhs.x, self.__y + rhs.y)
		
	def __sub__(self, rhs):
		return Vector2(self.__x + rhs.x, self.__y + rhs.y)
		
	def __mul__(self, scalar):
		return Vector2(self.__x * scalar, self.__y * scalar)
		
	def __truediv__(self, scalar):
		return Vector2(self.__x / scalar, self.__y * scalar)
		
	def __neg__(self):
		return Vector2(-self.__x, -self.__y)
		
	def __str__(self):
		return '{0}, {1}'.format(self.__x, self.__y)
		
	def points(p1, p2):
		return Vector2(p2[0] - p1[0], p2[1] - p1[1])
		
	def magnitude(self):
		return math.sqrt(self.__x**2 + self.__y**2)
		
	def normalize(self):
		m = self.magnitude()
		try:
			self.__x /= m
			self.__y /= m
		except ZeroDivisionError:
			self.__x = 0
			self.__y = 0

if __name__ == "__main__":
	# testes
	A = (10.0, 20.0)
	B = (30.0, 35.0)
	AB = Vector2.points(A, B)
	print('Vector AB [20.0, 15.0]:', AB)
	print('Magnetude do Vector é [25.0]:', AB.magnitude())
	AB.normalize()
	print('Vector AB Normalize é [0.8, 0.6]:', AB)
	