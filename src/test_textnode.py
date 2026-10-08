import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.lexus.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.lexus.com"})

    def test_image(self):
        node = TextNode("picture of 2025 lexus is350", TextType.IMAGE, "https://www.lexus.com/is_350_25.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.lexus.com/is_350_25.png", "alt": "picture of 2025 lexus is350"})

    def test_raise(self):
        node = TextNode("", "doesnt_exist")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        
if __name__ == "__main__":
    unittest.main()