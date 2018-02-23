from faker import Faker
import random
import numpy as np

fake = Faker()

collegeMen=['Christ\'s','Clare','Corpus Christi','Downing','Emmanuel','Fitzwilliam','Gonville & Caius','Jesus','King\'s',
            'Magdalene','Pembroke','Peterhouse','Queen\'s','Selwyn','Sidney Sussex','St Catharine\'s','St Edmund\'s',
            'St John\'s','Trinity','Trinity Hall']
MenWeights=[541/12717,655/12717,467/12717,623/12717,750/12717,688/12717,719/12717,704/12717,581/12717,
            493/12717,597/12717,370/12717,832/12717,630/12717,506/12717,621/12717,499/12717,
            831/12717,1030/12717,580/12717]

collegeWomen=['Girton','Newnham','Hughes Hall']
WomenWeights=[677/1761,524/1761,560/1761]







with open('pre1897data.csv', 'w') as fw:
    fw.write("DoB_month"+','+"DoB_day"+','+"DoB_year"+','+"Age"+','+"Name"+','+"College"+','+"Sex"+','+ "Eye_Colour"+','+
"Hair_Colour"+','+"Head_length"+','+"Face_breadth"+','+"Face_iobreadth"+'\n' )
    
    for _ in range(100):
        #Name, weighted for males and females
        chanceOfFemale=random.randint(1,100)
        Female=0
        if chanceOfFemale==1:
            firstName=fake.first_name_female()
            Female=1
            Sex='Female'
        else:
            firstName=fake.first_name_male()
            Sex='Male'
        lastName=fake.last_name()
        Name=firstName+" "+lastName

        #College
        if Female:            
            College=np.random.choice(collegeWomen,p=WomenWeights)
        else:
            College=np.random.choice(collegeMen,p=MenWeights)

        

        #Birthday
        DoB_month=random.randint(1,12)
        DoB_day=0
        if DoB_month==2:
            DoB_day=random.randint(1,28) #disregarding leap years
        elif DoB_month==4 or DoB_month==6  or DoB_month==9 or DoB_month==11:
            DoB_day=random.randint(1,30)
        else:
            DoB_day=random.randint(1,31)
        DoB_year= round(np.random.normal(75, 2))
        

        #Age
        Age=97-DoB_year
        

        #Eyes/Hair
        Eyes=['light', 'medium', 'dark']
        eyeWeight=[0.2,0.3,0.5]
        Eye_Colour=np.random.choice(Eyes,p=eyeWeight)

        Hair=['red', 'fair', 'brown', 'dark', 'jet-black']
        hairWeight=[0.1,0.25,0.2,0.2,0.25]
        Hair_Colour=np.random.choice(Hair,p=hairWeight)

                #Head Measurements
        if Female:
            Head_length=round(np.random.normal(186.43, 6.59)/25.4,1)
            Face_breadth=round(np.random.normal(143.5, 5.14)/25.4,1)
            Face_iobreadth=round(np.random.normal(59.2, 3.1)/25.4,1)
        else:
            Head_length=round(np.random.normal(198.58, 5.7)/25.4,1)
            Face_breadth=round(np.random.normal(152.25, 5.15)/25.4,1)
            Face_iobreadth=round(np.random.normal(61.5, 3.8)/25.4,1)            
        

        
        data=str(DoB_month)+','+str(DoB_day)+','+str(DoB_year)+','+str(Age)+','+Name+','+College+','+Sex+','+ Eye_Colour+','+Hair_Colour+','+str(Head_length)+','+str(Face_breadth)+','+str(Face_iobreadth)
        fw.write(data)
        fw.write('\n')
fw.close()


