import unittest
from compute_stats_refactor import ComputeStatsRefactor


class TestComputeStatsRefactor(unittest.TestCase):

    def test_read_inits(self):
        csr = ComputeStatsRefactor()
        return self.assertIsInstance(csr.read_ints(), list)

    def test_count(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.count(), 1000)

    def test_summation(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.summation(), 499500)

    def test_average(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.average(), 499)

    def test_minimun(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.minimum(), 0)

    def test_maximum(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.maximum(), 999)

    def test_harmonic_mean(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.harmonic_mean(), 129)

    def test_variance(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.variance(), 81476)

    def test_standard_dev(self):
        csr = ComputeStatsRefactor()
        return self.assertEqual(csr.standard_dev(), 285)


if __name__ == '__main__':
    # unittest.TestCase()
    unittest.main(argv=['ignored', '-v'], exit=False)
