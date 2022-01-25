from parameterized import parameterized
from unittest import TestCase, mock

from .lottery import count_duplicates, generate


class LotteryCountDuplicatesTestCase(TestCase):

    def test_counting_duplicates(self):
        self.assertEqual(0, count_duplicates([]))
        self.assertEqual(0, count_duplicates([1]))
        self.assertEqual(1, count_duplicates([1, 1]))
        self.assertEqual(1, count_duplicates([1, 1, 2]))
        self.assertEqual(2, count_duplicates([1, 1, 2, 2]))
        self.assertEqual(2, count_duplicates([1, 1, 2, 2, 2]))


class LotteryGenerateTestCase(TestCase):

    @mock.patch('src.lottery.randint')
    def test_only_one_value(self, randint_mock):
        randint_mock.side_effect = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertListEqual(generate(), [1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(8, randint_mock.call_count)

    @mock.patch('src.lottery.randint')
    def test_skip_more_duplicates(self, randint_mock):
        randint_mock.side_effect = [1, 1, 2, 2, 3, 3, 4, 5, 6]
        self.assertListEqual(
            generate(allowed_duplicates=2),
            [1, 1, 2, 2, 3, 4, 5, 6],
        )
        self.assertEqual(9, randint_mock.call_count)

    @mock.patch('src.lottery.randint')
    def test_ascending_order(self, randint_mock):
        randint_mock.side_effect = [4, 3, 2, 1]
        self.assertListEqual(generate(num=4), [1, 2, 3, 4])
        self.assertEqual(4, randint_mock.call_count)

    def test_empty_list_for_negative_num_parameter(self):
            self.assertListEqual(generate(num=-1), [])

    @parameterized.expand([
        (2, 1, 1),
        (3, 1, 2),
        (4, 1, 3),
    ])
    def test_prevent_infinity_loop(self, num, min, max):
            with self.assertRaises(AssertionError):
                generate(num=num, min=min, max=max, allowed_duplicates=0)
