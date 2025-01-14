def hexdump(data, addr=0, num=0):

    lines = []
    if num == 0:
        num = len(data)

    if len(data) == 0:
        return "<empty>"

    for byte_offset in range(0, num, 16):
        line = generate_hex_line(data, addr, byte_offset)

        lines.append(line)
    return "\n".join(lines)


def generate_hex_line(data, addr, byte_offset):

    n = byte_offset + 16

    return (
        generate_address_label(addr, byte_offset)
        + generate_hex_representation(data, n)
        + generate_printable_chars(data, n)
    )


def generate_printable_chars(data, n):
    line = ""
    for j in range(n - 16, n):
        if j >= len(data):
            break
        c = data[j] if not (data[j] < 0x20 or data[j] > 0x7E) else "."
        line += "%c" % c
    return line


def generate_hex_representation(data, n):
    line = ""
    for j in range(n - 16, n):
        if j >= len(data):
            break
        line += "%02x " % (data[j] & 0xFF)
    line += " " * (3 * 16 - len(line)) + " | "
    return line


def generate_address_label(addr, byte_offset):
    return "%04x | " % (addr + byte_offset)


def main():

    with open("python/hexdump/main.py", "rb") as file:
        data = file.read()
        lines = hexdump(data)
        print(lines)


if __name__ == "__main__":
    main()
