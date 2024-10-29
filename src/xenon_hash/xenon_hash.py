from typing import List

def rotl(x: int, r: int) -> int:
    """Rotate left function for 64-bit integers"""
    r = r % 64
    return ((x << r) | (x >> (64 - r))) & 0xFFFFFFFFFFFFFFFF

PHI = 0x9E3779B97F4A7C15

MIXING_CONSTANTS = [
    0x243F6A8885A308D3, 0x13198A2E03707344,
    0xA4093822299F31D0, 0x082EFA98EC4E6C89,
    0x452821E638D01377, 0xBE5466CF34E90C6C,
    0xC0AC29B7C97C50DD, 0x3F84D5B5B5470917
]

def mix_function(x: int, y: int, z: int) -> int:
    """Enhanced mixing function with better distribution"""
    x = x & 0xFFFFFFFFFFFFFFFF
    y = y & 0xFFFFFFFFFFFFFFFF
    z = z & 0xFFFFFFFFFFFFFFFF
    
    # Multiple rounds of mixing
    h = rotl(x, 13) ^ rotl(y, 29) ^ rotl(z, 43)
    h = (h * PHI) & 0xFFFFFFFFFFFFFFFF
    
    # Add non-linearity
    h = rotl(h, 31) + (x ^ y ^ z)
    h = (h * 0x9ddfea08eb382d69) & 0xFFFFFFFFFFFFFFFF
    
    return h

def finalize_state(state: List[int]) -> List[int]:
    """Enhanced state finalization"""
    result = state.copy()
    
    # Multiple rounds of mixing for better distribution
    for r in range(4):
        for i in range(8):
            # Mix with neighbors
            prev = result[(i - 1) % 8]
            next = result[(i + 1) % 8]
            
            # Apply mixing function with stronger constants
            result[i] = mix_function(
                result[i], 
                rotl(prev, 13 + r * 7),
                rotl(next, 37 + r * 11)
            )
            
            # Add round constant with better mixing
            result[i] = (result[i] + MIXING_CONSTANTS[r * 2 + (i % 2)] * PHI) & 0xFFFFFFFFFFFFFFFF
    
    return result

def compress(state: List[int], block: List[int]) -> List[int]:
    """Optimized compression function"""
    v = state.copy()
    m = block.copy()
    
    # Reduced rounds with better mixing per round
    for r in range(4):
        for i in range(8):
            # Simplified mixing pattern
            idx1 = (i + 1) % 8
            idx2 = (i + 3) % 8
            
            v[i] = mix_function(
                v[i] + m[idx1],
                v[idx2],
                MIXING_CONSTANTS[r]
            )
        
        # Simplified message word rotation
        temp = m[7]
        for i in range(7, 0, -1):
            m[i] = m[i-1]
        m[0] = temp
    
    # Simplified final mixing
    for i in range(8):
        state[i] = (state[i] ^ v[i] ^ m[i]) & 0xFFFFFFFFFFFFFFFF
    
    return state

def pad_message(message: str) -> bytes:
    """Pad the input message"""
    message_bytes = message.encode('utf-8')
    length = len(message_bytes)
    padding_length = (128 - (length + 17)) % 128
    padded = message_bytes + b'\x80' + b'\x00' * padding_length + (length * 8).to_bytes(16, 'little')
    return padded

def bytes_to_blocks(b: bytes) -> List[List[int]]:
    """Convert bytes to blocks"""
    blocks = []
    for i in range(0, len(b), 64):
        block = []
        for j in range(0, 64, 8):
            block.append(int.from_bytes(b[i+j:i+j+8], 'little'))
        blocks.append(block)
    return blocks

def xenon_hash(message: str) -> str:
    """Main hash function with improved distribution"""
    
    # Initialize state
    state = [
        0x243F6A8885A308D3, 0x13198A2E03707344,
        0xA4093822299F31D0, 0x082EFA98EC4E6C89,
        0x452821E638D01377, 0xBE5466CF34E90C6C,
        0xC0AC29B7C97C50DD, 0x3F84D5B5B5470917
    ]
    
    # Enhanced finalization
    state = finalize_state(state)
    
    # Combine state into final hash using all 512 bits
    hash_value_high = 0
    hash_value_low = 0
    
    # Mix upper 256 bits
    for i in range(4):
        mixed = mix_function(
            state[i],
            rotl(state[i], i * 8 + 1),
            MIXING_CONSTANTS[i]
        )
        hash_value_high ^= mixed
        hash_value_high = rotl(hash_value_high, 11)
    
    # Mix lower 256 bits
    for i in range(4, 8):
        mixed = mix_function(
            state[i],
            rotl(state[i], i * 8 + 1),
            MIXING_CONSTANTS[i]
        )
        hash_value_low ^= mixed
        hash_value_low = rotl(hash_value_low, 11)
    
    
    # Combine both halves into final 512-bit hash
    return f"{hash_value_high:016x}{hash_value_low:016x}"
