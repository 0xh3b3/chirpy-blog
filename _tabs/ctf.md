---
title: CTFs
icon: fas fa-flag
order: 1
layout: page
---

<style>
.filter-buttons, .tag-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
}
.filter-buttons button, .tag-buttons button {
  padding: 6px 12px;
  border-radius: 8px;
  background: #333;
  color: white;
  border: none;
  cursor: pointer;
}
.filter-buttons button.active, .tag-buttons button.active {
  background: #0d6efd;
}
</style>

<div class="filter-buttons">
  <button onclick="filterCategory('All')" class="active">All</button>
  <button onclick="filterCategory('HTB')">HTB</button>
  <button onclick="filterCategory('PicoCTF')">PicoCTF</button>
  <button onclick="filterCategory('NahamCon2025')">NahamCon2025</button>
</div>

<div class="tag-buttons">
  <button onclick="filterTag('All')" class="active">All Tags</button>
  <button onclick="filterTag('Warmups')">Warmups</button>
  <button onclick="filterTag('Web')">Web</button>
  <button onclick="filterTag('Rev')">Rev</button>
  <button onclick="filterTag('Crypto')">Crypto</button>
</div>

<div id="ctf-posts">
  {% assign posts = site.posts | where_exp: "post", "post.categories contains 'CTF'" %}
  {% for post in posts %}
    <div class="ctf-entry" data-category="{{ post.categories | join: ' ' }}" data-tags="{{ post.tags | join: ' ' }}">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      <p><strong>Categories:</strong> {{ post.categories | join: ', ' }} | <strong>Tags:</strong> {{ post.tags | join: ', ' }}</p>
      <hr>
    </div>
  {% endfor %}
</div>

<script>
function filterCategory(cat) {
  document.querySelectorAll('.filter-buttons button').forEach(btn => btn.classList.remove('active'));
  document.querySelector(`.filter-buttons button[onclick*="${cat}"]`).classList.add('active');

  const tag = document.querySelector('.tag-buttons button.active').innerText;
  filterPosts(cat, tag);
}

function filterTag(tag) {
  document.querySelectorAll('.tag-buttons button').forEach(btn => btn.classList.remove('active'));
  document.querySelector(`.tag-buttons button[onclick*="${tag}"]`).classList.add('active');

  const cat = document.querySelector('.filter-buttons button.active').innerText;
  filterPosts(cat, tag);
}

function filterPosts(cat, tag) {
  document.querySelectorAll('.ctf-entry').forEach(entry => {
    const inCategory = cat === 'All' || entry.dataset.category.includes(cat);
    const inTag = tag === 'All Tags' || entry.dataset.tags.includes(tag);
    entry.style.display = inCategory && inTag ? 'block' : 'none';
  });
}
</script>
