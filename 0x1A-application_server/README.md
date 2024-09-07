# Application server

task 0 steps:

1. Add the SSH public key to the authorized ssh public keys on the server

2. Git clone AirBnB_clone_v2 on web-01 server.

3. Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/

---

task 1 steps:

1. `pip3 install gunicorn flask` (if not done in task 0) or
   if not working --> `sudo apt install gunicorn`

2. `sudo ufw allow 5000`

3. `gunicorn --bind 0.0.0.0:5000 0-hello_route:app`

if not working -->

3. `sudo apt purge python3-click ; sudo pip install click==8.1.6`

4. `gunicorn --bind 0.0.0.0:5000 0-hello_route:app`
