from storage.engine import StorageEngine
from struct import pack, unpack, calcsize


class NonExistentKeyError(Exception):
    pass


class AppendOnlyLogStorage(StorageEngine):
    struct_pattern = "LQ"
    header_size = calcsize(struct_pattern)

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def set(self, key: bytes, value: bytes) -> None:
        header, payload = self.write_line(key, value)

        with open(self.filepath, "ab") as f:
            f.write(header + payload + b"\n")

    def get(self, key: bytes) -> tuple[bytes, bytes]:
        with open(self.filepath, "rb") as f:
            for line in f.readlines():
                line = line.rstrip(b"\n")

                line_values = self.read_line(line)

                if line_values[0] == key:
                    return line_values

        raise NonExistentKeyError

    def delete(self):
        raise NotImplementedError

    @classmethod
    def write_line(cls, key: bytes, value: bytes) -> tuple[bytes, bytes]:
        line_header = pack(cls.struct_pattern, len(key), len(value))
        line_payload = (key + value)

        return line_header, line_payload

    @classmethod
    def read_line(cls, line: bytes) -> tuple[bytes, bytes]:
        line_header, line_payload = line[:cls.header_size], line[cls.header_size:]

        if len(line_header) != cls.header_size:
            raise ValueError

        unpacked_values = unpack(cls.struct_pattern, line_header)

        if len(unpacked_values) != 2:
            raise ValueError

        key_size, _ = unpacked_values
        key_data, value_data = line_payload[:key_size], line_payload[key_size:]

        return key_data, value_data

    TOMBSTONE = b"__TOMBSTONE__"

    def get(self, key: bytes) -> tuple[bytes, bytes] | None:
        last_value = None

        with open(self.filepath, "rb") as f:
            for line in f.readlines():
                line = line.rstrip(b"\n")
                line_values = self.read_line(line)

                if line_values[0] == key:
                    last_value = line_values[1]

        if last_value is None or last_value == self.TOMBSTONE:
            return None

        return key, last_value
