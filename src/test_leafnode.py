import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_value_none(self):
        node = LeafNode(tag="div", value=None, props={"class": "greeting"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_value_not_string(self):
        node = LeafNode(tag="div", value=123, props={"class": "greeting"})
        with self.assertRaises(TypeError):
            node.to_html()

    def test_value_empty_string(self):
        node = LeafNode(tag="div", value="", props={"class": "greeting"})
        expected_html = '<div class="greeting"></div>'
        self.assertEqual(node.to_html(), expected_html)