---
layout: page
title: CTFs
permalink: /ctf/
---

{% include lang.html %}

{% assign posts = site.posts | where_exp: "post", "post.categories contains 'CTF'" %}
{% for post in posts %}
  {% include post-list.html %}
{% endfor %}
