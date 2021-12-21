class Solution(object):
    def day_of_year(self, data):
        data_split = data.split('-')
        year, month, date = [int(x) for x in data_split]
        # check leap year
        if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0):
            month_day = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30,
                            7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        else:
            month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        ret = 0
        for i in range(1, month):
            ret += month_day[i]
        ret += date

        return ret
    

if __name__ == '__main__':
    data = "2019-01-09"
    a = Solution()
    print(a(data))