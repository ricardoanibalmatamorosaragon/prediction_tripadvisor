#python ./code/gen_csv.py
import re
import os, glob
import csv
import pandas as pd

def read_dat(name):
    re_newline='\s'
    reader='<No. Reader>'
    helpful='<No. Helpful>'
    overall='<Overall>'
    value='<Value>'
    room='<Rooms>'
    location='<Location>'
    clean='<Cleanliness>'
    check='<Check in / front desk>'
    services='<Service>'
    business='<Business service>'
    f=open(name,'r')
    cont=0
    rows_csv=[]
    tmp=[]   
    for row in f:
        if re.match(reader,row)!=None:
            r=row[12:-1].split()
            tmp.append(int(r[0]))
        
        elif re.match(helpful,row)!=None:
            h=row[13:-1].split()
            tmp.append(int(h[0]))

        elif re.match(overall,row)!=None:
            o=row[9:-1].split()
            overall_tmp=int(o[0])
            tmp.append(int(o[0]))

        elif re.match(value,row)!=None:
            v=row[7:-1].split()
            tmp.append(int(v[0]))
        
        elif re.match(room,row)!=None:
            r=row[7:-1].split()
            tmp.append(int(r[0]))

        elif re.match(location,row)!=None:
            l=row[10:-1].split()
            tmp.append(int(l[0]))
    
        elif re.match(clean,row)!=None:
            c=row[13:-1].split()
            tmp.append(int(c[0]))

        elif re.match(check,row)!=None:
            c=row[23:-1].split()
            tmp.append(int(c[0]))
        
        elif re.match(services,row)!=None:
            s=row[9:-1].split()
            tmp.append(int(s[0]))
            
        elif re.match(business,row)!=None:
            b=row[18:-1].split()
            tmp.append(int(b[0]))


        elif re.match(re_newline,row)!=None:
            if tmp!=[]:
                if overall_tmp < 4:
                    tmp.append('bad')
                else:
                    tmp.append('good')
                rows_csv.append(tmp)
            tmp=[os.path.basename(f.name)[0:-4]]
        else:
            pass
    return rows_csv     

def write_csv_train(data):
    with open("./first_step_prepro/training_initial_assumption.csv","w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(data)

def write_csv_test(data):
    with open("./first_step_prepro/testing_initial_assumption.csv","w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(data)

def read_all_directory(path,option):
    final_list=[] 
    os.chdir(path)
    for file in glob.glob("*.dat"):
        data=read_dat(path+file)
        final_list=final_list+data
    if option ==1:
        write_csv_train(final_list)
    else:
        write_csv_test(final_list)
     

def main():
    #training
    read_all_directory("/home/ricardo/Scrivania/prediction_tripadvisor/Training/",1)
    #testing
    read_all_directory("/home/ricardo/Scrivania/prediction_tripadvisor/Testing/",2)

if __name__=="__main__":
    main()

