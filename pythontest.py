def printurls( baseurl, lasturl ):
	n = 34
	s = ""

	for i in range(n):
	    s += "\""+baseurl+str(i+1)+"\""
	    if i < n-1 or not lasturl:
	        s += ",\n"
	return s

baseurl = "http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=235&searchdisciplines=&searchdegree=&searchtuition=0&resident=0&page="

print(    	printurls("http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=",True))



