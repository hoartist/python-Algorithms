
def ANSWER(R1,S):
    S=S*2
    R1=S-R1

    return R1

R1,S=map(int,input().split())
print(ANSWER(R1,S))
