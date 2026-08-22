class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number=0
        for i in digits:
            number=number*10+i
        number+=1
        list=[]
        for i in str(number):
            list.append(int(i))
        return list
        