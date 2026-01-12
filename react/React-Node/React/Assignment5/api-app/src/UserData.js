import React, { useEffect, useState } from "react";

/**
 * UserData component
 * Fetches user data from an external API when the component mounts
 * and displays the name and email of the first user.
 */
function UserData() {
  /**
   * State to store fetched user data
   */
  const [user, setUser] = useState(null);

  /**
   * useEffect runs once when the component mounts
   * It fetches user data from the API
   */
  useEffect(() => {
    /**
     * Fetch user data from the API
     */
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        /**
         * Store the first user from the response
         */
        setUser(data[0]);
      })
      .catch((error) => {
        console.error("Error fetching user data:", error);
      });
  }, []); // Empty dependency array means it runs only once

  return (
    <div>
      <h2>User Details</h2>

      {/**
       * Display user details only after data is fetched
       */}
      {user ? (
        <div>
          <p><strong>Name:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
    </div>
  );
}

export default UserData;
