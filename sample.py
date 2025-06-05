import re


# words = ["abc","a","a","b","ab","ac"]
words = ["back","backdoor","gammon","blackgammon","comeback","come","door"]

count = 0
for i in range(0,len(words)):
    for j in range(i+1,len(words)):
        print("\n")

        print(f"word[i] : {words[i]} and words[j]: {words[j]}")

        res = re.match(words[i],words[j])
        print("res",res)
        res_opp = re.match(words[j],words[i])
        print("res_opp",res_opp)

        if res is not None or res_opp is not None:
            
            count+=1

print(count)