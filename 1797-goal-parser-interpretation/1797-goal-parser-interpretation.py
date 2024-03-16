class Solution(object):
    def interpret(self, c):
        s=""
        i=0
        while(i<len(c)):

            if c[i:i+4]=="(al)":
                s+="al"
                i+=4

            elif c[i:i+2]=="()":
                s+="o"
                i+=2
            else:
                s+=c[i]
                i+=1
            print(s)
        return s

        """
        :type command: str
        :rtype: str
        """
        