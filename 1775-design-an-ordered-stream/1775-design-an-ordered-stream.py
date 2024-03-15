class OrderedStream(object):

    def __init__(self, n):
        self.t=[None]*n
        self.ptr=0

       
        

    def insert(self, idKey, value):
        idKey-=1
        self.t[idKey]=value
        if self.ptr<idKey:
            return []
        else:
            while self.ptr<len(self.t)and self.t[self.ptr]is not None:
                self.ptr+=1
            return self.t[idKey:self.ptr]
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)