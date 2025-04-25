import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[])

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None)

    def test_to_html(self):
        child1 = ParentNode(tag="span", children=[], props={"class": "child1"})
        child2 = ParentNode(tag="p", children=[], props={"class": "child2"})
        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "parent"})
        expected_html = '<div class="parent"><span class="child1"></span><p class="child2"></p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    #def test_to_html_with_children(self):
    #    child_node = LeafNode("span", "child")
    #    parent_node = ParentNode("div", [child_node])
    #    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    #def test_to_html_with_grandchildren(self):
    #    grandchild_node = LeafNode("b", "grandchild")
    #    child_node = ParentNode("span", [grandchild_node])
    #    parent_node = ParentNode("div", [child_node])
    #    self.assertEqual(
    #        parent_node.to_html(),
    #        "<div><span><b>grandchild</b></span></div>",
    #    )