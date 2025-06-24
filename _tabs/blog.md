---
title: Blog
icon: fas fa-blog
order: 2
---

<style>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
  margin-top: 30px;
}
.blog-post {
  border: 1px solid #444;
  padding: 20px;
  border-radius: 10px;
  background: #1e1e1e;
  transition: transform 0.2s ease;
}
.blog-post:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.blog-post h3 {
  margin-top: 0;
  font-size: 1.2rem;
}
.blog-post .meta {
  font-size: 0.9rem;
  color: #aaa;
  margin-bottom: 10px;
}
.blog-post p {
  font-size: 1rem;
  color: #ccc;
}
</style>

<h1>Cybersecurity Blog</h1>
<p>Insights, writeups, and thoughts on bug bounty hunting, cybersecurity practices, and more.</p>

<div class="blog-grid">
  {% assign blogposts = site.posts | where_exp: "post", "post.categories contains 'Blog'" %}
  {% for post in blogposts %}
    <div class="blog-post">
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <div class="meta">{{ post.date | date: "%B %d, %Y" }} &bull; Categories: {{ post.categories | join: ', ' }}</div>
      <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
    </div>
  {% endfor %}
</div>
