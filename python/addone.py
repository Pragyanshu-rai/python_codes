class Solution:
    def plusOne(self, numbers):
        carry=False
        add=False
        i=0
        while i<len(numbers):
            if numbers[i] == 0:
                numbers.pop(i)
                i-=1
            else:
                break
            i+=1
        numbers.reverse()
        for index in range(0,len(numbers)):
            if add==True and carry==False:
                break
            elif numbers[index]==9 and (add==False or carry==True):
                numbers[index]=0
                carry=True
            else:
                numbers[index]+=1
                carry=False
                add=True
        if add==False:
            numbers.append(1)
        numbers.reverse()
        return numbers
