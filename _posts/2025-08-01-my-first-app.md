---
title: "My First App"
date: 2025-08-01
categories: [CTF, mmuCTF, Web]
tags: [web]
---

# Challenge
>***Points:** 50*

> Our intern dev swears this app’s secure...
>
>**Attachment:** [Create Your Account](http://simulations.cyberchiefgames.tech:8081/profile.php)
>
>***Author:** mburk4*
>
---

## Solution

I clicked the challenge link and I was redirected to a login/Create account page.

While penetration testing a login page, I usually start with common vulnurabilities that can be found in a login page i.e injections like `xss`, `sqli`, `xxe` and `ldap`

So I tries sqli but it seemed not to be vulnurable. so I created an account with xss payloads but they too were filtered

From the screenshot below you can see tht there is a protection against xss and the dangerous characters are being filtered, there is also no sqli as the sqli characters have no effect.

![screenshot](/assets/img/mmuCTF_web1.png)

Ofcourse someone could easily point up blind sqli but I assumed that it too wasn;t there. unless I exhaust all other options then I could come to test for such.

As you can see the id parameter and value is reflected on the url which is a good indication to test for `idor`

Lets start from id 1 since the admin page could be the most interesting and it is most likely to be id 1, anyone familiar with website development and databases will know this.

![screenshot](/assets/img/mmuCTF_web2.png)

> `mmuctf{1d0r_4dm1n_4cc3ss_1s_c0mpr0m1s3d}`

---
## Learning Resources


TryHackMe: [idor](https://tryhackme.com/room/idor)
