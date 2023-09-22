class AbstractExpression:
    
    @staticmethod
    def interpret(self):
        pass
    

# Terminal expression
class NumberExpression(AbstractExpression):
    
    def __init__(self, value) -> None:
        self.value = float(value)
    
    def interpret(self):
        return self.value
    

# Non terminal Expression
class AlgebraExpression(AbstractExpression):
    
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
class Add(AlgebraExpression):
    
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    
class Substract(AlgebraExpression):
    
    def interpret(self):
        return self.left.interpret() - self.right.interpret()
    
class Multiply(AlgebraExpression):
    
    def interpret(self):
        return self.left.interpret() * self.right.interpret()
    
class Divide(AlgebraExpression):
    
    def interpret(self):
        return self.left.interpret() / self.right.interpret()
    
if __name__ == "__main__":
    target = "3 + 5 - 2 * 7 / 5 + 11"
    
    tokens = target.split()
    
    expressions = []
    
    for i in range(len(tokens)):
        if i == 0:
            expressions.append(NumberExpression(tokens[i]))
        elif tokens[i] == "+":
            expressions.append(Add(expressions.pop(), NumberExpression(tokens[i+1])))
        elif tokens[i] == "-":
            expressions.append(Substract(expressions.pop(), NumberExpression(tokens[i+1])))
        elif tokens[i] == "*":
            expressions.append(Multiply(expressions.pop(), NumberExpression(tokens[i+1])))
        elif tokens[i] == "/":
            expressions.append(Divide(expressions.pop(), NumberExpression(tokens[i+1])))
            
    result = expressions.pop().interpret()
    print(result)
        
        

