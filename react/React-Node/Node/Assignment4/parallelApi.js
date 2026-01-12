const axios = require('axios');
async function fetchMultipleData() {
  try {
    const [postsResponse, commentsResponse] = await Promise.all([
      axios.get('https://jsonplaceholder.typicode.com/posts'),
      axios.get('https://jsonplaceholder.typicode.com/comments')
    ]);
    console.log('Posts count:', postsResponse.data.length);
    console.log('Comments count:', commentsResponse.data.length);
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}
fetchMultipleData();
