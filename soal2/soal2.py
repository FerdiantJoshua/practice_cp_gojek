n = int(input())
answers = [0 for _ in range(n)]
for i in range(n):
	a = int(input())
	b = int(input())
	k = int(input())
	answers[i] = (b//k - (a-1)//k)
	
for i in range(len(answers)):
	print(f'Case {i+1}: {answers[i]}')