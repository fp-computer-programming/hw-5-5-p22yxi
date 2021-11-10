# Author Yongdong Xi

# Question 1
becut = input("Give me a string")
A = float(len(becut))
a = A / 2 
first_half = becut[0:a]
second_half = becut[a:A]
print(first_half)
print(second_half)

# Question 2
lw = input("enter a 6 letter word.")
q = lw(1)
w = lw(3)
e = lw(5)
print(q, w, e)
r = lw(2)
t = lw(4)
o = lw(6)
print(r, t, o)

# Question 3
word2 = input("Give me a word")
word3 = (word2[::-1])
if word2 == word3 :
    print(word2, 'is palindrome')

