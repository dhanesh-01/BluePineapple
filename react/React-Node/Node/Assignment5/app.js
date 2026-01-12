const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

//Built-in Middleware
app.use(express.json()); // to read JSON body

//Custom Logger Middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

//Routes

// GET /
app.get('/', (req, res) => {
  res.send('Welcome to Express!');
});

// POST /data
app.post('/data', (req, res) => {
  console.log(req.body);
  res.send('Data received.');
});

// GET /users (mock data)
app.get('/users', (req, res) => {
  const users = [
    { id: 1, name: 'Dhanesh' },
    { id: 2, name: 'pranav' },
    { id: 3, name: 'vaibhav' }
  ];
  res.json(users);
});

//external API
app.get('/external-posts', async (req, res, next) => {
  try {
    const response = await axios.get(
      'https://jsonplaceholder.typicode.com/posts'
    );
    res.json(response.data);
  } catch (error) {
    next(error);
  }
});

//404 Middleware
app.use((req, res) => {
  res.status(404).send('Route not found');
});

//Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500).send('Something went wrong!');
});

//Start Server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
