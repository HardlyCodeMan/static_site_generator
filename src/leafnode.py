from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=str, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        if not isinstance(self.value, str):
            raise TypeError("Value must be a string")
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"