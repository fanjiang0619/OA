class Solution:
    
    def reorderLogFiles(self, logs):
        
        def myFunc(e):
            return [e.split(" ", 1)[1],e.split(" ", 1)[0]]
        
        num = []
        non_num = []
        for i in logs:
            if i.split()[1].isalpha():
                non_num.append(i)
            else:
                num.append(i)
        non_num.sort(key=myFunc)
        
        return non_num+num