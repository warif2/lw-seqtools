#!/usr/bin/python
"""
Purpose: Finds intersecting or non-intersecting set between two files by rows.
Usage: python intersection.py [Options] [FILE1] [FILE2] [Comma sep. #'s for columns to check]
         To use column option, input file must be in .csv format.
Options: 
         -int = intersection
         -nint = non-intersection

	 -v = view column headers

         If no column #'s given then whole row will be compared.

Example: python intersection.py -i file1.txt file2.txt 0,1,2,3
Note: First column is denoted as 0 and so on...
"""

import sys
import license


if __name__ == '__main__':
	# Check license
	license.check_status()

	if sys.argv[1] == "--help":
		print(__doc__)
		sys.exit()

	elif sys.argv[1] == '-l':
		print(license.message())

	elif sys.argv[1] == "-int" and len(sys.argv) == 6:
		license.intersect(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

	elif sys.argv[1] == "-int" and len(sys.argv) == 5:
		license.line_intersect(sys.argv[2], sys.argv[3], sys.argv[4])

	elif sys.argv[1] == "-nint" and len(sys.argv) == 6:
		license.non_intersect(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

	elif sys.argv[1] == "-nint" and len(sys.argv) == 5:
		license.line_non_intersect(sys.argv[2], sys.argv[3], sys.argv[4])

	elif sys.argv[1] == "-v":
		with open(sys.argv[2], 'r') as f:
			if sys.argv[3] == "comma":
				dlm = ','
			elif sys.argv[3] == "tab":
				dlm = '\t'
			else:
				print("Specify delimiter!")

			header = f.readline().strip("\n").split(dlm)
			i = 0
			for element in header:
				print("%s	%s" % (i, element))
				i += 1
		print(" ")
	else:
		print("Argument Error! Please see 'python intersection.py --help'.")
