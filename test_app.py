import unittest
from app import get_message

class TestApplication(unittest.TestCase):
    def test_message(self):
        self.assertEqual(
            get_message(),
            "Hello from Experiment 13 CI/CD Pipeline!"
        )

    def test_message_is_not_empty(self):
        self.assertTrue(get_message())

if __name__ == "__main__":
    unittest.main()
