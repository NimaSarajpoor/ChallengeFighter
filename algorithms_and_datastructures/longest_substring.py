# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def naive_GetLongestSubstring(s):
    if len(s) == 0:
        return 0
    else:
        for m in range(len(s), 1, -1):
            for i in range(len(s) - m + 1):
                if len(set(s[i:i+m])) == m:
                    return m
        
        return 1


def GetLongestSubstring(s):
    """
    use `current` to track substring
    """
    positions = dict()
    current = ''
    bsf = 0  # best so far

    # two pointer
    start = 0
    stop = 0
    for right in range(len(s)):
        idx = positions.get(s[right], None)

        if idx is not None and idx >= start:
            start = idx + 1
    
        current = s[start:(right + 1)]
        positions[s[right]] = right
        bsf = max(bsf, len(current))

    return bsf