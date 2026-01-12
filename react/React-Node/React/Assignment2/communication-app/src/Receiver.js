import React from "react";
/**
 * Receiver component
 * Receives the message from the parent component
 * and displays it on the screen */
function Receiver({ message }) {
  return (
    <div>
      <h3>Received Message:</h3>
      <p>{message}</p>
    </div>
  );
}

export default Receiver;
