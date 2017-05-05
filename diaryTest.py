import diaryprogram as dp
import unittest

diary = dp.Diary()

class testOpener(unittest.TestCase):		
	def testOpenerRaise(self):
		"""Opener should fail given incorrect path to file."""
		self.assertRaises(IOError, dp.opener, 'corrupted/path')

class ChooseStudentBadInput(unittest.TestCase):
	def testNotInteger(self):
		"""choose_student should fail when given non integer value"""
		k = 'asd'
		self.assertRaises(dp.NotIntegerError, dp.choose_student, diary, k)

	def testTooLarge(self):
		"""choose_student should fail with large input"""
		k = 4
		self.assertRaises(dp.OutOfRangeError, dp.choose_student, diary, k)	
		
	def testZero(self):
		"""choose_student should fail with 0 input"""
		k = 0
		self.assertRaises(dp.OutOfRangeError, dp.choose_student, diary, k)	

	def testNegative(self):
		"""choose_student should fail with negative input"""
		k = -1
		self.assertRaises(dp.OutOfRangeError, dp.choose_student, diary, k)			
		
		
class ChooseSubjectBadInput(unittest.TestCase):		
	def testNotInteger(self):
		"""choose_subject should fail with non-integer input"""
		k = 'asd'
		self.assertRaises(dp.NotIntegerError, dp.choose_subject, diary, 2, k)
		
	def testTooLarge(self):
		"""choose_subject should fail with large input"""
		k = 4
		self.assertRaises(dp.OutOfRangeError, dp.choose_subject, diary, 2, k)	
	
	def testZero(self):
		"""choose_subject should fail with 0 input"""
		k = 0
		self.assertRaises(dp.OutOfRangeError, dp.choose_subject, diary, 2, k)	

	def testNegative(self):
		"""choose_subject should fail with negative input"""
		k = -1
		self.assertRaises(dp.OutOfRangeError, dp.choose_subject, diary, 2, k)			

class GradeStudentBadInput(unittest.TestCase):
	def testNotInteger(self):
		"""grade_student should fail when given non integer value"""
		k = 'asd'
		self.assertRaises(dp.NotIntegerError, dp.grade_student, diary, k)

	def testTooLarge(self):
		"""grade_student should fail with large input"""
		k = 6
		self.assertRaises(dp.OutOfRangeError, dp.grade_student, diary, k)	
		
	def testZero(self):
		"""grade_student should fail with too small input"""
		k = 1
		self.assertRaises(dp.OutOfRangeError, dp.grade_student, diary, k)	

	def testNegative(self):
		"""grade_student should fail with negative input"""
		k = -1
		self.assertRaises(dp.OutOfRangeError, dp.grade_student, diary, k)				
	
	
if __name__ == "__main__":

	unittest.main()	
	
	
	