def rotateString(s, goal):
    for _ in range(len(s)):
        front=s[0]
        left=s[1:]
        s=left+front
        if s==goal:
            return True
    return False

'''
Testcase 3. 
Input: s = "abcde", goal = "abcde"
Output: True
'''
print(rotateString("abcde", "abcde"))