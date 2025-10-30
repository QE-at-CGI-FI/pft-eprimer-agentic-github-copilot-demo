# number in integer to text function
def num_to_text(n):
    if n == 0:
        return "zero"

    def one(num):
        switcher = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        return switcher.get(num)

    def ten(num):
        switcher = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }
        return switcher.get(num)

    def helper(num):
        if num == 0:
            return ""
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        elif num < 100:
            return ten(num // 10) + (" " + one(num % 10) if (num % 10 != 0) else "")
        else:
            return one(num // 100) + " hundred" + (" " + helper(num % 100) if (num % 100 != 0) else "")

    billion = n // 1000000000
    million = (n - billion * 1000000000) // 1000000
    thousand = (n - billion * 1000000000 - million * 1000000) // 1000
    remainder = n - billion * 1000000000 - million * 1000000 - thousand * 1000

    result = ""
    if billion != 0:
        result += helper(billion) +