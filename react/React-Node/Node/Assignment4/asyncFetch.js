async function fetchData() {
  try {
    // simulate API delay of 2 seconds
    await new Promise((resolve) => setTimeout(resolve, 2000));

    const success = true; // change to false to test error

    if (!success) {
      throw new Error('Something went wrong');
    }

    return 'Data fetched successfully';
  } catch (error) {
    throw error;
  }
}

// Using the async function
(async () => {
  try {
    const result = await fetchData();
    console.log(result);
  } catch (err) {
    console.error(err.message);
  }
})();
