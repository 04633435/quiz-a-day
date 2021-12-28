import random

# my solution
class solution1:
    def longest_dup_substring(self, input_string):
        length = len(input_string)
        # strhash for the input string
        p = 31
        m = 1e9 + 7
        p_pow = 1
        h_val = 0
        h_val_lst = []
        for i in range(length):
            h_val = (h_val + (ord(input_string[i]) - ord('a') + 1) * p_pow) % m
            h_val_lst.append(h_val)
            p_pow = (p_pow * p) % m
        count_matrix = [[0] * length] * length # space comsuming
        # traverse the start point
        for i in range(length):
            for j in range(i, length):
                target_len = len(input_string[i, j])
                target_h_val = h_val_lst[j-1] - h_val_lst[i-1]
                # find the potential duplicated string
                s_pt = j-1
                while((s_pt + target_len) <= j):
                    h_val = h_val_lst[s_pt + target_len] - h_val_lst[s_pt - 1]
                    if (h_val == target_h_val):
                        # count += 1
                        # update the start points
                        pass
        # find the maximun count in matrix
        max_count = max(count_matrix)
        if max_count == 0:
            return ''
        else:
            # find the index of the max_count
            pass 


# The correct direction is using str hashing for efficiently finding the duclicatied strings.
# What I didnt took into account is starting the searching from the longest duplicated string, whihc
# will reduce the searching space.

# solution 2 binary search + str hashing
class solution2:
    p = 31
    mod = 1e9 + 7
    def longest_dup_substring(self, input_str):
        length = len(input_str)
        # encoding for the elements of a string
        ord_arr = [ord(ele) - ord('a') + 1 for ele in input_str]
        # str hash
        strhash = []
        h_val = 0
        p_pow = 1
        for i in range(length):
            h_val = (h_val + ord_arr[i] * p_pow) % self.mod
            p_pow = (p_pow * self.p) % self.mod
            strhash.append(h_val)
        # binary search
        l, r = 1, length
        start, ret_length = -1, 0
        while l <= r:
            m = l + (r - l) // 2
            idx = self.check(m, strhash, ord_arr)
            if idx != -1:
                ret_length = m
                start = idx
                l = m + 1
            else:
                r = m - 1
        return input_str[start:start+ret_length] if start != -1 else ""

    
    def check(self, middle, strhash, ord_arr):
        n = len(strhash)
        target_hash_val = strhash[middle-1]
        # print(f"mod : {target_hash_val % self.mod}")
        seen = {target_hash_val}
        for i in range(1, n- middle + 1):
            # hash_value = (strhash[i + middle - 1] - strhash[i - 1]) % self.mod
            # power = i - 0
            # p_ = pow(self.p, power)
            b_hash_val = 0
            b_p_pow = 1
            for j in range(i, i + middle):
                b_hash_val = (b_hash_val + ord_arr[j] * b_p_pow) % self.mod
                b_p_pow = (b_p_pow * self.p) % self.mod
            # compare_hash_val = target_hash_val * p_
            if (b_hash_val in seen):
                return i
            seen.add(b_hash_val)
        return -1

# leetcode solution
class solution3:
    def longestDupSubstring(self, s: str) -> str:
        # 生成两个进制
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        # 生成两个模
        mod1, mod2 = random.randint(10**9+7, 2**31-1), random.randint(10**9+7, 2**31-1)
        n = len(s)
        # 先对所有字符进行编码
        arr = [ord(c)-ord('a') for c in s]
        # 二分查找的范围是[1, n-1]
        l, r = 1, n-1
        length, start = 0, -1
        while l <= r:
            m = l + (r - l + 1) // 2
            idx = self.check(arr, m, a1, a2, mod1, mod2)
            # 有重复子串，移动左边界
            if idx != -1:
                l = m + 1
                length = m
                start = idx
            # 无重复子串，移动右边界
            else:
                r = m - 1
        return s[start:start+length] if start != -1 else ""

    def check(self, arr, m, a1, a2, mod1, mod2):
        n = len(arr)
        aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = (h1 * a1 + arr[i]) % mod1
            h2 = (h2 * a2 + arr[i]) % mod2
        # 存储一个编码组合是否出现过
        seen = {(h1, h2)}
        for start in range(1, n - m + 1):
            h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
            # 如果重复，则返回重复串的起点
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        # 没有重复，则返回-1
        return -1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-0i9rd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    s = solution2()
    input_str = "unuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczxunuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczx"
    print(s.longest_dup_substring(input_str))