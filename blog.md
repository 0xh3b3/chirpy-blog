---
layout: page
title: Blog
permalink: /blog/
---

{% include lang.html %}

{% assign posts = site.posts | where_exp: "post", "post.categories contains 'Blog'" %}
{% for post in posts %}
  {% include post-list.html %}
{% endfor %}
