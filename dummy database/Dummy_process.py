import psycopg2
import heapq

#Assume we are going to setup a locally hosted database, given that enough space occur in the Rasperry PI
conn = psycopg2.connect("dbname='group project' user='postgres' host='localhost' password=''")
cur = conn.cursor()

#Some model code for dump purpose
#cur.execute("""SELECT * FROM students_post_1897""")
#rows = cur.fetchall()
#print("\nShow me the databases:\n")
#for column in rows:
#    print("   ", column)

#Store the column name for marking purpose
cur.execute("""
SELECT column_name
FROM information_schema.columns
WHERE table_name='students_post_1897'""")
columnnamesnew = cur.fetchall()
# Head_length @ 18
# Head_breadth @ 19
# Head_height @ 20
# Face_iobreadth @ 27

cur.execute("""
SELECT column_name
FROM information_schema.columns
WHERE table_name='students_pre_1897'""")
columnnamesold = cur.fetchall()

# Head_sides @ 22
# Head_fback @ 23


cur.execute("""
SELECT *
FROM students_pre_1897
""")
oldtablesize = cur.rowcount

cur.execute("""
SELECT *
FROM students_post_1897
""")
newtablesize = cur.rowcount

#Return object
class ReturnObjects:
    def set(self, data):
        self.data = data
    #Get the numberth person's data out
    def get(self, number):
        return self.data[number]
    def getall(self):
        return self.data


class LimitedSizeHeap:
    #All the value are ranked by its minus number, so this becomes a fake-max heap wit twisting

    def push(self,thing):
        if len(self.heap)<20:
            heapq.heappush(self.heap, thing)
        else:
            heapq.heappush(self.heap, thing)
            heapq.heappop(self.heap)

    def pop(self):
        return heapq.heappop(self.heap)
    def __init__(self):
        self.heap = []

# Given headlength (approximate profile width),headbreadth, headheight, interocular breadth, and facewidth in cm, find the cloest match set(maximum of 20).
# (if there is more than one, then it will choose the one that it first find)
# A null parameter can be replaced by negative numbers or 0,
# where it would not be searched.
# If all three parameters are empty, then it will retrun None.
# The default return type is a new instance of the above class, with data being the list of tuples (column name, value).
def getClosestRecordSet(headlength, headbreadth, headheight, interocular, facewidth):
    if (headlength<=0 and headbreadth<=0 and headheight<=0 and interocular<=0 and facewidth<=0):
        return None
    delta = 1

    if (headlength>0 or headbreadth>0):
        while True:
           string1 ="""
SELECT *
FROM students_pre_1897
WHERE TRUE """
           if (headbreadth>0):
               string1 = string1 + """ AND (("Head_breadth" < """
               string1 = string1 + str((headbreadth+delta)/2.54)
               string1 = string1 + """ AND "Head_breadth" > """
               string1 = string1 + str((headbreadth-delta)/2.54)
               string1 = string1 + """ )OR ("Head_breadth" is NULL))"""
           if (headlength>0):
               string1 = string1 + """ AND (("Head_length" < """
               string1 = string1 + str((headlength+delta)/2.54)
               string1 = string1 + """ AND "Head_length" > """
               string1 = string1 + str((headlength-delta)/2.54)
               string1 = string1 + """ )OR ("Head_length" is NULL))"""
           cur.execute(string1)
           oldrows = cur.fetchall()
           if (len(oldrows)>20 or len(oldrows)==oldtablesize):
               break
           else:
               delta = delta*2
    
    delta = 1
    
    while True:
        string1 ="""
SELECT *
FROM students_post_1897
WHERE TRUE """
        if (headbreadth>0):
            string1 = string1 + """ AND (("Head_breadth" < """
            string1 = string1 + str((headbreadth+delta)*10)
            string1 = string1 + """ AND "Head_breadth" > """
            string1 = string1 + str((headbreadth-delta)*10)
            string1 = string1 + """ ) OR ("Head_breadth" is NULL))"""
        if (headlength>0):
            string1 = string1 + """ AND (("Head_length" < """
            string1 = string1 + str((headlength+delta)*10)
            string1 = string1 + """ AND "Head_length" > """
            string1 = string1 + str((headlength-delta)*10)
            string1 = string1 + """ ) OR ("Head_length" is NULL))"""
        if (headheight>0):
            string1 = string1 + """ AND (("Head_height" < """
            string1 = string1 + str((headheight+delta)*10)
            string1 = string1 + """ AND "Head_height" > """
            string1 = string1 + str((headheight-delta)*10)
            string1 = string1 + """ ) OR ("Head_height" is NULL))"""
        if (interocular>0):
            string1 = string1 + """ AND (("Face_iobreadth" < """
            string1 = string1 + str((interocular+delta)*10)
            string1 = string1 + """ AND "Face_iobreadth" > """
            string1 = string1 + str((interocular-delta)*10)
            string1 = string1 + """ ) OR ("Face_iobreadth" is NULL))"""
        if (facewidth<0):
            string1 = string1 + """ AND "Face_breadth" < """
            string1 = string1 + str((facewidth+delta)*10)
            string1 = string1 + """ AND "Face_breadth" > """
            string1 = string1 + str((facewidth-delta)*10)
            string1 = string1 + """ ) OR ("Face_breadth" is NULL))"""
        cur.execute(string1)
        newrows = cur.fetchall()
        if (len(newrows)>20 or len(newrows)==newtablesize):
            break
        else:
            delta = delta*2

    indexlist = LimitedSizeHeap()
    if (headlength>0 or headbreadth>0):
        for i in range(0,len(oldrows)):
            currentsd = 0
            if (headlength>0):
                if (oldrows[i][22] == None):
                    currentsd = currentsd + headbreadth ** 2
                else:
                    currentsd = currentsd + (oldrows[i][22] - headbreadth) ** 2
            if (headbreadth>0):
                if (oldrows[i][23] == None):
                    currentsd = currentsd + headlength ** 2
                else:
                    currentsd = currentsd + (oldrows[i][23] - headlength) ** 2
            currentsd = currentsd**0.5
            tuple1 = (-currentsd, i, 'old')
            indexlist.push(tuple1)
    for i in range(0,len(newrows)):
        currnetsd = 0
        if (headlength>0):
            if (newrows[i][18] == None):
                currentsd = currentsd + headlength ** 2
            else:
                currentsd = currentsd + (newrows[i][18] - headlength) ** 2
        if (headbreadth>0):
            if (newrows[i][19] == None):
                currentsd = currentsd + headbreadth ** 2
            else:
                currentsd = currentsd + (newrows[i][19] - headbreadth) ** 2
        if (headheight>0):
            if (newrows[i][20] == None):
                currentsd = currentsd + headheight ** 2
            else:
                currentsd = currentsd + (newrows[i][20] - headheight) ** 2
        if (interocular>0):
            if (newrows[i][27] == None):
                currentsd = currentsd + interocular ** 2
            else:
                currentsd = currentsd + (newrows[i][27] - interocular) ** 2
        if (facewidth>0):
            if (newrows[i][26] == None):
                currentsd = currentsd + facewidth ** 2
            else:
                currentsd = currentsd + (newrows[i][26] - facewidth) ** 2
        currentsd = currentsd**0.5
        tuple1 = (-currentsd, i, 'new')
        indexlist.push(tuple1)

    tobeadd = []

    while (len(indexlist.heap)>0):
        k = indexlist.pop()
        if (k[2]=='new'):
            row = []
            rowdata = newrows[k[1]]
            for i in range(0, len(rowdata)):
                row.append((columnnamesnew[i][0],rowdata[i]))
            tobeadd.append(row)
        else:
            row = []
            rowdata = oldrows[k[1]]
            for i in range(0, len(rowdata)):
                row.append((columnnamesold[i][0], rowdata[i]))
            tobeadd.append(row)
    result = ReturnObjects()
    tobeadd.reverse() #reverse the list
    result.set(tobeadd)
    return result

#Get one person's data given a person's id (an primary key(integer) used in the database)
#If fromwhere = 'old', then it will get the person from pre 1897 database
#If fromwhere = 'new', then it will get the person from post 1897 database
#Otherwise return nothing back
def getPersonDataById(id,fromwhere):
    if (fromwhere != 'new' and fromwhere != 'old'):
        return None
    else:
        if (fromwhere == 'new'):
            string1 = """
SELECT *
FROM students_post_1897
WHERE id = """
            string1 = string1 + str(id)
            cur.execute(string1)
            data = cur.fetchall()
            row = []
            if (data==[]):
                return None
            for i in range(0, len(columnnamesnew)):
                row.append((columnnamesnew[i][0], data[0][i]))
            return row
        else:
            string1 = """
SELECT *
FROM students_pre_1897
WHERE id = """
            string1 = string1 + str(id)
            cur.execute(string1)
            data = cur.fetchall()
            row = []
            if (data==[]):
                return None
            for i in range(0, len(columnnamesold)):
                row.append((columnnamesold[i][0], data[0][i]))
            return row


#unit test: emitted if not needed
#k=getClosestRecordSet(21.3,16.5,25.5,2.8,16)
#print(k.data)
#print(k.get(0))
#print(getPersonDataById(4,'new'))
#print(getPersonDataById(1,'new'))
#print(getPersonDataById(2,'new'))
#print(getPersonDataById(3,'new'))
#print(getPersonDataById(1,'old'))
#print(getPersonDataById(2,'old'))
#print(getPersonDataById(3,'old'))