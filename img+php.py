#!/usr/bin/env python
# L0V3R IN MYANMAR
# file : file binder

import sys
version = 1
def help():
	print '''
	File combiner( Version : %s )

	Usage 	   : python %s [imgfile] [phpfile] [savefile] [savefile] 
	
	Example    : python %s image.png phpfile.php shell.php

	savefile = default.php ( default file name )
	''' % (version,sys.argv[0],sys.argv[0])
def bind(savefile='default.php'):
	try:
		img_read = open(sys.argv[1]).read()
		if len(img_read) == 0:
			print 'image file is empty!'
			sys.exit(1)
		php_read = open(sys.argv[2]).read()
		if len(php_read) == 0:
			print 'php file is empty!'
			sys.exit(1)
	except IOError,e :
		# print 'Error : Check %s '% sys.argv[1]
		print "Error : File Not Found '%s'"% e.filename
		
		sys.exit(1)

	final_data = img_read+php_read
	open(savefile, 'w').write(final_data)
	print "Bind file save as : ", savefile

if __name__ == '__main__':
	if len(sys.argv) == 1:
		help()
	elif len(sys.argv) == 2:
		print 'Missing phpfile!'
		help()
	elif len(sys.argv) == 3:
		bind()
	elif len(sys.argv) == 4:
		bind(sys.argv[3])
