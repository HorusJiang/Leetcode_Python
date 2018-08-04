
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right + 1):
            j = i
            flag = 0
            while(j>0):
                if(j%10==0):
                    flag = 1
                    break
                elif(i%(j%10)!=0):
                    flag = 1
                    break
                else:
                    j=j//10
            if(flag==0):
                result.append(i)
        return result