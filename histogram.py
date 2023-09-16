class Histogram:
    def __init__(self):
        """
        Initialize a Histogram object.

        Attributes:
        - intervals (list): Stores the intervals for the histogram.
        - outliers (list): Stores samples that are outside of any interval.
        - frequency (list): Stores the count of samples in each interval.
        - sample_count (int): Total count of valid samples.
        - sample_sum (float): Sum of valid samples.
        - sample_squared_sum (float): Sum of squares of valid samples.
        - mean (float): Sample mean.
        - variance (float): Sample variance.
        """
        self.intervals = []
        self.outliers = []
        self.frequency = []
        self.sample_count = 0
        self.sample_sum = 0
        self.sample_squared_sum = 0
        self.mean = 0
        self.variance = 0

    def check_consistency(self, intervals):
         """
        Validate and set the intervals for the histogram.

        Args:
        - intervals (list of tuples): List of interval tuples, e.g., [(start1, end1), (start2, end2), ...]

        Raises:
        - ValueError: If intervals are invalid or overlapping.
        """
        intervals.sort(key = lambda x: x[0])
        intervals.sort(key = lambda x: x[1])
        maxi = 0

        for pair in intervals:
            left, right = pair[0], pair[1]
            if left >= right:
                raise ValueError("Invalid interval: start must be less than end")
            elif maxi > left:
                raise ValueError("Overlapping intervals are not allowed")
            else:
                self.intervals.append([left, right])
                maxi = max(maxi, right)

        self.siz = len(self.intervals)
        self.frequency = [0] * self.siz

    def get_total_count(self):
        return len(self.outliers) + self.sample_count

    def sample_insert(self, sample):
         """
        Determine the index of the interval to which a sample belongs.

        Args:
        - sample (float): The sample value.

        Returns:
        - int: Index of the interval (1-based) or 0 for outliers.
        """
        low, high = 0, self.siz - 1
        while low <= high:
            mid = (low + high) // 2
            if self.intervals[mid][0] <= sample <= self.intervals[mid][1]:
                return mid + 1
            elif self.intervals[mid][0] > sample:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    def insertSamples(self, samples):
         """
        Insert a list of samples into the histogram.

        Args:
        - samples (list of floats): List of sample values.
        """
        for sample in samples:
            index = self.sample_insert(sample)
            if index >= 1:
                self.frequency[index - 1] += 1
                self.sample_sum += sample
                self.sample_squared_sum += sample * sample
                self.sample_count += 1
            else:
                self.outliers.append(sample)

    def compute_metrics(self):
        """
        Compute the sample mean and sample variance.
        
        Raises:
        - ValueError: If no samples have been inserted.
        """
        if self.sample_count == 0:
            raise ValueError("No samples inserted")

        self.mean = self.sample_sum / self.sample_count
        self.variance = (self.sample_squared_sum / self.sample_count) - (self.mean * self.mean)

    def metrics(self):
        """
        Generate a metrics report.

        Returns:
        - str: Textual representation of the histogram metrics, including counts, mean, variance, and outliers.
        """
        self.compute_metrics()
        metrics_text = ""
        for i in range(self.siz):
            left, right = self.intervals[i][0], self.intervals[i][1]
            metrics_text += "[{}, {}): {}\n".format(left, right, self.frequency[i])

        metrics_text += "\n"
        metrics_text += "sample mean: {}\n".format(self.mean)
        metrics_text += "sample variance: {}\n".format(self.variance)

        if self.outliers:
            outliers_list = ", ".join(map(str, self.outliers))
            metrics_text += "\noutliers: {}".format(outliers_list)

        return metrics_text
