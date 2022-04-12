# 이상형 찾기 
# 함수 예시 커피를 만드는데 매번 수작업으로 만들다 보니 매번 맛이 달라서
# 커피 머신을 구매했다 머신을 가지고 커피를 만드니까 맛이 매번 똑같았다
# 커피 머선이 함수라고 생각 
# 미리 정의된 작업을 쭉 나열해 놓고
# 필요할때 호출만 하면 됨
# 커피머신의 버튼만 누르면 언제나 똑같은 커피를 만드는 것 처럼
# 함수도 우리가 재료를 넣으면 언제나 똑같이 결과물을 뽑아다 줍니다.

# 함수사용법

#def 함수이름():
# 함수내용을 적는다
# 1. 컵에 물을 담는다   
# 2. 얼음을 넣든다
# 3...

#total_dictionary = {}
#while True:
#    question = input("질문을 입력해주세요 : ")
#    if question == "q":
#        break
#    else:
#        total_dictionary[question] = "" 
#1.사용자에게 입력 받은 key을 question변수를 totaldictionary 키로 만들어 줍니다 
#2. 키랑 벨류는 같이 다녀야 함 그래서 처음에 빈 문자열로 넣었고
#질문은 키에다 넣었고 답변을 벨류에다 넣었음
#for i in total_dictionary:
#    print(i)
#    answer = input("답변을 입력해주세요 : ") # 2. 답변을 입력 받은 뒤에 answer라는 변수에 치환에서 넣었슴 
#    total_dictionary[i] = answer
#print(total_dictionary) 

total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)