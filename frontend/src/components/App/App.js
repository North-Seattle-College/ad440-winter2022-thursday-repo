import "./App.css";

import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback] = useState('');
  return (
    <div className="App">
 
      <SubmitBtn feedback={feedback} setFeedback={setFeedback} />

    </div>
  );
}

export default App;