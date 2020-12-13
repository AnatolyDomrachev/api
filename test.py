import urllib2
req = urllib2.Request('https://api.spotify.com/v1/tracks/?ids=11dFghVXANMlKmJXsNCbNl', {'Authorization' : 'Bearer BQA5pi8lsJOPpvSPBYnX99N_8z2KL-5uniilECprwCI0D22yiegWSI5ExZyZ-GPqf48JGnzFHN__ap3qs0f_ToIXZ6zkg3EM09LZHBHLNa81_kHMytDMLIvX9CZOtGfPe68PuTRGH_JFwpNwtQXwo5AlvQG2R5DnkF4mHI-3dE2E37ETYHCIQCY61vnuBGvILsITcwi6MW8DdCDQ3f8vElJv69tgsb8HupGjnlErICycSUt8qB1XsFh08tm1VjO3saqpQCoLLCJwzZ8IEIvsm3KQ2NqGdmLRLHo'})

#req.add_header('Authorization','Bearer BQA5pi8lsJOPpvSPBYnX99N_8z2KL-5uniilECprwCI0D22yiegWSI5ExZyZ-GPqf48JGnzFHN__ap3qs0f_ToIXZ6zkg3EM09LZHBHLNa81_kHMytDMLIvX9CZOtGfPe68PuTRGH_JFwpNwtQXwo5AlvQG2R5DnkF4mHI-3dE2E37ETYHCIQCY61vnuBGvILsITcwi6MW8DdCDQ3f8vElJv69tgsb8HupGjnlErICycSUt8qB1XsFh08tm1VjO3saqpQCoLLCJwzZ8IEIvsm3KQ2NqGdmLRLHo')

#req = urllib2.Request("http://google.com", None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})

#req.add_header('Referer', 'http://www.python.org/')
resp = urllib2.urlopen(req)
content = resp.read()
print(content)
