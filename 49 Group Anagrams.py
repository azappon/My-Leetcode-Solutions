class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap in order to store each string linked with its key (set of character used in the string)
        hashmap = {}
        
        for s in strs:
            # create the key (unique set of character used in the string) 
            key = ''.join(sorted(s))
            
            if key not in hashmap:
                # if we find a new set of unique characters we create a new index in the hashmap with the string
                # i put the string in a list in order to later append more strings with the same key together
                hashmap[key] = [s]
      
            else:
                # if we've already encountered the key we append it together with the other strings sharing the same key
                hashmap[key].append(s)
                
        # simlpy return the values of the hasmap (remember the indexes are the keys!)
        return hashmap.values()
