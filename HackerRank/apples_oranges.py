#Apple and Orange




s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

num_apples = [a +  x for x in apple]
num_orange = [b + x for x in orange]

#print(num_apples , num_orange)

apple_range = [x for x in num_apples if x >= s and x <= t]
orange_range = [x for x in num_orange if x >= s and x <= t]
print(len(apple_range))
print(len(orange_range))