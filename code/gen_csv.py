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
                rows_csv.append(tmp)
            tmp=[os.path.basename(f.name)[0:-4]]
        else:
            pass
    return rows_csv    

def write_csv(data):
    
    f= open('reviews.csv','w')
    for i in range(len(data)):
        tmp=''
        for j in data[i]:
            tmp+=str(j)+", "
        tmp=str(i)+', '+tmp[0:-2]
        f.write(tmp+'\n')
    '''
    with open('file_reviews.csv','wb') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    '''

def read_all_directory(path):
    final_list=[] 
    os.chdir(path)
    for file in glob.glob("*.dat"):
        data=read_dat(path+file)
        final_list=final_list+data
    write_csv(final_list)
     

def main():
    read_all_directory("/home/ricardo/Scrivania/Tripadvisor/Training/")

if __name__=="__main__":
    main()

