class Solution(object):
    def minimumSum(self, num):
        s1=str(num)
        s = ''.join(sorted(s1))
        print s
        mini=20000000000000000
        for i in range(1,len(s)):
            current_sum=int(s[:i])+int(s[i:])
            print(int(s[:i]),int(s[i:]))
            if current_sum<mini:
                mini=current_sum
                print(mini,current_sum)
        s=s[0]+s[2]+s[1]+s[3]
        
        i=2
        current_sum=int(s[0:2])+int(s[2:])
        print(int(s[:i]),int(s[i:]))
        if current_sum < mini:

            mini=current_sum
            print(mini,current_sum)

        return mini
        """
        :type num: int
        :rtype: int
        """
        