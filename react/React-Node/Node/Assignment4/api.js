const axios = require('axios');
async function getPosts() {
  try {
    const response = await axios.get(
      'https://jsonplaceholder.typicode.com/posts'
    );
    const posts = response.data;
    // Log first 5 posts
    posts.slice(0, 5).forEach((post, index) => {
      console.log(`Post ${index + 1}`);
      console.log('Title:', post.title);
      console.log('Body:', post.body);
      console.log('---------------------');
    });
  } catch (error) {
    console.error('Error fetching posts:', error.message);
  }
}
getPosts();
