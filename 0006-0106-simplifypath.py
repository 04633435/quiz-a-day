class Solution:
    def simplify_path(self, path):
        splits = path.split('/')
        folder_names = []
        for name in splits:
            if name != '':
                folder_names.append(name)
        stack = []
        for name in folder_names:
            if name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)



if __name__ == "__main__":
    s = Solution()
    path = "/../"
    print(s.simplify_path(path))
