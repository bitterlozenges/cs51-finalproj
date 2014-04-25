# calculates frechet distance between two curves defined by a list
# of coordinates in R^2 
def frechet(song, hum):

	# calculates euclidean distance in R^2
	def euclid(p1,p2):
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)

	min_list = []
	# iterate over the hum list and calculate euclidean distance between
	# hum and every point in the song
	# frechet distance is the sum of the infs of these values
	for tick_h in hum:
		min_val = euclid(tick_h,song[0])
		# iterate over song list to calculate minimum euclidean distance
		for tick_s in song:
			new_dist = euclid(tick_h,tick_s)
			if new_dist < min_val:
				min_val = new_dist
		min_list.append(min_val)
	return sum(min_list)










		

