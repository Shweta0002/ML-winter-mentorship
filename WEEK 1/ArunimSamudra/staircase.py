"""staircase.py"""

def main(N):
	for i in range(1,N+1):
		print((N-i)*" "+(i)*"#")


if __name__ == '__main__':
	N = int(input())
	main(N)