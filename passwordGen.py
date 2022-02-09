def password(n):
	import secrets, string as S
	of = secrets.choice
	cats = [S.ascii_lowercase, S.ascii_uppercase, S.punctuation, S.digits]
	cats = cats * 2 + [of(cats) for _ in range(n - 8)]
	for i in range(8):
		j = of(range(i, n))
		cats[i], cats[j] = cats[j], cats[i]
	return ''.join(map(of, cats))
print(password(9))
