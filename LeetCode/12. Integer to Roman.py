class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        outstr=""
        snum = num
        while snum != 0:
            if snum < 4:
                outstr += "I"*snum
                snum = 0
            elif snum == 4:
                outstr += "IV"
                snum = 0
            elif snum < 9:
                outstr += "V"+"I"*(snum-5)
                snum = 0
            elif snum == 9:
                outstr += "IX"
                snum = 0
            elif snum < 40:
                outstr += "X"*(snum//10)
                snum = snum%10
            elif snum < 50:
                outstr += "XL"
                snum = snum-40
            elif snum < 90:
                outstr += "L"
                snum = snum - 50
            elif snum < 100:
                outstr += "XC"
                snum = snum - 90
            elif snum < 400:
                outstr += "C"*(snum//100)
                snum = snum % 100
            elif snum < 500:
                outstr += "CD"
                snum = snum - 400
            elif snum < 900:
                outstr += "D"
                snum = snum - 500
            elif snum < 1000:
                outstr += "CM"
                snum = snum - 900
            else:
                outstr += "M"*(snum//1000)
                snum = snum%1000
        return outstr

a = Solution()
print(a.intToRoman(3))