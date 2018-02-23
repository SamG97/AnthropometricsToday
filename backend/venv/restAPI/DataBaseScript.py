import psycopg2
import heapq

#Assume we are going to setup a locally hosted database, given that enough space occur in the Rasperry PI
conn = psycopg2.connect("dbname='group project' user='postgres' host='localhost' password='tom'")
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

cur.execute("""
SELECT column_name
FROM information_schema.columns
WHERE table_name='generatedpeople'""")
columnnamesgen = cur.fetchall()

# Head_breadth @ 22
# Head_length @ 23


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

cur.execute("""
SELECT *
FROM generatedpeople
""")
gentablesize = cur.rowcount

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
        if len(self.heap)<self.size:
            heapq.heappush(self.heap, thing)
        else:
            heapq.heappush(self.heap, thing)
            heapq.heappop(self.heap)

    def pop(self):
        return heapq.heappop(self.heap)
    def __init__(self,size):
        self.heap = []
        self.size = size

# Given headlength (approximate profile width), interocular breadth, and facewidth in cm, find the cloest match set(maximum of 20).
# A null parameter can be replaced by negative numbers or 0,
# where it would not be searched.
# If all three parameters are empty, then it will retrun None.
# The default return type is a new instance of the above class, with data being the list of tuples (column name, value).
def getClosestRecordSetOld(headlength, interocular, facewidth):
    if (headlength<=0 and interocular<=0 and facewidth<=0):
        return None
    delta = 1

    if (headlength>0):
        while True:
           string1 ="""
SELECT *
FROM students_pre_1897
WHERE TRUE """
           if (headlength>0):
               string1 = string1 + """ AND (("Head_length" < """
               string1 = string1 + str((headlength+delta)/2.54)
               string1 = string1 + """ AND "Head_length" > """
               string1 = string1 + str((headlength-delta)/2.54)
               string1 = string1 + """ )OR ("Head_length" is NULL))"""
           cur.execute(string1)
           oldrows = cur.fetchall()
           if (len(oldrows)>20 or len(oldrows)==oldtablesize or delta>200000):
               break
           else:
               delta = delta*2
    
    delta = 1
    
    while True:
        string1 ="""
SELECT *
FROM students_post_1897
WHERE TRUE """
        if (headlength>0):
            string1 = string1 + """ AND (("Head_length" < """
            string1 = string1 + str((headlength+delta)*10)
            string1 = string1 + """ AND "Head_length" > """
            string1 = string1 + str((headlength-delta)*10)
            string1 = string1 + """ ) OR ("Head_length" is NULL))"""
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
        if (len(newrows)>20 or len(newrows)==newtablesize or delta>200000):
            break
        else:
            delta = delta*2

    indexlist = LimitedSizeHeap(20)
    if (headlength>0):
        for i in range(0,len(oldrows)):
            currentsd = 0
            if (headlength>0):
                if (oldrows[i][23] == None):
                    currentsd = currentsd + headlength ** 2
                else:
                    currentsd = currentsd + (oldrows[i][23] - headlength) ** 2
            currentsd = currentsd**0.5
            tuple1 = (-currentsd, i, 'old')
            indexlist.push(tuple1)
    for i in range(0,len(newrows)):
        currentsd = 0
        if (headlength>0):
            if (newrows[i][18] == None):
                currentsd = currentsd + headlength ** 2
            else:
                currentsd = currentsd + (newrows[i][18] - headlength) ** 2
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
def getPersonDataByIdOld(id,fromwhere):
    if ((fromwhere != 'new' and fromwhere != 'old') or not isinstance(id, int)):
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



#method for getting data from new table that contains genrated data.
#Excluding malicious input, only accepts integer
def getPersonDataById(id):
    if (not isinstance(id, int)):
        return None
    string1 = """
SELECT *
FROM generatedpeople
WHERE id = """
    string1 = string1+str(id)
    cur.execute(string1)
    data = cur.fetchall()
    row = []
    if (data==[]):
        return None
    for i in range(0, len(columnnamesgen)):
        row.append((columnnamesgen[i][0],data[0][i]))
    return row


#Get all the measurements in the generated people database, and return its id only.
#Returns the returnobject
def getAllMeasurements():
    string1 = """
SELECT *
FROM generatedpeople
"""
    cur.execute(string1)
    data = cur.fetchall()
    row = []
    totaldata = []
    if (data==[]):
        return None
    for i in range(0,len(data)):
        row.append((columnnamesgen[9][0], data[i][9]))
        row.append((columnnamesgen[10][0], data[i][10]))
        row.append((columnnamesgen[11][0], data[i][11]))
        row.append((columnnamesgen[12][0], data[i][12]))
        totaldata.append(row)
        row = []
    k = ReturnObjects()
    k.set(totaldata)
    return k


#New method that does the same thing as above, except only for the dedicated table for generation:
#Returns None if nothing found in the database.
def getClosestRecordSet(headlength, interocular, facewidth):
    if (headlength <= 0 and interocular <= 0 and facewidth <= 0):
        return None

    delta = 1

    while True:
        string1 = """
    SELECT *
    FROM generatedpeople
    WHERE TRUE """
        if (headlength > 0):
            string1 = string1 + """ AND (("Head_length" < """
            string1 = string1 + str((headlength + delta) * 10)
            string1 = string1 + """ AND "Head_length" > """
            string1 = string1 + str((headlength - delta) * 10)
            string1 = string1 + """ ) OR ("Head_length" is NULL))"""
        if (interocular > 0):
            string1 = string1 + """ AND (("Face_iobreadth" < """
            string1 = string1 + str((interocular + delta) * 10)
            string1 = string1 + """ AND "Face_iobreadth" > """
            string1 = string1 + str((interocular - delta) * 10)
            string1 = string1 + """ ) OR ("Face_iobreadth" is NULL))"""
        if (facewidth < 0):
            string1 = string1 + """ AND "Face_breadth" < """
            string1 = string1 + str((facewidth + delta) * 10)
            string1 = string1 + """ AND "Face_breadth" > """
            string1 = string1 + str((facewidth - delta) * 10)
            string1 = string1 + """ ) OR ("Face_breadth" is NULL))"""
        cur.execute(string1)
        newrows = cur.fetchall()
        if (len(newrows) > 20 or len(newrows) == newtablesize or delta>200000):
            break
        else:
            delta = delta * 2

    indexlist = LimitedSizeHeap(5)

    for i in range(0, len(newrows)):
        currentsd = 0
        if (headlength > 0):
            if (newrows[i][9] == None):
                currentsd = currentsd + headlength ** 2
            else:
                currentsd = currentsd + (newrows[i][9] - headlength) ** 2
        if (interocular > 0):
            if (newrows[i][10] == None):
                currentsd = currentsd + interocular ** 2
            else:
                currentsd = currentsd + (newrows[i][10] - interocular) ** 2
        if (facewidth > 0):
            if (newrows[i][11] == None):
                currentsd = currentsd + facewidth ** 2
            else:
                currentsd = currentsd + (newrows[i][11] - facewidth) ** 2
        currentsd = currentsd ** 0.5
        tuple1 = (-currentsd, i, 'new')
        indexlist.push(tuple1)

    tobeadd = []

    while (len(indexlist.heap) > 0):
        k = indexlist.pop()
        row = []
        rowdata = newrows[k[1]]
        for i in range(0, len(rowdata)):
            row.append((columnnamesgen[i][0], rowdata[i]))
        tobeadd.append(row)
    result = ReturnObjects()
    tobeadd.reverse()  # reverse the list
    result.set(tobeadd)
    if (len(result.data)==0):
        return None
    return result



#unit test: emitted if not needed
#k=getClosestRecordSet(21.3,2.8,16)
#print(k.data)
#print(k.get(0))
#print(getPersonDataByIdOld(4,'new'))
#print(getPersonDataByIdOld(1,'new'))
#print(getPersonDataByIdOld(2,'new'))
#print(getPersonDataByIdOld(3,'new'))
#print(getPersonDataByIdOld(1,'old'))
#print(getPersonDataByIdOld(2,'old'))
#print(getPersonDataByIdOld(3,'old'))

#k=getAllMeasurements()
#print(k.data)

#k=getClosestRecordSet(21.3,2.8,16)
#print(k.data)
#print(k.get(0))
#print(getPersonDataById(1))
#print(getPersonDataById(2))
#print(getPersonDataById(3))
#print(getPersonDataById(4))
#print(getPersonDataById(5))
#print(getPersonDataById(6))
#print(getPersonDataById(7))
#print(getPersonDataById('DROP *'))
