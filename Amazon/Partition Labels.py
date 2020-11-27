class Solution:
    def partitionLabels(self, S):
        result = []
        unique = list(dict.fromkeys(S))
        first = []
        last = []
        for i in unique:
            first.append(S.index(i))
            last.append(S.rindex(i))
        small = first[0]
        big = last[0]
        for k in range(1, len(unique)):
            if first[k] > big:
                result.append(big - small +1)
                small = first[k]
                big = last[k]
            else:
                if last[k] > big:
                    big = last[k]
        result.append(big - small +1)           
        return result