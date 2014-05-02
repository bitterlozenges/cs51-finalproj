# calculates frechet distance between two curves defined by a list
# of coordinates in R^2 
def frechet(song, hum, starts, octave=0):

	# calculates euclidean distance in R^2
	def euclid(p1,p2):
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)

	# octave displacement
	def octave_displace(tick, octave):
		return (tick[0],tick[1] + (octave * 12))

	frechet_list = []
	# iterate over the hum list and calculate euclidean distance between
	# hum and every point in the song
	# frechet distance is the sum of the infs of these values
	# iterate over every start in the song
	for start in starts:
		# if the hum is longer than the length of the song from the start to
		# to the end, then we cannot compare
		song_clip = song[start:(len(song)-1)]
		if len(hum) > len(song_clip):
			continue
		# store a list of minimum euclidean distances between each point in
		# the hum and every point in the song; the sum of the min_list will 
		# therefore be the frechet distance	
		min_list = []
		for tick_h in hum:
			if not octave = 0:
				tick_h = (tick_h[0],octave_displace(tick_h[1]))
			min_val = euclid(tick_h,song_clip[0])
			# iterate over song list to calculate minimum euclidean distance
			for tick_s in song_clip:
				new_dist = euclid(tick_h,tick_s)
				if new_dist < min_val:
					min_val = new_dist
			min_list.append(min_val)
		frechet_list.append(sum(min_list))
	# return the minimum frechet value for a hum matched to each section
	# of a song
	return min(frechet_list)

def frechet_plain(song,hum):
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

#tests
l1 = [(0,0),(1,1),(2,2)]
l2 = [(0,0),(1,.5),(2,1),(3,1.5),(4,2)]
l3 = [(1,.5),(2,1),(3,1.5),(4,2)]
starts = [0,1]

frechet_plain(l2,l1)
frechet_plain(l3,l1)
frechet(l2,l1,starts)



		

