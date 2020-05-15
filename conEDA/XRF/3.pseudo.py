import csv
import os
from xlsx2csv import Xlsx2csv


#def extract_15():

#def extract_40():


if __name__ == "__main__":
    # target_file= input("Write Target Directory : \n")
    result_csv_path = "C:/result.csv" # %target_file
    count = 0 # n 행 표시를 위한 변수
    # run xrf_data_pre.py
    #xrf_data_pre.main(target_file)
    # Read csv
    with open(result_csv_path,newline='',encoding="UTF8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #각 행을 읽어서 비교
        fifteen_atm = []
        forty_atm = []
        Ba_atm = []
        save_final = []
        save_final_atm = []
        save_file_name = []
        result_list = []
        filename = ""
        for row in spamreader:
            #첫 행은 value가 아니므로 제외하고 2번째 줄부터 시작
            fifteen = []
            forty = []
            Ba = []
            if count <= 0:
                count += 1
                continue
            elif count == 1:
                row_split = row[1].split(',')
                for j in range(len(row_split)):
                    if j == 0:
                        continue
                    elif j >= 1 and j <=10:
                        fifteen_atm.append(row_split[j])
                    elif j >= 11 and j <=27:
                        forty_atm.append(row_split[j])
                    else :
                        Ba_atm.append(row_split[j])
                count += 1
                continue
            else :
                print("This is row\n")
                row_split = row[1].split(',')
                for j in range(len(row_split)):
                    if j == 0:
                        continue
                    elif j == 1:
                        filename = row_split[j]
                    elif j >= 2 and j <= 11:
                        fifteen.append(int(row_split[j]))
                    elif j >= 12 and j <= 28:
                        forty.append(int(row_split[j]))
                    else :
                        Ba.append(int(row_split[j]))
            #Ba 전처리
            Ba_result = 0
            if Ba[1] / 3 >= (Ba[0] + Ba[2]) / 2:
                Ba_result = 1
            print(row_split)
            print("*********************************************")
            print(filename)
            #print(fifteen_atm)
            #print(fifteen)
            #print(forty_atm)
            #print(forty)
            #print(Ba_atm)
            #print(Ba)
            #make key
            result_dict = {}
            fifteen_dict = []
            forty_dict = []
            #result_dict = dict(zip(fifteen_atm+forty_atm+Ba_atm,fifteen+forty+Ba))
            fifteen_dict = dict(zip(fifteen_atm,fifteen))
            forty_dcit = dict(zip(forty_atm,forty))
            result_dict = dict(zip(fifteen_atm+forty_atm,fifteen+forty))
            print(result_dict)
            print("NOW_PRINT_SORT")
            fifteen.sort(reverse=True)
            forty.sort(reverse=True)
            print(fifteen)
            print(forty)
            fifteen_result = []
            forty_result = []
            for i in range(5):
                fifteen_result.append(fifteen[i])
            for i in range(5):
                forty_result.append(forty[i])
            final=fifteen_result+forty_result
            final_atm = []
            result_count = 0
            for i in final:
                if result_count < 5:
#                    for j in fifteen_dict.keys():
#                        if j == 'Ba' and Ba_result == 0:
#                            continue
                    for j in fifteen_dict.keys():
                        if i == fifteen_dict[j]:
                            final_atm.append(j)
                            result_count += 1
                else:
                    for j in forty_dcit.keys():
                        if i == forty_dcit[j]:
                            final_atm.append(j)
#                for j in result_dict.keys():
#                    if i == result_dict[j]:
#                        final_atm.append(j)
            save_final.append(str(final))
            save_final_atm.append(str(final_atm))
            save_file_name.append(filename)
            print(final_atm)
            print(final)
        f2 = open("C:/huen/extract_resxult.csv", 'w', encoding='utf-8', newline='')
        wr = csv.writer(f2)
        print(save_final_atm)
        print(save_final)
        for i in range(len(save_final)):
            temp = []
            temp.append(save_file_name[i])
            temp.append(save_final_atm[i])
            temp.append(save_final[i])
            result_list.append(temp)
        wr.writerow(["파일명","원소명","에너지값"])
        print(result_list)
        for i in result_list:
            wr.writerow(i)

    # 15 KeV 5개 에너지값, 원소명 추출
    # 40 KeV 5개 에너지값, 원소명 추출
    # 추출 결과 저장