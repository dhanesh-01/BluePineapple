import React from "react";
/**
 * Sender component contains an input field.
 * Sends user-typed data to the parent component
 * using the setMessage function passed via props.
 */
function Sender({ setMessage }) {
  return (
    <div>
      <input
        type="text"
        placeholder="Type a message"
        onChange={(e) => setMessage(e.target.value)}
      />
    </div>
  );
}

export default Sender;
