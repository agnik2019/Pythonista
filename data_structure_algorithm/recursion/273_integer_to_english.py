class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        def recur(num):
            to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve "\
                    "Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
            tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
            if num == 0: return ""
            elif num <= 19:
                return to19[num - 1]
            elif num <= 99:
                return (tens[num//10-2]+" "+recur(num%10)).rstrip()
            elif num <= 999:
                return (recur(num // 100)+" Hundred "+recur(num%100)).rstrip()
            elif num <= 10**6-1:
                return (recur(num // 1000)+" Thousand "+recur(num%1000)).rstrip()
            elif num <= 10**9-1:
                return (recur(num // 10**6)+" Million "+recur(num% 10**6)).rstrip()
            else:
                return (recur(num // 10**9)+" Billion "+recur(num% 10**9)).rstrip()
        return recur(num)
                