![alt text](cartoon-project-post-mortem.jpg)
Issue :
Impact:
web server decided to take an impromptu nap, leaving the website in a state of existential crisis.
Users were greeted with HTTP 500 errors, akin to stumbling upon a closed sign at a 24/7 diner.

Approximately 90% of users were stranded in the digital void during the outage, contemplating the meaning of life.

what i did to fix it
once i noticed the problem, i reverted the server back to its previous state to get it running again. then, i rewrote the script. instead of using su to switch users, i directly edited the nginx configuration to make sure it always runs as the nginx user. this approach was simpler and more effective.

i also made sure to test these changes in a safe environment before applying them to the live server. finally, i did a security check to confirm that everything was secure.
