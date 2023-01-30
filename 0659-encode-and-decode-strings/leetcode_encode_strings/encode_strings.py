class Solution:
    """
    @param strs: a list of strings
    @return: encodes a list of strings to a string
    """

    delim = "%"

    def encode(self, strs: list[str]) -> str:
        print(strs)
        res = ""

        for str in strs:
            formatted = f"{len(str)}{self.delim}{str}"
            res += formatted

        return res

    """
    @param str: a string encoded
    @return: a list of strings decoded
    """

    def decode(self, str: str) -> list[str]:
        print(str)
        # index forward until delim, that is length of string
        decoded = []
        counting = True
        lengthStr = ""
        length = 0
        currentStr = ""

        for char in str:
            # first chars are length of string until we hit delim
            # while char != self.delim:
            if counting:
                if char != self.delim:
                    lengthStr += char
                else:
                    print("delim", lengthStr)
                    counting = False
                    length = int(lengthStr)
            else:
                print("DECODING!", char)
                if length > 0:
                    currentStr += char
                    length -= 1
                if length == 0:
                    print("string complete")
                    decoded.append(currentStr)
                    currentStr = ""
                    lengthStr = ""
                    counting = True
        print("decoded", decoded)
        return decoded
