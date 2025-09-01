# 任務：
# 1) 完成函式 reverse_words(s) -> 將字串以空白拆分、反轉順序再合併
# 2) 完成函式 count_vowels(s)  -> 回傳母音 (aeiou) 出現次數（不分大小寫）

# TODO: 在此實作 reverse_words

# 將字串以空白拆分、反轉順序再合併
# example:
# input: " hello world       "
# output: "world hello"
def reverse_words(s: str) -> str:
    s_reverse=[]
    for i in range(len(s.split())):
       s_reverse.append(s.split()[0-i-1])
    return ' '.join(s_reverse)
# TODO: 在此實作 count_vowels

# 回傳母音 (aeiou) 出現次數（不分大小寫）
def count_vowels(s: str) -> int:
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1
    return count
print(reverse_words("Hello World")) 