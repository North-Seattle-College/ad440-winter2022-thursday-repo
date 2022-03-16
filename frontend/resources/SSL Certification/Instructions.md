### About
This contains instructions on how to use Certbot to set up an SSL certificate for a custom DNS and/or API Gateway, when you cannot `ssh` into the server directly.

---
### Steps
1. Install Certbot on your computer (Instructions [here](https://certbot.eff.org/)).
2. Once Cerbot is installed, you should be able to run `certbot certonly --manual --preferred-challenges dns -d yourWebsite.com` in the terminal.
3. Certbot should respond with a "URL" and a "String".
4. Do NOT press `ENTER` yet.
  a. _(If you press enter before step 8 you will need to restart from step 2)_
5. Head over to your chosen DNS manager ([godaddy.com](http://godaddy.com/), etc..).
6. Create a new DNS.
  a. The `Type` should be "TXT".
  b. The `Name` will be the URL from Certbot.
  c. The `Value` will be the String from Certbot.
  d. The `TTL` can be default.
7. Wait a few minutes for the DNS manager to deploy the changes.
8. Switch back to the terminal.
9. Press `ENTER`
10. You should see a confirmation showing you the file location of the `Certificate` and `Key` .pem files.
11. Open this file directory and save the location/files
12. You can now upload the contents of these files to your AWS API Gateway by _"Importing Certificate"_

**NOTE:** In order to complete steps 5-7, you will need either need access the DNS manager or coordinate with the person who has access.