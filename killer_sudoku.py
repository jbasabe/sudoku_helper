N = 9 # Number of digits 1~N
ALL_ONES = (1<<N)-1
ALL_COMBINATIONS = list(range(ALL_ONES,0,-1))

def getCombinations(target, n_cells, mask_including, mask_excluding):
	mask_common = ALL_ONES # 0b000000000 -> 987654321
	mask_possible = 0
	
	
	for c in ALL_COMBINATIONS:
		if (c & mask_including) == mask_including and (c & mask_excluding) == 0 and bin(c).count('1') == n_cells and getSum(c) == target:
			print(bin2digits(c))
			mask_common &= c
			mask_possible |= c
	print("\nPossible digits:",bin2digits(mask_possible))
	print("Must have:", bin2digits(mask_common & mask_possible)) # Prevents 1~9 if no c was found

def getSum(x):
	s = 0
	i = 1
	while x > 0:
		s += i * (x&1)
		i += 1
		x >>= 1
	return s

def bin2digits(x):
	digits = []
	i = 1
	while x > 0:
		if (x&1) == 1:
			digits.append(i)
		i += 1
		x >>=1
	return digits

def str2mask(x):
	if x == '':
		return 0
	mask = 0
	x = list(map(int, x.split(' ')))
	for digit in x:
		# {0, 1}^N
		# N N-1 ... 2 1
		mask |= 1<<(digit-1)
	return mask

exit = False
while not exit:
	target = int(input("\n\ntarget: "))
	n_cells = int(input("# cells: "))
	mask_including = str2mask(input("including: "))
	mask_excluding = str2mask(input("excluding: "))
	print('')
	
	getCombinations(target, n_cells, mask_including, mask_excluding)
	exit = input("\nexit? [y/n]: ").lower() == 'y'