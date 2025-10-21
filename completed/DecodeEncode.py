class Code:
    def encode(self, strs):
        final_str = ""
        for i in strs:
            final_str += str(len(i))+"#"+i

        return final_str

    def decode(self, s):
        final_str = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            final_str.append(s[j+1:j+1+length])
            i = j+1+length
        return final_str


strs = ["Hello", "World"]
new_encoder = Code().encode(strs)
encoded_str = Code().decode(new_encoder)
print(encoded_str)

# I don't even understand how I come up with complicated implementation


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return strs[::-1]

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s[::-1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
