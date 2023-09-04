import numpy as np

class Sampler:
    @staticmethod
    def process(x, distr):
        mean_x = np.mean(x)
        std_x = np.std(x)
        x = [element for element in x if abs(element - mean_x) <= 2 * std_x]

        target_length = int(len(x) + len(distr))

        bin_edges = np.linspace(min(x), max(x), len(distr) + 1)

        hist_x, _ = np.histogram(x, bins=bin_edges, density=True)

        num_samples_needed = [int(target_length * p) for p in distr]

        y = []

        for i, num_samples in enumerate(num_samples_needed):
            num_elements_needed = max(0, num_samples - len(y))

            indices = np.where((x >= bin_edges[i]) & (x < bin_edges[i + 1]))[0]

            np.random.shuffle(indices)

            y.extend(x[indices[:num_elements_needed]])

        np.random.shuffle(y)

        return y
