import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a link node", TextType.LINK, "msn.com")
        node2 = TextNode("This is a link node", TextType.LINK, "yahoo.com")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("x", TextType.LINK, None)
        node2 = TextNode("x", TextType.LINK, "google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()