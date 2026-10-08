import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Welcome",)
        result = node.__repr__()
        self.assertEqual(result, "HTMLNode(h1, Welcome, None, None)")

if __name__ == "__main__":
    unittest.main()