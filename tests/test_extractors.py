import unittest
from src.extractors.network import NetworkExtractor
from src.extractors.process import ProcessExtractor

class TestExtractors(unittest.TestCase):
    def test_network_extractor_structure(self):
        extractor = NetworkExtractor()
        data = extractor.parse_pcap("dummy.pcap")
        self.assertIn("dns_requests", data)
        self.assertIn("remote_ips", data)

    def test_process_extractor_tree(self):
        extractor = ProcessExtractor()
        tree = extractor.parse_proc_tree([])
        self.assertIsInstance(tree, list)
        self.assertTrue(len(tree) > 0)
        self.assertIn("pid", tree[0])

if __name__ == "__main__":
    unittest.main()
