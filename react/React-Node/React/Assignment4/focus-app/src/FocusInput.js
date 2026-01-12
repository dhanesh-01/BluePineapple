import React, { useRef } from "react";
/**
 * FocusInput component
 * Demonstrates how to use useRef to focus an input field
 * when a button is clicked.
 */
function FocusInput() {
  /**
   * inputRef stores a reference to the input DOM element
   */
  const inputRef = useRef(null);

  /**
   * Focuses the input field when the button is clicked
   */
  const handleFocus = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Click button to focus me"
        /**
         * Attaches the ref to the input element
         */
        ref={inputRef}
      />

      <button onClick={handleFocus}>
        Focus Input
      </button>
    </div>
  );
}

export default FocusInput;
