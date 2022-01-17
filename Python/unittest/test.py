# https://wikidocs.net/16107

import unittest
import os


def custom_function(file_name):
    with open(file_name, "rt") as f:
        return sum(1 for _ in f)


# TestCase를 작성
class CustomTests(unittest.TestCase):
    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = "test_file.txt"
        with open(self.file_name, "wt") as f:
            f.write("hey hey hey I am I am \n asd \n hey".strip())

    def tearDown(self):
        """테스트 종료 후 파일 삭제"""
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""

        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)

    def test_no_file(self):
        # with self.assertRaises(IOError):
        # custom_function(self.file_name)
        custom_function("abc.txt")
        # print(custom_function("abc.txt"))


# unittest를 실행
if __name__ == "__main__":
    unittest.main()
