---
layout: page
title: Blog
permalink: /blog/
---

<style>
.blog-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}
.blog-filters button {
  padding: 6px 12px;
  border-radius: 8px;
  background: #333;
  color: white;
  border: none;
  cursor: pointer;
}
.blog-filters button.active {
  background: #0d6efd;
}
</style>

<div class="blog-filters">
  <button onclick="filterBlog('All')" class="active">All</button>
  <button onclick="filterBlog('Updates')">Updates</button>
  <button onclick="filterBlog('Tutorial')">Tutorial</button>
  <button onclick="filterBlog('Security')">Security</button>
</div>

<div id="blog-posts">
  {% assign posts = site.posts | where_exp: "post", "post.categories contains 'Blog'" %}
  {% for post in posts %}
    <div class="blog-entry" data-category="{{ post.categories | join: ' ' }}">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      <p><strong>Categories:</strong> {{ post.categories | join: ', ' }}</p>
      <hr>
    </div>
  {% endfor %}
</div>

<script>
function filterBlog(cat) {
  document.querySelectorAll('.blog-filters button').forEach(btn => {
    btn.classList.remove('active');
    if (btn.innerText === cat || (cat === 'All' && btn.innerText === 'All')) {
      btn.classList.add('active');
    }
  });
  document.querySelectorAll('.blog-entry').forEach(el => {
    if (cat === 'All' || el.dataset.category.includes(cat)) {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
  });
}
</script>

  border-radius: 8px;
  background: #333;
  color: white;
  border: none;
  cursor: pointer;
}
.filter-buttons button.active {
  background: #0d6efd;
}
</style>

<div class="filter-buttons">
  <button onclick="filterCTF('All')" class="active">All</button>
  <button onclick="filterCTF('HTB')">HTB</button>
  <button onclick="filterCTF('PicoCTF')">PicoCTF</button>
  <button onclick="filterCTF('NahamCon2025')">NahamCon2025</button>
</div>

<div id="ctf-posts">
  {% assign posts = site.posts | where_exp: "post", "post.categories contains 'CTF'" %}
  {% for post in posts %}
    <div class="ctf-entry" data-category="{{ post.categories | join: ' ' }}">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      <p><strong>Categories:</strong> {{ post.categories | join: ', ' }}</p>
      <hr>
    </div>
  {% endfor %}
</div>

<script>
function filterCTF(cat) {
  document.querySelectorAll('.filter-buttons button').forEach(btn => {
    btn.classList.remove('active');
    if (btn.innerText === cat || (cat === 'All' && btn.innerText === 'All')) {
      btn.classList.add('active');
    }
  });
  document.querySelectorAll('.ctf-entry').forEach(el => {
    if (cat === 'All' || el.dataset.category.includes(cat)) {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
  });
}
</script>

