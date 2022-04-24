class Codec:
    def __init__(self):
        self.code=[]

    def encode(self, longUrl: str) -> str:
        x = len(self.code)
        self.code.append(longUrl)
        
        
        return x
        
    def decode(self, shortUrl: str) -> str:
       
        return self.code[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))