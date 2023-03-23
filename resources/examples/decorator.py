class Text:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class UnderlineText(Text):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return "<u>" + self.wrapped.render() + "<u>"


class BoldText(Text):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return "<b>" + self.wrapped.render() + "<b>"


text = Text("hello world")
bold = BoldText(text)
underline = UnderlineText(text)
underline_bold = UnderlineText(bold)

text.render()
bold.render()
underline.render()
underline_bold.render()
