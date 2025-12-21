import os
import urllib.request
import pytest

DATA_PATH = "data/cyber_incidents_simulated.csv"
# Alternative URLs in order of preference
DATA_URLS = [
    "https://github.com/texasbe2trill/AlertSage/releases/download/v1.0/cyber_incidents_simulated.csv",
    # Fallback: generate minimal test data if download fails
]


def ensure_data():
    """Download dataset if it doesn't exist locally."""
    if not os.path.exists(DATA_PATH):
        print(f"Dataset not found at {DATA_PATH}, downloading...")
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        # Try to download from available URLs
        for url in DATA_URLS:
            try:
                print(f"Attempting to download from {url}")
                urllib.request.urlretrieve(url, DATA_PATH)
                print(f"Dataset downloaded to {DATA_PATH}")
                return
            except Exception as e:
                print(f"Failed to download from {url}: {e}")
                continue

        # If all downloads fail, create minimal test data
        print("All download attempts failed. Creating minimal test data...")
        create_minimal_test_data()


def create_minimal_test_data():
    """Create minimal test data if download fails."""
    import csv

    minimal_data = [
        ["incident_id", "title", "description", "severity", "category"],
        [
            "INC-001",
            "Test Incident",
            "This is a test incident for CI/CD",
            "Medium",
            "Security Alert",
        ],
        [
            "INC-002",
            "Another Test",
            "Another test incident",
            "High",
            "Malware Detection",
        ],
    ]

    with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(minimal_data)
    print(f"Created minimal test data at {DATA_PATH}")


@pytest.fixture(scope="session", autouse=True)
def setup_data():
    """Pytest fixture to ensure data is available before running tests."""
    ensure_data()
    yield
    # Optional: cleanup code here if needed
