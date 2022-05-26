class Solution: # https://www.lintcode.com/problem/659/description
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # to encode I just joined together the strings in the input list separating them with a blank space
        return ' '.join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, state = [], []
        
        # iterate over each char in the string
        for i, s in enumerate(str):
            print(s)
            # if the char is a blank space that means we've got a complete string inside our state
            # we can thus join the state together and append it to the result list
            # after that we clear the list for the next string
            if s == ' ':
                res.append(''.join(state))
                state.clear()
            # in order to return the last string I check if the index is equal to the lenght of the encoded list of strings 
            # this is because after the last character there is no blank space and thus the need for this condition
            elif i == len(str)-1: 
                state.append(s)
                res.append(''.join(state))
            # a normal iteration consists of storing the characters into the state in roder to return them later on
            else:
                state.append(s)

        return res

