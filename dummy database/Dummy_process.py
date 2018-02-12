import psycopg2


#Assume we are going to setup a local database, given that enough space occur in the Rasperry PI
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

#Return object
class ReturnObjects:
    def set(self,data):
        self.data = data
        

# Given headlength,headbreadth, headheight and interocular breadth in cm, find the cloest match.
# (if there is more than one, then it will choose the one that it first find)
# A null parameter can be replaced by negative numbers,
# where it would not be searched.
# If all three parameters are empty, then it will retrun None.
# The default return type is a new instance of the above class, with data being the list of tuples (column name, value).
def getClosestRecord(headlength, headbreadth, headheight, interocular):
    if (headlength<0 and headbreadth<0 and headheight<0 and interocular<0):
        return None
    delta = 1
    if (headlength>0 or headbreadth>0):
        while True:
           string1 ="""
SELECT *
FROM students_pre_1897
WHERE TRUE """
           if (headbreadth>0):
               string1 = string1 + """ AND "Head_sides" < """
               string1 = string1 + str((headbreadth+delta)/2.54)
               string1 = string1 + """ AND "Head_sides" > """
               string1 = string1 + str((headbreadth-delta)/2.54)
           if (headlength>0):
               string1 = string1 + """ AND "Head_fback" < """
               string1 = string1 + str((headlength+delta)/2.54)
               string1 = string1 + """ AND "Head_fback" > """
               string1 = string1 + str((headlength-delta)/2.54)
           cur.execute(string1)
           oldrows = cur.fetchall()
           if (len(oldrows)>0):
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
            string1 = string1 + """ AND "Head_breadth" < """
            string1 = string1 + str((headbreadth+delta)*10)
            string1 = string1 + """ AND "Head_breadth" > """
            string1 = string1 + str((headbreadth-delta)*10)
        if (headlength>0):
            string1 = string1 + """ AND "Head_length" < """
            string1 = string1 + str((headlength+delta)*10)
            string1 = string1 + """ AND "Head_length" > """
            string1 = string1 + str((headlength-delta)*10)
        if (headheight>0):
            string1 = string1 + """ AND "Head_height" < """
            string1 = string1 + str((headheight+delta)*10)
            string1 = string1 + """ AND "Head_height" > """
            string1 = string1 + str((headheight-delta)*10)
        if (interocular>0):
            string1 = string1 + """ AND "Face_iobreadth" < """
            string1 = string1 + str((interocular+delta)*10)
            string1 = string1 + """ AND "Face_iobreadth" > """
            string1 = string1 + str((interocular-delta)*10)
        cur.execute(string1)
        newrows = cur.fetchall()
        if (len(newrows)>0):
            break
        else:
            delta = delta*2
    sdold = 9999999
    oldindex = -1
    newindex = -1
    sdnew = 9999999
    if (headlength>0 or headbreadth>0):
        for i in range(0,len(oldrows)):
            currentsd = ((oldrows[i][22]-headbreadth)**2+(oldrows[i][23]-headlength)**2)**0.5
            if currentsd<sdold:
                sdold = currentsd
                oldindex = i
    for i in range(0,len(newrows)):
        currentsd = ((newrows[i][18]-headlength)**2+(newrows[i][19]-headbreadth)**2+(newrows[i][20]-headheight)**2+(newrows[i][27]-interocular)**2)**0.5
        if currentsd<sdnew:
            sdnew = currentsd
            newindex = i
    if sdnew<sdold:
        result = ReturnObjects()
        k = []
        for i in range(0,len(columnnamesnew)):
            tup1 = (columnnamesnew[i][0],newrows[newindex][i])
            k.append(tup1)
        result.set(k)
        return result
    else:
        result = ReturnObjects()
        k = []
        for i in range(0,len(columnnamesold)):
            tup2 = (columnnamesold[i][0],oldrows[oldindex][i])
            k.append(tup2)
        result.set(k)
        return result

    
k=getClosestRecord(21.3,16.5,25.5,2.8)
print(k.data)


