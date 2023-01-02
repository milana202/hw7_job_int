
# Задание 1
class Stack:
    def __init__(self, stack: str=''):
        self.stack = stack

    def is_empty(self):
        if len(self.stack) > 0:
            res = False
        else:
            res = True
        return res

    def push(self, item):
        self.stack += item

    def pop(self):
        el = self.stack[-1]
        self.stack = self.stack[:-1]
        return el

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Задание 2
    def check_balanced(self):
        closer = ''
        for i in self.stack:
            if i == '(':
                closer += ')'
            if i == '{':
                closer += '}'
            if i == '[':
                closer += ']'

            if i == ')' and closer != '' and closer [-1] == ')':
                closer = closer[:len(closer)-1]
            if i == '}' and closer != '' and closer [-1] == '}':
                closer = closer[:len(closer)-1]
            if i == ']' and closer != '' and closer [-1] == ']':
                closer = closer[:len(closer) - 1]

        if closer == '':
            print('Stack is balanced')
        else:
            print('Stack is unbalanced')


if __name__ == '__main__':

    # Вызов методов к 1 заданию
    stack1 = Stack()
    print(f'Пуст ли stack1 — ', stack1.is_empty())

    stack1.push('f')
    stack1.push('5')
    stack1.push('q')
    stack1.push('8')

    print(f'Пуст ли stack1 — ', stack1.is_empty())
    print(stack1.stack[0:])

    print(f'Удаляю последний элемент — ', stack1.pop())
    print(f'Получаю обновленный стек', stack1.stack[0:])

    print(f'Показываю последний элемент — ', stack1.peek())
    print(f'Стек при этом не меняется — ', stack1.stack[0:])

    print(f'Длина стека — ', stack1.size())

    # Вызов методов ко 2 заданию
    stack2 = Stack('[([])((([[[]]])))]{()}')
    stack3 = Stack('}{{[')

    stack2.check_balanced()
    stack3.check_balanced()




