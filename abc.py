import mysql.connector as ms
from datetime import date 
from datetime import datetime
mycon=ms.connect(host="localhost", user= 'root', password='shivansh')
cs=mycon.cursor() 
if mycon.is_connected(): 
    cs.execute("create database if not exists TRAVELS; ") 
    cs.execute("use TRAVELS") 
    cs.execute("create table if not exists booking (BOOKING_NO int AUTO_INCREMENT primary key , MODE varchar(10) , DATEOF date ,LOCATION varchar(20) , DESTINATION varchar(20) ,NO_OF_PASSANGERS INT);") 
    cs.execute("create table if not exists passanger_details(BOOKING_NO int, NAME varchar(30) , DOB date , EMAIL_ID varchar(40) , PHONE_NO char(10));")
    cs.execute("create table if not exists preferences(BOOKING_NO int, AIRLINE varchar(20) , A_CLASS varchar(20) , TRAIN_COACH varchar(10) , BUS_SERVICE varchar(20) , BUS_TYPES varchar(10));")
    def deletebooking(): 
        bn=int(input('Enter booking number  : ')) 
        de='delete from booking where BOOKING_NO ={}'.format(bn) 
        cs.execute(de) 
        pd='delete from passanger_details where BOOKING_NO ={}'.format(bn) 
        cs.execute(pd) 
        pf='delete from preferences where BOOKING_NO ={}'.format(bn) 
        cs.execute(pf) 
        mycon.commit() 
        print('Your booking is cancelled') 
    while True: 
        print() 
        
        print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^") 
        print() 
        print('\t\t\tTRANSPORT AGENCY ') 
        print('\t\t\tWELCOME') 
        print() 
        todaydate=date.today() 
        current_time=datetime.now().strftime("%H:%M:%S") 
        print('\t\t',todaydate,'\t',current_time) 
        print() 
        ch=int(input('Please Enter 1-4 for :- 1.BOOKING , 2.BOOKING SLIP ,3.CANCEL BOOKING , 4.EXIT : '))  
        if ch==1: 
            default=0 
            md=int(input("1-Airways , 2-Railways ,3-Roadways ; Please enter 3.CANCEL BOOKING , 4.EXIT : "))  
            if md==1: 
                m='Airways' 
            elif md==2: 
                m='Railways' 
            elif md==3: 
                m='Roadways' 
            d=input('Enter date of travelling in form yyyy-mm-dd : ') 
            location=input('Enter boarding location :') 
            destination=input('Enter destination : ') 
            n=int(input('Enter number of passangers : ')) 
            a="insert into booking values('{}','{}','{}','{}','{}',{})".format(default,m,d,location,destination,n)
            cs.execute(a) 
            mycon.commit() 
            i=cs.lastrowid 
            bn=i 
            print('....................................................................................') 
            print('Kindly enter passanger(s) details') 
            for r in range(0,n): 
                name=input('Enter full name : ') 
                dob=input('Enter date of birth in form yyyy-mm-dd : ') 
                email=input('Enter email id : ') 
                pno=int(input('Enter phone number : ')) 
                b="insert into passanger_details values('{}','{}','{}','{}',{})".format(bn,name,dob,email,pno) 
                cs.execute(b) 
                 
                if n>1 and r!=n-1: 
                    print() 
                    print('Enter next passanger details') 
            print('........................................................................................................') 
            print('Kindly enter your preferences ') 
            if md==1: 
                fa=input('Enter your favourable airline : ') 
                c=input('Enter class you prefer - economy,premium economy,business,first class  : ') 
                x='NULL' 
                y='NULL' 
                z='NULL' 
                w="insert into preferences values('{}','{}','{}','{}','{}','{}')".format(bn,fa,c,x,y,z) 
                cs.execute(w) 
                mycon.commit() 
            elif md==2: 
                fa='NULL' 
                c='NULL' 
                x=input("Enter your coach type - AC/non-AC  : ") 
                y='NULL' 
                z='NULL' 
                w="insert into preferences values('{}','{}','{}','{}','{}','{}')".format(bn,fa,c,x,y,z) 
                cs.execute(w) 
                mycon.commit() 
            elif md==3: 
                fa='NULL' 
                c='NULL' 
                x='NULL' 
                y=input('Enter your preferable bus service  : ') 
                z=input('Enter bus type- AC/non-AC  : ') 
                w="insert into preferences values('{}','{}','{}','{}','{}','{}')".format(bn,fa,c,x,y,z) 
                cs.execute(w) 
                mycon.commit() 
            print() 
            print('............................................................................................') 
            print() 
            print('THANK YOU !') 
            print() 
            print('Your booking number is : ',bn,' ,Kindly note it down for future reference') 
            print() 
            print("you'll receive message of booking within 24 hours on your email and phone number") 
             
        elif ch==2: 
            bnum=int(input('Enter your booking number : ')) 
            b="select * from booking where BOOKING_NO = '{}' ".format(bnum) 
            cs.execute(b) 
            data=cs.fetchone() 
            print('BOOKING DETAILS',data) 
            pd="select * from passanger_details where BOOKING_NO = '{}' ".format(bnum) 
            cs.execute(pd) 
            data=cs.fetchall() 
            for row in data: 
                print('PASSANGER DETAILS',row) 
            pf="select * from preferences where BOOKING_NO = '{}' ".format(bnum) 
            cs.execute(pf) 
            data=cs.fetchone() 
            print('PREFERENCE',data) 
        elif ch==3: 
            deletebooking() 
        elif ch==4: 
            break 
        else: 
            print('INVALID choice , enter a valid choice') 
else: 
    print('Error connecting to MYSQL database') 
mycon.close() 
 

