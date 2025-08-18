class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        sorted_s2 = "".join(sorted(s2))
        perm_len = len(s1)
        ptr2 = 0
        curr_str = ""

        if len(s1) == len(s2):
            return sorted_s1 == sorted_s2
        if len(s1) > len(s2):
            return False

        while ptr2 < len(s2):
            while len(curr_str) < perm_len:
                curr_str += s2[ptr2]
                ptr2 += 1
            if "".join(sorted(curr_str)) == sorted_s1:
                return True
            curr_str = curr_str[1:] + s2[ptr2]
            ptr2 += 1
        return "".join(sorted(curr_str)) == sorted_s1
