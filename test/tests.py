import numpy as np
from app.sampler import Sampler
from test_base import TestBase


class TestBasic(TestBase):
    """
    Basic tests
    """

    def test_uniform_small(self):
        """
        Small input with uniform distribution, hardcoded expected distribution
        """
        x = np.arange(10)
        outliers = [-100, 100]
        distr = [0.3, 0.5, 0.2]
        self.check_result(x, outliers, distr)

    def test_uniform_large(self):
        """
        Large input with uniform distribution, linear expected distribution
        """
        x = np.arange(10000)
        outliers = [-100000, 100000]
        distr = np.arange(100)
        self.check_result(x, outliers, distr)

    def test_normal2uniform(self):
        """
        Normal input distribution, uniform expected distribution
        """
        x = np.clip(np.random.randn(100), -1, 1)
        outliers = [-10, 10]
        distr = np.ones(4)
        self.check_result(x, outliers, distr)

    def test_uniform2normal(self):
        """
        Uniform input distribution, normal expected distribution
        """
        x = np.arange(100)
        outliers = [-1000, 1000]
        distr = np.abs(np.random.randn(8))
        self.check_result(x, outliers, distr)

    def test_shuffle(self):
        """
        Check if output is shuffled
        """
        x = np.arange(100)
        distr = np.abs(np.random.randn(8))
        distr = np.array(distr) / sum(distr)
        y1 = Sampler.process(x, distr)
        y2 = Sampler.process(x, distr)
        assert not np.array_equal(np.array(y1), np.array(y2))
