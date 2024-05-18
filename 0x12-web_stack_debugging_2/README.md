# Web stack debugging #2

## Resources:

0-->

- https://askubuntu.com/questions/486346/this-account-is-currently-not-available-error-when-trying-to-ssh

- https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwix_8uIvZuDAxXCTaQEHUOmC-8QFnoECBcQAw&url=https%3A%2F%2Fbeebom.com%2Fhow-switch-users-linux%2F&usg=AOvVaw3yIB3BUhD4QpRhra-2QB1O&opi=89978449

1-->

- https://www.geeksforgeeks.org/how-to-run-nginx-for-root-non-root/
- Web stack debugging concept page

---

steps in task 1:

1. Run `netstat -lpn` -> found out that apache is running and binding all ports

2. Ran `pgrep -lf apache` -> got apache pid's to kill them

3. killed those process using `kill -9 <pid>` (`kill -l` to know all the signals)

4. edited /etc/nginx/nginx.conf first line to "nginx" (after adding the necessary permissions `w`)

5. ran `sudo nginx -t` to test

6. ran `sudo -u nginx service nginx start` -> it gave the error permission denied

7. chmod a+r /etc/nginx/nginx.conf

8. number 6 again
