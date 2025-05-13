# 단 출력
dans = ""
for i in range(2, 10):
    dans += f"#  {i}단  # "
print(dans)

# 계산식 출력
for i in range(1, 10):     # 단의 바깥쪽
    dan = ""
    for j in range(2, 10): # 단
        if(j*i < 10):
            dan += f"{j}X  {i}=  {j*i} "
        else:
            dan += f"{j}X  {i}= {j*i} "
    print(dan)