class Solution:
    def encode(self, strs: List[str]) -> str:
        resp = []
        for s in strs:
            resp.append(f"{len(s)}#{s}")
        return "".join(resp)

    def decode(self, s: str) -> List[str]:
        resp = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            resp.append(s[i:j])
            i = j

        return resp