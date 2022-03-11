import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# XSS BEST PRACTICES
# Validate all data that flows into your application from the server or a third-party API. This cushions your application against an XSS attack, and at times, you may be able to prevent it, as well.
# Don't mutate DOM directly. If you need to render different content, use innerText instead of innerHTML. Be extremely cautious when using escape hatches like findDOMNode or createRef in React.
# Always try to render data through JSX and let React handle the security concerns for you.
# Use dangerouslySetInnerHTML in only specific use cases. When using it, make sure you're sanitizing all your data before rendering it on the DOM.
# Avoid writing your own sanitization techniques. It's a separate subject on its own that requires some expertise.
# Use good libraries for sanitizing your data. There are a number of them, but you must compare the pros and cons of each specific to your use case before going forward with one.


# url = 'http://localhost:3000/feedback'
# payload = {"feedback": "<scrip lanugage = http://"}
# r = requests.post(url, json=payload)
# print(r.json())


# get forms
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# get form details
def get_form_details(form):
    details = {}
    # get the form action
    action = form.attrs.get("action").lower()
    # get the form method
    method = form.attrs.get("method", "get").lower()
    # get all the input details
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # store all details
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# fill and submit form
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def check_xss(url):
    # get all forms from the URL
    forms = get_all_forms(url)
    print(f"Found {len(forms)} forms on {url}.")
    js_script = "<script>alert('This could be insecure')</script>"
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable


if __name__ == "__main__":
    url = "http://localhost:3000/"
    print(check_xss(url))