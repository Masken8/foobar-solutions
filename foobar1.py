def solution(x, y):
    xContains = set(x)
    yContains = set(y)

    differentKeys = xContains.symmetric_difference(yContains)
    return differentKeys.pop()