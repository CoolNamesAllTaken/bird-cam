import os
import subprocess
import twitter

MOTION_FILES_PATH = os.path.join(os.sep, "home", "pi", "motion_files")
MOTION_FILES_TIMESTAMP_OFFSET = 2
GIFS_PATH = os.path.join(os.sep, "home", "pi", "gifs")

GIF_DELAY = 10

twitter_api = twitter.Api(
	consumer_key="dZ71fxd5V6Sxoz7lYhSQUhOFc",
	consumer_secret="ONzpIQ04ztMISw7E8VfnMIsCXXAIMr0MY32u2ucEKkdof3UMIu",
	access_token_key="1071898063088668673-RcAAiLf6Q6ODoGhRx2pFxBrNyck4yw",
	access_token_secret="IHnDqtmhk50CmbKCfX4PKrmLWhShiwcNzAcyqQuFIw859")

def main():
	make_gifs()

"""
Assembles gifs from images in MOTION_FILES_PATH.  Walks back from the last "-" symbol in the filenames generated
by motion by MOTION_FILES_TIMESTAMP_OFFSET characters to group images into batches for giffing.  Puts the resulting
gif into the GIFS_PATH directory and deletes the constituent images.
"""
def make_gifs(do_twoot=True):
	motion_filenames = os.listdir(MOTION_FILES_PATH)
	# print(motion_filenames)
	while (len(motion_filenames) > 0):
		# repeat until directory is empty
		motion_filename = motion_filenames[0]
		motion_filename_prefix = motion_filename[0:motion_filename.rfind("-")-MOTION_FILES_TIMESTAMP_OFFSET]
		print("Making gif from images with prefix {}".format(motion_filename_prefix))

		gif_filename = os.path.join(GIFS_PATH, "{}.gif".format(motion_filename_prefix))

		# send specific files to image magick
		p = subprocess.Popen(
			["convert",
			"-delay", str(GIF_DELAY),
			"-loop", str(0),
			"{}*.jpg".format(os.path.join(MOTION_FILES_PATH, motion_filename_prefix)),
			gif_filename])
		p.wait()

		if do_twoot:
			# attempt to twoot the gif
			twoot(gif_filename)

		# delete images that went to image magick
		print("Removing images with prefix {}".format(motion_filename_prefix))
		for f in motion_filenames:
			if f.find(motion_filename_prefix) != -1:
				os.remove(os.path.join(MOTION_FILES_PATH, f))

		motion_filenames = os.listdir(MOTION_FILES_PATH)

"""
Tweets all the gifs in the GIFS_PATH directory.
"""
def tweet_all_gifs():
	for f in os.listdir(GIFS_PATH):
		twoot(os.path.join(GIFS_PATH, f))

"""
Tweets the gif on a given path.
Inputs:
	path = path to file for tweeting
"""
def twoot(path):
	print("twoot {}".format(path))
	try:
		twitter_api.PostUpdate("{}".format(path), path)
	except:
		print("no twoot :(")

"""
Deletes the files in the GIFS_PATH folder
"""
def delete_gifs():
	for f in os.listdir(GIFS_PATH):
		os.remove(f)

if __name__ == "__main__":
	main()