# link: https://leetcode.com/problems/longest-palindromic-substring/

def naive_longestPalindrome(s):
    out = ''
    for m in range(len(s), 0, -1):
        for i in range(len(s) - m + 1):
            sub = s[i : i + m]
            if sub == sub[::-1]:
                out = sub
                return out

    
    return out