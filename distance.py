def frechet(song, hum):
	def euclid(p1,p2):
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)	
	min_list = []
	for tick_h in hum:
		min_val = euclid(tick_h,song[0])
		for tick_s in song:
			new_dist = euclid(tick_h,tick_s)
			if new_dist < min_val:
				min_val = new_dist
		min_list.append(min_val)
	return sum(min_list)











		

