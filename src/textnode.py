from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    HIGHLIGHT = "highlight"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    LINK = "link"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Method that returns True if all of the properties of two TextNode objects are equal.
    # Our future unit tests will rely on this method to compare objects.
    def __eq__(node1, node2):
        if isinstance(node1, TextNode) and isinstance(node2, TextNode):
            return node1.text == node2.text and node1.text_type == node2.text_type and node1.url == node2.url
        return False

    # Method that returns a string representation of the TextNode object. 
    # It should look like this: TextNode(TEXT, TEXT_TYPE, URL)
    def __repr__(node):
        out = f"TextNode({node.text}, {node.text_type}, {node.url})"
        return out