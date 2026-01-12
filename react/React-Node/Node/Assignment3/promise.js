function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true; // change to false to test rejection

      if (success) {
        resolve('Data fetched successfully');
      } else {
        reject('Error while fetching data');
      }
    }, 2000);
  });
}

//handling the promise
fetchData()
  .then((message) => {
    console.log(message);
  })
  .catch((error) => {
    console.error(error);
  });
