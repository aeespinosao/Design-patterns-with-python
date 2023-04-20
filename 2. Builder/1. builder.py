class HtmlElement:
    indent_size = 4
    
    def __init__(self, name: str = "", text: str = "") -> None:
        self.name = name
        self.text = text
        self.elements = []
    
    def __str__(self) -> str:
        return self.__str()
    
    def __str(self, indent: int = 0) -> str:
        lines = []
        i = self.__indent(indent)
        lines.append(f'{i}<{self.name}>')
        
        if self.text:
            i1 = self.__indent(indent+1)
            lines.append(f'{i1}{self.text}')
            
        for element in self.elements:
            lines.append(element.__str(indent+1))
            
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    
    def __indent(self, indents) -> str:
        return ' ' * indents * self.indent_size
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)
    
    
class HtmlBuilder:
    __root = HtmlElement()
    
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root.name = root_name
        
    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        
    def add_child_fluent(self, child_name: str, child_text: str):
        self.add_child(child_name, child_text)
        return self
    
    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)
    
text = 'hello'
parts = ['<p>', text, '</p>']
print(' '.join(parts))

words = ['hello', 'world']
parts = ['<ul>']

for word in words:
    parts.append(f'<li>{word}</li>')
parts.append('</ul>')
print(' '.join(parts))

# ordinary non-fluent builder
# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# fluent builder
builder.clear()
builder.add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)