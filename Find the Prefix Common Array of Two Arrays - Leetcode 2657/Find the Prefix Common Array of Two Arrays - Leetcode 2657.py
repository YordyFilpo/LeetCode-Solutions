class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        if len(A) != len(B):
            return None
        
        setA = set()
        setB = set()

        prefix_array = []
        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            common_numbers = len(setA & setB)
            prefix_array.append(common_numbers)
        
        return prefix_array