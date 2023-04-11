from src.is_base_64 import is_base_64


class TestWithUString:
    def test_with_string(self):
        assert is_base_64("aGVsbG8gd29ybGQ=") is True

    def test_with_string_with_spaces(self):
        assert is_base_64("aGVsbG8gd29ybGQ= ") is False

    def test_with_string_with_new_line(self):
        assert is_base_64("aGVsbG8gd29ybGQ=\n") is False

    def test_with_string_with_tab(self):
        assert is_base_64("aGVsbG8gd29ybGQ=\t") is False


class TestWithBString:
    def test_with_b_string(self):
        assert is_base_64(b"aGVsbG8gd29ybGQ=") is True

    def test_with_b_string_with_spaces(self):
        assert is_base_64(b"aGVsbG8gd29ybGQ= ") is False

    def test_with_b_string_with_new_line(self):
        assert is_base_64(b"aGVsbG8gd29ybGQ=\n") is False

    def test_with_b_string_with_tab(self):
        assert is_base_64(b"aGVsbG8gd29ybGQ=\t") is False


class TestWithRString:
    def test_with_r_string(self):
        assert is_base_64(r"aGVsbG8gd29ybGQ=") is True

    def test_with_r_string_with_spaces(self):
        assert is_base_64(r"aGVsbG8gd29ybGQ= ") is False

    def test_with_r_string_with_new_line(self):
        assert is_base_64(r"aGVsbG8gd29ybGQ=\n") is False

    def test_with_r_string_with_tab(self):
        assert is_base_64(r"aGVsbG8gd29ybGQ=\t") is False
