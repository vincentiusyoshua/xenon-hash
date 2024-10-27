from typing import List
import time

def rotl(x: int, r: int) -> int:
    """Rotate left function for 64-bit integers.
    
    Args:
        x (int): Number to rotate
        r (int): Rotation amount
        
    Returns:
        int: Rotated number
    """
    r = r % 64
    return ((x << r) | (x >> (64 - r))) & 0xFFFFFFFFFFFFFFFF

# [Semua fungsi yang sudah ada sebelumnya, ganti nama fungsi lightspeed_hash menjadi xenon_hash]

class XenonHash:
    """XenonHash class for creating cryptographic hash values."""
    
    def __init__(self, debug=False):
        """Initialize XenonHash.
        
        Args:
            debug (bool): If True, prints timing information
        """
        self.debug = debug
        self.PHI = 0x9E3779B97F4A7C15
        self.MIXING_CONSTANTS = [
            0x243F6A8885A308D3, 0x13198A2E03707344,
            0xA4093822299F31D0, 0x082EFA98EC4E6C89,
            0x452821E638D01377, 0xBE5466CF34E90C6C,
            0xC0AC29B7C97C50DD, 0x3F84D5B5B5470917
        ]
    
    def hash(self, message: str) -> str:
        """Generate hash from input message.
        
        Args:
            message (str): Input message to hash
            
        Returns:
            str: 512-bit hash value as hexadecimal string
        """
        return xenon_hash(message)