import struct
import zlib
import binascii

def make_png(width, height, rgba_data):
    """Pure Python PNG Generator (Zero dependencies)"""
    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', binascii.crc32(tag + data) & 0xffffffff)
    raw = b''.join(b'\x00' + rgba_data[i*width*4:(i+1)*width*4] for i in range(height))
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b'')

def hex_to_rgba(hex_str, alpha=255):
    hex_str = hex_str.lstrip('#')
    return [int(hex_str[i:i+2], 16) for i in (0, 2, 4)] + [alpha]

def create_16x16_icon(palette, grid_rows):
    data = bytearray(16 * 16 * 4)
    for y in range(16):
        row = grid_rows[y]
        for x in range(16):
            char = row[x] if x < len(row) else ' '
            rgba = palette.get(char, [0, 0, 0, 0])
            idx = (y * 16 + x) * 4
            data[idx:idx+4] = bytes(rgba)
    return make_png(16, 16, bytes(data))

def create_armor_texture(base_hex, detail_hex, accent_hex):
    data = bytearray(64 * 32 * 4)
    c_base = hex_to_rgba(base_hex, 255)
    c_det = hex_to_rgba(detail_hex, 255)
    c_acc = hex_to_rgba(accent_hex, 255)
    c_trans = [0, 0, 0, 0]

    for y in range(32):
        for x in range(64):
            idx = (y * 64 + x) * 4
            pixel = c_trans
            if (16 <= x <= 39 and 16 <= y <= 31) or (40 <= x <= 55 and 16 <= y <= 31):
                if (x + y) % 6 == 0:
                    pixel = c_det
                elif (x + y) % 8 == 0:
                    pixel = c_acc
                else:
                    pixel = c_base
            elif (0 <= x <= 31 and 0 <= y <= 15):
                if y in (6, 7) and x in (10, 11, 20, 21):
                    pixel = c_acc
                elif (x + y) % 5 == 0:
                    pixel = c_det
                else:
                    pixel = c_base
            data[idx:idx+4] = bytes(pixel)

    return make_png(64, 32, bytes(data))

def create_pack_icon(size=128):
    """High-Res 128x128 Omnitrix Emblem for Packs and App Logo"""
    data = bytearray(size * size * 4)
    c_trans = [0, 0, 0, 0]
    c_bg = hex_to_rgba("#030712", 255)
    c_rim_out = hex_to_rgba("#16a34a", 255)
    c_rim_in = hex_to_rgba("#475569", 255)
    c_dial = hex_to_rgba("#0f172a", 255)
    c_black = hex_to_rgba("#020617", 255)
    c_green = hex_to_rgba("#22c55e", 255)
    c_glow = hex_to_rgba("#86efac", 255)
    c_core = hex_to_rgba("#bbf7d0", 255)
    c_node = hex_to_rgba("#94a3b8", 255)

    cx, cy = (size - 1) / 2.0, (size - 1) / 2.0
    r_max = size * 0.48
    r_rim = size * 0.44
    r_dial = size * 0.38
    r_core = size * 0.32

    for y in range(size):
        for x in range(size):
            idx = (y * size + x) * 4
            dx = x - cx
            dy = y - cy
            dist = (dx*dx + dy*dy)**0.5

            if dist > r_max:
                pixel = c_trans
            elif dist > r_rim:
                pixel = c_rim_out
            elif dist > r_dial:
                # 4 Omnitrix faceplate nodes at 45 degree angles
                is_node = (abs(abs(dx) - abs(dy)) < size * 0.04) and (dist > r_dial + 2)
                pixel = c_node if is_node else c_rim_in
            elif dist > r_core:
                pixel = c_dial
            else:
                # Hourglass shape
                # Top triangle: dy < 0 and |dx| < -dy * 0.82
                # Bottom triangle: dy > 0 and |dx| < dy * 0.82
                in_hourglass = False
                if dy < 0 and abs(dx) <= -dy * 0.82:
                    in_hourglass = True
                elif dy > 0 and abs(dx) <= dy * 0.82:
                    in_hourglass = True

                if in_hourglass:
                    if dist < r_core * 0.35:
                        pixel = c_core
                    elif dist < r_core * 0.70:
                        pixel = c_glow
                    else:
                        pixel = c_green
                else:
                    pixel = c_black

            data[idx:idx+4] = bytes(pixel)

    return make_png(size, size, bytes(data))

