import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades

def remove():
    print " In remove"
    query = { "type" : "homework" }
    my_sort = [ ("student_id" , pymongo.ASCENDING ), ("score", pymongo.ASCENDING) ]
    
    try :
        cursor = grades.find(query).sort(my_sort)
    except:
         print "Unexpected error:", sys.exc_info()[0]
    
    prevStudentId = -1
    for student in cursor:
       studentId = student["student_id"]
       if studentId != prevStudentId: # we have a new student
           grades.remove(student)
           prevStudentId = studentId       
       
           
remove()


       
