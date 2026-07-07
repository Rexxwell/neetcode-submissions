class Solution:
    # Chunking with a Lookup Table
    # If you process a 32-bit number bit-by-bit, it takes 32 operations.
    # If we have to do this millions of times, it would take a lot of operations.
    # Instead of processing 1 operation at a time, we could process 8 bits (1 byte at a time)
    # Since 32 bits is four 8-bit chunks joined together.
    # An 8-bit chunk has 256 possible values.
    # We can pre-calculate the reversed version of all 256 possible 8-bit chunks and save them
    # in a dictionary.
    # When the function gets a 32-bit number, we would slice it to 4 chunks and then
    # immediately look up the reversed version of the chunk in our cache, and
    # combine them together in reverse order.
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(1) or O(4)
    # Space Complexity: O(1) or O(256)
    def __init__(self):
        # This remembers the reversed bytes
        self.cache = {}

    def reverseBits(self, n: int) -> int:
        reverse_n = 0
        
        for i in range(4):
            byte = n & 0xFF
            if byte not in self.cache:
                self.cache[byte] = self.reverseByte(byte)
            
            reverse_n = (reverse_n << 8) | self.cache[byte]
            n >>= 8

        return reverse_n

    def reverseByte(self, byte: int) -> int:
        reverse_byte = 0
        for i in range(8):
            reverse_byte = (reverse_byte << 1) | (byte & 1)
            byte >>= 1
        
        return reverse_byte