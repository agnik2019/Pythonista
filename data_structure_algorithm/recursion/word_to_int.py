def word2integer(s):
    hm = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
	"eleventh":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17,
	"eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, 
	"seventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000, "million":1000000, "billion":1000000000}
    if s == 'zero': return 0
    splits = s.split()
    res, curr = 0, 1
    for sp in splits:
        num = hm[sp.lower()]
        if num>=curr:
            curr *= num
        else:
            res += curr
            curr = num
            
    return res+curr

s = "Three hundred million five thousand forty five"
print(word2integer(s))
s = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
print(word2integer(s))