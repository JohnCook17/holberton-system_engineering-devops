Diagrams of various networks:

Task 0: A simple network with a single server,
the steps are as follows:
1. Search for domain name
2. DNS look up
3. ANS resolution
4. return ANS info
5. DNS resolution
6. IP address lookup
7. Get HTML and other webpage info
8. Request HTML and webpage from server
9. Request HTML and webpage from code base
10. Return HTML and webpage info from code base
11. Return HTML and webpage info from server
12. Return HTML and webpage info from website
13. Return HTML and webpage info from internet

Task 1: A more complicated network with a load balancer and two servers,
the steps are as follows:
1. Search for domain name
2. DNS look up
3. ANS resolution
4. return ANS info
5. DNS resolution
6. IP address lookup
7. Request HTML and website info
8. load balancing
9. Request HTML and website info from server
10. Request HTML and website info from code base
11. Return HTML and website from code base
12. Return HTML and website info from server
13. Return HTML and website info from load balancer
14. Return HTML and website info from website
15. Return HTML and website info from internet

Task 2: The same as 1 but with monitoring and security,
the steps are as follows:
1. Search for domain name
2. DNS look up
3. ANS resolution
4. return ANS info
5. DNS resolution
6. IP address lookup
7. Request HTML and website info
8. Pass through the firewall request ssl
9. Pass through the load balancer
10. Pass through the secondary firewall
11. Request HTML and webpage info from the server
12. Request HTML and webpage info from the code base
13. Return HTML and webpage info from the code base
14. Return HTML and webpage info through firewall
15. Return HTML and webpage through load balancer
16. Return HTML and webpage through primary firewall
17. Return SSL and HTML and webpage through firewall
18. Return SSL and HTML and webpage from website
19. Return SSL and HTML and webpage from internet

Task 2 also has monitoring set up on the 3 servers, 
the code bases and the load balancer to 
monitor things like queries per second, 
and if there are any outages, or problems.
