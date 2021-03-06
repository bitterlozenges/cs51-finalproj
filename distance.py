# calculates frechet distance between two curves defined by a list
# of coordinates in R^2 
from analyze import compression_factor

# this is python's maximum float val, used to signify hum length > song length
float_max = 1.7976931348623157e+308

# what "bucket" in the song clip we restrict our search for the closet point to
bucket_size = 100 / compression_factor

# We experimented with weighting the distance using constants, but this did not
# affect results significantly
time_weight = 1.0
freq_weight = 1.0

# calculates (weighted) euclidean distance in R^2
def euclid(p1,p2):
	return ( time_weight*(p1[0]-p2[0])**2 + freq_weight*(p1[1]-p2[1])**2 )**(0.5)

def frechet(song, hum, starts):
	frechet_list = []
	# iterate over the hum list and calculate euclidean distance between
	# hum and every point in the song
	# frechet distance is the sum of the infs of these values
	# iterate over every start in the song
	for start in starts:
		# if the hum is longer than the length of the song from the start to
		# to the end, then we cannot compare
		song_clip = song[start:]
		# print len(song_clip)
		if len(hum) > len(song_clip):
			continue
		# store a list of minimum euclidean distances between each point in
		# the hum and every point in the song; the sum of the min_list will 
		# therefore be the frechet distance	
		min_list = []
		# for tick_h in hum:
		for x in xrange(0,len(hum)):
			# this initial min_val uses the index in the distance	
			# min_val = (euclid((x,hum[x][1]),(x,song_clip[x][1])),song_clip[x][0],x)
			# this initial min_val normalizes the timestamps
			min_val = euclid((hum[x][0] - hum[0][0],hum[x][1]),((song_clip[x][0]
				-song_clip[0][0]),song_clip[x][1]))
			
			# iterate over song list to calculate minimum euclidean distance
			for y in xrange(max((x-bucket_size),0),min(x+bucket_size,len(song_clip))):
				new_dist = euclid((hum[x][0]-hum[0][0],hum[x][1]),(song_clip[y][0]
					-song_clip[0][0],song_clip[y][1]))
				if new_dist < min_val:
					min_val = new_dist
			min_list.append(min_val)
	
		# append sum to pair
		frechet_list.append(sum(min_list))
	
	# handles the case of no matches, i.e. hum is longer than entire song
	if len(frechet_list) == 0:
		frechet_list = [float_max]

	# return the minimum frechet value for a hum matched to each section
	return min(frechet_list)

