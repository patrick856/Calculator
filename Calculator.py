#!/usr/bin/env python
# coding: utf-8

# In[49]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.num = 0
    
    def push(self,value):
        self.num += 1
        node = Node(value)
        node.next = self.top
        self.top = node
    
    def is_empty(self):
        return self.top is None
    
    def pop(self):
        if self.is_empty():
            print("The stack is already empty")
        else:
            self.num -= 1
            self.top = self.top.next
    
    def peek(self):
        if self.is_empty():
            return
        else:
            return self.top.value
    
    def __str__(self):
        stack_str = ""
        current = self.top
        while current is not None:
            stack_str += str(current.value) + "\n"
            current = current.next
        return stack_str
    def reverse(self):
        stack = Stack()
        for i in range(0,self.num):
            stack.push(self.peek())
            self.pop()
        return stack
        
def solve(equation):
    stack1 = Stack()
    operators = Stack()
    current_number = ""
    for i in equation:
        if i.isdigit():
            current_number += i
        else:
            if current_number:
                    stack1.push(int(current_number))
                    current_number = ""
            if i == ')':
                while operators.is_empty() == 0:
                    if operators.peek() == '(':
                        operators.pop()
                        break
                    stack1.push(operators.peek())
                    operators.pop()
                continue
            elif i != ' ':#------------------------------operators-----------------------
                if operators.is_empty() or values.get(i) > values.get(operators.peek()) or operators.peek() == '(':
                    operators.push(i)
                else:
                    while operators.is_empty() == 0:
                        if values.get(operators.peek()) >= values.get(i) and operators.peek() != '(':
                            stack1.push(operators.peek())
                            operators.pop()
                        else:
                            break
                    operators.push(i)
    if current_number:
            stack1.push(int(current_number))
            current_number = ""
    while operators.is_empty() == 0:
        stack1.push(operators.peek())
        operators.pop()
    stack1 = stack1.reverse()
    calculate = Stack()
    #print(stack1)
    while stack1.is_empty() == 0:
        if isinstance(stack1.peek(),int):
            calculate.push(stack1.peek())
            stack1.pop()
        else:
            operator = stack1.peek()
            stack1.pop()
            int1 = calculate.peek()
            calculate.pop()
            int2 = calculate.peek()
            calculate.pop()
            if operator == '+':
                calculate.push(int1+int2)
            elif operator == '-':
                calculate.push(int2-int1)
            elif operator == '*':
                calculate.push(int1*int2)
            else:
                calculate.push(int2/int1)

    return calculate.peek()    
                
        
values = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 3
}    
equation = input()
answer = solve(equation)
print(answer)

