#!/usr/bin/python3.7
import sys 

if (len(sys.argv) == 1):
	print ("\n\n-h    |    --help    for info\n\n")
	exit()

if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
	print ("\n________________________SIMPLE CLASS GENERATOR__________________________")	
	print ("\n\n-h    |    --help                for info")
	print ("\n\n-f    |   --function             Write names of functions in your class")
	print ("\n-pf   |   ---private-function    Write names of private functions")
	print ("\n________________________________________________________________________\n")
	exit()



def index(j):
	while ( (j < len(sys.argv)) and (sys.argv[j][0] != '-') ):
		print (sys.argv[j])
		j+=1

	return j



h = open('%s.h' %sys.argv[1], 'a+')
cpp = open('%s.cpp' %sys.argv[1], 'a+')

h.write('#ifndef _%s_H_\n' %sys.argv[1].upper())
h.write('#define _%s_H_\n\n' %sys.argv[1].upper())
h.write('class %s{\npublic:\n' %(sys.argv[1]))
h.write("\t%s();\n\t~%s();\n\n" % (sys.argv[1], sys.argv[1]))

cpp.write('#include "%s.h"\n#include <iostream>\n\n\nusing namespace std;\n\n' %sys.argv[1])
cpp.write("%s::%s()\n{\n\n}\n\n%s::~%s()\n{\n\n}\n\n" % (sys.argv[1], sys.argv[1],sys.argv[1], sys.argv[1]))

if (len(sys.argv) > 2):
	end = index(3)
	i = 2
	while(1):
		option = sys.argv[i]
		i+=1
		if (option == "-f" or option == "--public-function"):	
			while (i<end):
				h.write("\tTYP_TYP %s();\n" %(sys.argv[i]))
				cpp.write("TYP_TYP %s::%s()\n{\n\n}\n\n" %(sys.argv[1],sys.argv[i]))
				i+=1
		elif (option == "-pf" or option == "--private-function"):			
			h.write("\n\nprivate:\n")
			cpp.write("\n//========================PRIVATE==============================\n")
			while (i<end):
				h.write("\tTYP_TYP %s();\n" %(sys.argv[i]))
				cpp.write("TYP_TYP %s::%s()\n{\n\n}\n\n" %(sys.argv[1],sys.argv[i]))
				i+=1
		
		if (end < len(sys.argv)):
			end = index(end+1)
		else:
			break

h.write("\n};\n\n\n#endif")



h.close()
cpp.close()