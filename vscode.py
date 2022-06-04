from IPython.display import clear_output, Image                                    #주피터 스크롤 없애고 사진 첨부하기
import pandas as pd
from csv import writer
import csv, time, random, glob, datetime
# import time
# import random
# import glob
  
def get_dictionary():                                                               #csv파일에서 원하는 값만 사전형으로 만들기
    f = open("new_keyword.csv","r", encoding="utf-8")                               #파일 읽기 
    reader = csv.reader(f)
    for i in reader:                                                               #총 조회수 뽑기
        keywords.append(i[1])                                                      #키워드
        search_volume.append(i[4])
    f.close()

                                                                                   #https://www.delftstack.com/ko/howto/python/python-dictionary-to-csv/
def new_file():                                                                   # 새로운 파일에 저장하기
    with open('dct.csv', 'w', newline='') as f:                                   #with를 사용하면 close를 사용하지 않아도 됨
        writer = csv.writer(f)
        for k, v in total.items():                                                #items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있다.
            writer.writerow([k, v])
            
            
def show_image1():
    a = [s for s in img if r_keyword in s]
    c = str(*a)
    Image("%s" %c)
    pic = display(Image("%s" %c, width = '100px'))
    return pic 
    
def show_image2():
    a = [s for s in img if f_keyword in s]
    c = str(*a)
    pic = display(Image("%s" %c, width = '100px'))
    return pic


def timer():
    sec = int("10")
    while (sec != 0 ):
        sec = sec-1
        time.sleep(0.5)
        print("\t\t\t\t\t\t\t\t\t",clear_output(wait=True) , sec  * '▶')   

def play_time():
    sec = time.time() - start
    times = str(datetime.timedelta(seconds=sec)).split(".")
    p_time= times[0]
    print("게임 진행 시간 : ", p_time)
    

def f_ranking():    
    id_list.append(name)
    score_list.append(score)
    rranking = dict(zip(id_list, score_list))
    
    with open('rank.csv', 'a', newline='',encoding = 'cp949') as f:
        wr = csv.writer(f)
        for a, b in rranking.items():
            wr.writerow([a, b])
        
    want = int(input('top 10을 보시겠어요? \n예 : 1/ 아니요 : 2 :\n'))
    if want == 1:
        with open('rank.csv', 'r',encoding = 'utf8') as f:
            reader = csv.reader(f)
            aslwl = list(reader)[1:]
        print(alswl)     
    else:
        print('게임을 종료합니다.')
        

        
        
#______________________________________________________________________      진짜 실행 코드

keywords = [] #키워드를 넣어라 
search_volume =[] #검색량을 넣어라

id_list = []
score_list = []


# 사진 파일 형식 찾아서 한곳에 모아두기
img_files = glob.glob('image\\*.png')
img_fil = glob.glob('image\\*.jpeg')
img_file = glob.glob('image\\*.jpg')
img = []

for f in img_files:
    img.append(f)
for f in img_file:
    img.append(f)
for f in img_fil:
    img.append(f)

get_dictionary()                                                             #csv파일에서 원하는 값만 사전형으로 만들기

total = dict(zip(keywords,search_volume))                                   # 딕셔너리로 묶기

new_file()                                                                  #새 파일에 넣기

print('게임 설명 ')

name = input("ID를 입력하세요 : ")

start = time.time()                                                      #시간측정❤❤❤❤❤❤❤❤
score = 0
used = []                                                                #랜덤으로 추출된 값을 넣기.(넣어서 중복 키워드 출력 예방)
del keywords[0]                                                          # 키워드 첫 행 지움. 

f_keyword = random.choice(keywords)                                      #첫번째 제시어 랜덤 추출      f_keyword
used.append(f_keyword)                                                   #리스트에 추가
keywords.remove(f_keyword)                                               #키워드 리스트에서 제거
f_value = int(total[f_keyword].replace(',',''))                          # 문자열을 정수로 변환
clear_output(wait=True)                                                 # 화면 초기화


for i in range(len(keywords)):   
    r_keyword = random.choice(keywords)                                  # 랜덤으로 키워드 하나 추출    r_keyword                                                     #이미지 삽입
    r_value = int(total[r_keyword].replace(',',''))                      # 검색량을 비교하기 위해 ','를 제거하고 정수로 만든다.
    keywords.remove(r_keyword)                                           # 키워드 목록을 지운다.
    show_image2()                                                        # 이미지2 출력
    print(f_keyword, total[f_keyword],)                                  # 이미지2와 맞는 키워드 출력
    print('\t vs \t')
    show_image1()                                                        # 이미지1 출력
    print(r_keyword)                                                     # 이미지1과 맞는 키워드 출력

    if f_value < r_value:                                                # 검색량 비교
        result = 0
    elif f_value > r_value:
        result = 1

    if r_keyword not in used:                                            # 새로나온 랜덤값이면
        used.append(r_keyword)                                           # 새로운 리스트에 넣고

        print(r_keyword,total[r_keyword])                                # 키워드 제시어

        user_choice = int(input('1) 더 많다\t 2) 더 적다. \n'))
        clear_output(wait=True)                                         # 출력창 초기화

        if user_choice == 1:                                            # 더 많다
            if result == 0:                                             # 검색량이 더 많으면
                score +=1                                               # 점수 +1
                #print("______________________________________")
                print('\t \t \t 점수 : %d' %score)
                f_keyword = r_keyword                                   # 키워드 초기화 
                f_value = r_value                                       # 검색량 초기화
            else:
                print(r_keyword, total[r_keyword])                      # 키워드의 검색량 출력
                time.sleep(3)                                           # 3초 기다렸다가
                clear_output(wait=True)                                 # 화면 초기화
                play_time()                                             # 게임 진행 시간 
                print('게임 종료 \n{0}님의 총 점수는 {1}입니다.'.format(name, score))   # 마무리 멘트
                f_ranking()
                break

        elif  user_choice == 2:                                         # 더 적다
            if result == 1:                                             
                score += 1                                              # 점수 +1
                #print("______________________________________")
                print('\t \t \t 점수 : %d' %score)
                f_keyword = r_keyword                                    # 키워드 초기화 
                f_value = r_value                                       # 검색량 초기화
            else:                                                       
                print(r_keyword, total[r_keyword])                      # 키워드와 검색량을 보여주기
                time.sleep(3)                                           # 3초 기다렸다가
                clear_output(wait=True)                                # 화면 초기화
                play_time()                                             # 게임 진행 시간 
                print('게임 종료 \n{0}님의 총 점수는 {1}입니다.'.format(name, score))  # 마무리 멘트
                f_ranking()
                break
        else:
            print(r_keyword,"의 검색량은", total[r_keyword],"이었습니다.")                      # 키워드와 검색량을 보여주기
            play_time()
            print('1,2만 누를 수 있습니다. 게임을 종료합니다. 총 점수는 %d 입니다.'%score)
            f_ranking()
            break