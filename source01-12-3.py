def get_sum(hand):
	result = 0
	for num in hand:
		result += num
	return result

player_hand = [3,2,13,9]
player_sum = get_sum(player_hand)
print("リストの合計値は",player_sum)
