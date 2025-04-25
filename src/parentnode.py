from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children=[], props=None):
        super().__init__(tag, None, children, props)
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        self.tag = tag
        if children is None:
            raise ValueError("ParentNode must have at least one child")
        self.children = children

    def to_html(self):
        return f"<{self.tag} {self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"