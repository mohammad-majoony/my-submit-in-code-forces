get = lambda x : list(map(int,input().split()))
level = int(input())
littleX = get(":)")
littleY = get(":)")
passes = set(littleX[1:] + littleY[1:])
print("I become the guy." if len(passes) == level else "Oh, my keyboard!")