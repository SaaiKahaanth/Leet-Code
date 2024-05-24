class Solution(object):
    def canConstruct(self, a, b):
        dict={}
        for i in b:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i in a:
            if i in dict and dict[i]>0:
                dict[i]-=1
            else :
                return False
        return True




        if a in b:

            j=b.index(a[0])

            for i in range(len(a)):

                if a[i]!=b[j]:
                    return False
                b.remove(b[j])
            else :
                j+=1

        
        
