
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

db=connection.school
students = db.students

def removeLowHomeworkScore():
    print "In removeLowHomeworkScore"

    query = { 'scores':{ '$elemMatch':{ 'type' : 'homework' } } }
    try :
        cursor = students.find(query)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    limit = 0
    for doc in cursor:
        scoreList =  doc['scores']
        #print scoreList
        minScore = 100.0
        for score in scoreList:
            if score['type'] == 'homework':
                #print score['score']
                if score['score'] < minScore:
                    minScore = score['score']
        print doc['name'], minScore
        scoreList.remove({'type': 'homework', 'score': minScore })
        #print scoreList
        try:
            students.save(doc)
        except:
            print "Unexpected error:", sys.exc_info()[0]

         
        
removeLowHomeworkScore()   

