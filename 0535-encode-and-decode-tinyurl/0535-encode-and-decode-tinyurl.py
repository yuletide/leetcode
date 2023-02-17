
class Codec:
    def __init__(self):
        self.map = {}
        # self.counter = 0

    def encode(self, longUrl: str) -> str:
        # letters = "abcdefghijklmnopqrstuvwxyz"
        # letters += letters.upper()
        # print(letters)
        """Encodes a URL to a shortened URL.
        Use md5 hash
        """
        hash = longUrl
        self.map[longUrl] = longUrl
        # self.counter += 1
        # encode counter as string 
        return hash
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))