import os

os.chdir(r'C:\Users\student\nawon\SSAFY지원자')

for filename in os.listdir("."): # . 은 현재폴더를 뜻함 파일안의 모든것을 for 문으로 돌리며 filename이라는 이름으로 설정
    #if filename.startswith('SAMSUNG'):
    # new_filename = filename.replace('SAMSUNG', 'SSAFY') 
    # os.rename(filename, new_filename) 

    after_name = filename.replace("SAMSUNG","SSAFY")
    os.rename(filename, after_name)


