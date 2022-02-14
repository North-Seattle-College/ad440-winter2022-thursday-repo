import "./App.css";
import InputBox from "../InputBox/InputBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback] = useState('');
  return (
    <div className="App">
      <InputBox feedback={feedback} setFeedback={setFeedback} />
      <div className="userBtns">
        <SubmitBtn feedback={feedback} setFeedback={setFeedback} />
        <ClearBtn setFeedback={setFeedback} />
      </div>
      <FeedbackBox />
    </div>
  );
}

export default App;
