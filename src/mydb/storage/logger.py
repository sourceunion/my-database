from storage.engine import StorageEngine
from struct import pack


class AppendOnlyLogStorage(StorageEngine):
    struct_pattern = "LQ"

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def set(self, key: bytes, value: bytes) -> None:
        header, payload = self.format_log_line(key, value)

        with open(self.filepath, "ab") as f:
            f.write(header + payload + b"\n")

    def get(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    @classmethod
    def format_log_line(cls, key: bytes, value: bytes) -> tuple[bytes, bytes]:
        line_header = pack(cls.struct_pattern, len(key), len(value))
        line_payload = (key + value)

        return line_header, line_payload
