import os
import unittest
from streamlines.read_write import source, EXT_TO_OPEN

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
FIXTURES_DIR = os.path.join(THIS_DIR, "fixtures")


def get_zen_of_python():
    import codecs, sys
    out = sys.stdout
    with open(os.devnull, "w") as tmp_out:
        sys.stdout = tmp_out
        from this import s as zen_of_python
    sys.stdout = out
    return codecs.encode(zen_of_python, 'rot_13')

ZEN_OF_PYTHON = get_zen_of_python()


class SourceTests(unittest.TestCase):
    def test_compressed_versions(self):
        raw_text_path = os.path.join(FIXTURES_DIR, "zen.txt")

        with open(raw_text_path) as fp:
            expected = fp.read()

        result = "".join(source(raw_text_path, compression=None))
        self.assertEqual(expected, result)

        for ext in list(EXT_TO_OPEN) + ['.unk']:
            input_file = raw_text_path + ext
            result = "".join(source(input_file))
            self.assertEqual(expected, result)

        with self.assertRaisesRegexp(AssertionError,
                                     "Unknown compression type."):
            list(source(raw_text_path, compression='badfmt'))  # Hit generator
