from concurrent import futures


# Creating a list of expressions. Some will raise a ZeroDivision exception
expressions = ['1 + 1', '2 + 3', '4 / 0', '5**200', '3 / 0', '100*100', '2**8']

# This will evaluate the expressions in sequence. It will halt on errors
#for expression in expressions:
#    eval(expression)

def evaluate(expression):
    try:
        print(eval(expression))
    except:
        print('Error')


executor = futures.ThreadPoolExecutor(max_workers=2)
results = executor.map(evaluate, expressions)
print(len(list(results)))
