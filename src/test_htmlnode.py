import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "greeting"})
        #expected_html = '<div class="greeting">Hello, World!</div>'
        with self.assertRaises(NotImplementedError):
            node.to_html()
        #self.assertEqual(node.to_html(), expected_html)
    
    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "greeting"})
        expected_props = 'class="greeting"'
        self.assertEqual(node.props_to_html(), expected_props)
    
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "greeting"})
        expected_repr = 'TextNode(div, Hello, World!, [], {\'class\': \'greeting\'})'
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()