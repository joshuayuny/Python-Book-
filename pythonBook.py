def book():
    print "You've just entered the Python Booklet!"
    print "Do you wish to continue?(y/n) "
    answer = raw_input().lower()
    if answer == "Y" or answer == "y":
      print "print = Display anything (Basically cout in c++)\n"
      print "Do you wish to continue?(y/n) "
      answer1 = raw_input().upper()
      if answer1 == "Y" or answer1 == "y":
          print  "#" + " = To comment code (Basically // in C++)"
      	  print "\nDo you wish to continue?(y/n) "
	  a2 = raw_input()
	  if a2 == "y" or a2 == "Y":
		print "\"\"\"" + " = Long quote for string or to comment\n"
		print "Do you wish to continue?(y/n) "
		a3 = raw_input()
		if a3 == "y" or a3 == "Y":
			print ".upper()" + " : UPPERCASE\n"
			print "\nContinue(y/n)"
			a4 = raw_input()
			if a4 == "y" or a4 == "Y":
				print ".lower()" + " : lowercase\n"
				print "Continue(Y/N)"
				a5 = raw_input()
				if a5 == "Y" or a5 == "y":
					print "variable.replace(word you want to replace, world that you want to replace with)" + " : Replacing a word"
      else:
          print "Invalid input\n"
    elif answer == "No" or answer == "no":
      print "Have a nice day\n"
    else:
      print "Invalid input\n"
      book()

book()
