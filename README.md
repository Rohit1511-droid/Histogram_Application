# Histogram_Application
An asynchronous web service containing a Histogram and exposing two asynchronous end-points to manipulate the Histogram and get information about the current state of the Histogram.  When started, this web service will read from an input file whose path is provided by an environment variable.
# Histogram Web Service

This is a web service for managing a histogram with non-overlapping intervals.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository.
2. Create a virtual environment (optional).
3. Install dependencies:


2. Access the web service at `http://localhost:8000`.

### Endpoints

- `POST /insertSamples/`: Insert samples into the histogram.
- `GET /metrics/`: Get current statistics of the histogram.

### Tests

To run unit tests, use pytest:
