class Solution(object):
    def partitionString(self, s):
       d={""}
       c=1
       for i in s:
           if i  not in d:
                d.add(i)
           else:
               c+=1
               d.clear()
               d.add(i)
       return c
                  


       