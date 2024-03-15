class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        l=["type","color","name"]
        ind=l.index(ruleKey)
        c=0
        for i in range(len(items)):
            if items[i][ind]==ruleValue:
                c+=1
        return c
      
        """

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int res = 0;
        
        for(int i = 0 ;i<items.size();i++){
            if(ruleKey.equals("type") && items.get(i).get(0).equals(ruleValue)) res++;
            if(ruleKey.equals("color") && items.get(i).get(1).equals(ruleValue)) res++;
            if(ruleKey.equals("name") && items.get(i).get(2).equals(ruleValue)) res++;
        }
        
        return res;
        
    }
}"""