class Solution(object):
    def decode(self, e, f):
       r=[]
       r.append(f)
       for i in range(1,len(e)+1):
           
           r.append(r[i-1]^e[i-1])
           
       return r
      