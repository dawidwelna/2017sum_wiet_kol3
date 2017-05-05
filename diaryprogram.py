#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


import math
import json


class DiaryError(Exception): pass
class OutOfRangeError(DiaryError): pass
class NotIntegerError(DiaryError): pass


def opener(path):
	try:
		with open(path) as data_file:
			data_json = json.load(data_file)
		return data_json
	except IOError:
		raise IOError, "The file does not exist, exiting gracefully"
	
	
def choose_student(diary, k = 9):
	while True:
		try:
			if k == 9:
				print "\nChoose a student from list below" 
				for i in range(3):
					print str(i + 1) + ' ' + diary.data['student'][i]['firstName'] + ' ',
				
				y = input("\nEnter a number: ")
			else:
				y = int(k)
		except ValueError:	
			raise NotIntegerError, "Oops! That was no valid number. Try again..."
		if (0 < y < 4):
			return y
			break
		else:
			raise OutOfRangeError, "The number out of range. Try again.."

			
			
def choose_subject(diary, y, k = 9):
	while True:	
		try:
			if k == 9:
				print "\nChoose a subject from list below" 
				for i in range(3):
					print str(i + 1) + ' ' + diary.data['student'][y-1]['subject'][i]['name'] + ' ',
				
				z = input("\nEnter a number: ")
			else:
				z = int(k)			
		except ValueError:
			raise NotIntegerError, "Oops! That was no valid number. Try again..."			
		if 0<z<4:
			return z
			break
		else:	
			raise OutOfRangeError, "The number out of range. Try again.."
	
	
def grade_student(diary, k = 9):	
	while True:
		try:
			if k == 9:
				grade = int(raw_input())
			else:
				grade = int(k)
		except ValueError:
			raise NotIntegerError, "Oops! That was no valid number. Try again..."	
		if 1<grade<6:
			return grade
			break
		else:
			raise OutOfRangeError, "The number out of range. Try again.."
	
class Diary(object):
	def __init__(self):
				
		self.data = opener('json_file.json')
	
			
	def get_total_avg_score(self): 

		for i in range(3):
			grade = 0
			counter = 0
			for j in range(3):
				for k in range(5):
					if diary.data['student'][i]['subject'][j]['grades'][k] != 0:
						grade += diary.data['student'][i]['subject'][j]['grades'][k]
						counter += 1
			if counter == 0: 
				counter = 1
			print "Student " + 	str(diary.data['student'][i]['firstName']),
			print " avg total grade is " + str(float(grade)/float(counter))
				
	
	def get_class_avg_score(self): 
		
		for i in range(3):
			for j in range(3):
				grade = 0
				counter = 0
				for k in range(5):
					if diary.data['student'][i]['subject'][j]['grades'][k] != 0:
						grade += diary.data['student'][i]['subject'][j]['grades'][k]
						counter += 1
				if counter == 0: 
					counter = 1
				print "Student " + 	diary.data['student'][i]['firstName'] + ' subject: ', 
				print diary.data['student'][i]['subject'][j]['name'] + " avg class grade is " + str(float(grade)/float(counter))
		
	
	

def menu():
	while True:
	
		print "\nOptions: \n" + "%s\n%s\n%s\n%s\n%s\n%s\n%s" % (
			'1. Grade student.',
			'2. Check attendance.',
			"3. Show students average total grade",
			"4. Show students average class score",
			"5. Print out School's current state",
			"6. Save changes.",
			"9. Exit."
		) 
		try:
			x = int(raw_input("\nEnter a number: "))	
		except ValueError:
			x = 5
			print "Oops! That was no valid number. Try again..."
		
		y = 0
		z = 0
		
		if x==9:
			break
		elif x==1:

			y = choose_student(diary)
				
			z = choose_subject(diary, y)
				
			attendance = diary.data['student'][y-1]['subject'][z-1]['attendance']
			print "\nGive student the grade he deserves (range 2-5)>> "
			
			grade = grade_student(diary)
			# while True:
				# try:
					# grade = input()
					# if 1<grade<6:
						# break
					# print "The number out of range. Try again.."
				# except ValueError:
					# print "Oops! That was no valid number. Try again..."
			
			
			diary.data['student'][y-1]['subject'][z-1]['grades'][attendance] = grade
			diary.data['student'][y-1]['subject'][z-1]['attendance'] += 1
		elif x==2:
			if (y == 0):
				y = choose_student(diary)
			if (z == 0):	
				z = choose_subject(diary, y)
			print "The student was present on " + str(diary.data['student'][y-1]['subject'][z-1]['attendance'])				
		elif x==3:
			diary.get_total_avg_score()	
		elif x==4:
			diary.get_class_avg_score()
		elif x==5:
			print json.dumps(diary.data)
		elif x==6:
			with open('data.txt', 'w') as outfile:
				json.dump(diary.data, outfile)
		else:
			print "Error occurred. Please choose the correct option"


			

	
if __name__ == "__main__":
	
	diary = Diary()		
	#diary.choose_student()
	menu()

	
	