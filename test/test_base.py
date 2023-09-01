import numpy as np
from app.sampler import Sampler


class TestBase:
    """
    Base class for tests
    """

    def check_result(self, x, outliers, distr):
        """
        Compare the output distribution with the expected distribution
        """
        x_outliers = np.append(x, outliers)
        distr = np.array(distr) / sum(distr)
        np.random.shuffle(x)
        np.random.shuffle(x_outliers)
        np.random.shuffle(distr)
        y = Sampler.process(x_outliers, distr)
        bins = np.histogram_bin_edges(x, len(distr))
        hist_y, _ = np.histogram(y, bins)
        hist_y = hist_y / sum(hist_y)
        assert abs(len(y) - len(x)) <= len(distr)
        assert np.allclose(distr, hist_y / sum(hist_y), rtol=1 / len(x), atol=1 / len(x))
        assert len(np.unique(y)) >= min(len(distr) + 1, len(np.unique(x)))
