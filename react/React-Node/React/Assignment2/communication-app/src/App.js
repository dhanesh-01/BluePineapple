import React, { useState } from "react";
import Sender from "./Sender";
import Receiver from "./Receiver";
/**
  App component
  Acts as the parent component.
  Stores the message in state and passes:
  a function to Sender to update the message
  and the message itself to Receiver for display
 */

function App() {
  const [message, setMessage] = useState("");

  return (
    <div>
      <Sender setMessage={setMessage} />
      <Receiver message={message} />
    </div>
  );
}

export default App;
