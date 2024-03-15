class Solution(object):
    def transpose(self, m):
        
        """MY SOLUTION
        row,col=len(m),len(m[0])
        #res=[[0 for _ range(row)]for _ in range(cols)]
        
        res = [[0 for _ in range(row)] for _ in range(col)]

        
        
        for i in range(0,row):
            for j in range(0,col):
                res[j][i]=m[i][j]
                #print [j,i]
                #print m[i][j]
                row.append(m[i])
            res.append(row)
           # es.append(row)
            row=[]

                
            print("\n")
    
        """
        #METHOD SOLUTION
            
        return list( zip(*m))
        
        """
        #brute force
        row = len(m)
        col = len(m[0])
        result = [[0] * row for _ in range(col)]
        
        for i in range(col):
            for j in range(row):
                result[i][j] = m[j][i]
                
        return result
        
        """
        