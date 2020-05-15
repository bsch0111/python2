import sys
import psycopg2
import os
def InsertJSON(dir,file_name,insert_object,db_name):
 
    f = open(dir,encoding='UTF8')
    lines = f.read()
    lines = lines.replace('\n', '')
    lines = lines.replace('\t', '')
    lines = lines.replace("'", '')
    #conn = psycopg2.connect("host = 172.17.0.3 dbname=%s user=con.lsware password=100.dpfdptmdnpdj"%db_name)
    conn = psycopg2.connect("host = localhost dbname=%s user=con.lsware password=100.dpfdptmdnpdj"%db_name)

    cur = conn.cursor()
    command="insert into %s (painting_meta) values('%s');" % (insert_object, lines) 
    
    cur.execute(command)
    cur.execute('commit;')
    conn.close()

def InsertAN(path, id,insert_object,db_name):
    conn = psycopg2.connect("host = 172.17.0.3 dbname=%s user=con.lsware password=100.dpfdptmdnpdj"%db_name)
    cur = conn.cursor()
    command = "insert into %s (painting_an_path,painting_id) values('%s','%s');" % (insert_object, path, id)
    cur.execute(command)
    cur.execute('commit;')
    conn.close()

db_name = input("Write_DB name: ")
data_dir= input("Wirte_Directory : ")
db_table= input("Write_DB's Table: ")
#file_list = os.listdir(data_dir)
#print(file_list)
#new_file_list=[]
#for i in file_list:
#    i = int(i)
#    new_file_list.append(i)
#file_list=[]
#new_file_list.sort()
#for i in new_file_list:
#    print(i)
dir_name = os.path.split(data_dir)[-1]
dir_name = int(dir_name)
for (path, dir, files) in os.walk(data_dir):
    for filename in files:
        end = os.path.splitext(filename)[-1]
        print(os.path.join(path,filename))
        InsertAN(os.path.join(path,filename),dir_name,db_table,db_name)

#for i in file_list:
#    for (path, dir, files) in os.walk(i):
#        for filename in files:
#            end = os.path.splitext(filename)[-1]
#            print(os.path.splitext(i))
            #InsertAN(os.path.join(path,filename),os.path.splitext(i)[-1],db_table)
#for i in file_list:
#    if ".json" in i:
#        file_path = os.path.join(data_dir,i)
#        InsertJSON(file_path,i,db_table)
#        print("Insert %s to %s..."%(file_path,db_table))

#print(file_list)
#p_dir=sys.argv[1]
#p_file_name=sys.argv[2]
#p_insert_object=sys.argv[3]
#print("FilePath : "+p_dir)
#print("FileID : "+p_file_name)
#print(p_dir)
#InsertJSON(p_dir,p_file_name,p_insert_object)