class Solution:
    def slowest_key(self, releasetimes, keyspressed):
        n = len(releasetimes)
        char_pressed_time = {char: 0 for char in keyspressed}
        for i in range(n):
            if i == 0:
                pressed_time = releasetimes[i]
            else:
                pressed_time = releasetimes[i] - releasetimes[i-1]
            if pressed_time > char_pressed_time[keyspressed[i]]:
                char_pressed_time[keyspressed[i]] = pressed_time
        max = 0
        for i in char_pressed_time.keys():
            if char_pressed_time[i] > max:
                max = char_pressed_time[i]
        ret = []
        for i in char_pressed_time.keys():
            if char_pressed_time[i] == max:
                ret.append(i)
        return sorted(ret)[-1]



if __name__ == '__main__':
    s = Solution()
    releasetimes = [9,29,49,50]
    keyspressed = "cbcd"
    print(s.slowest_key(releasetimes, keyspressed))