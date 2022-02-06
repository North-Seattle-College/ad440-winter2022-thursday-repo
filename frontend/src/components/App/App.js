import "./App.css";
import InputBox from "../InputBox/InputBox";
import ErrorBox from "../ErrorBox/ErrorBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback] = useState('');
  return (
    <div className="App">
      <InputBox feedback={feedback} setFeedback={setFeedback}/>
      <SubmitBtn feedback={feedback} setFeedback={setFeedback} />
      <ClearBtn />
      <FeedbackBox />
      <ErrorBox />
    </div>
  );
}

export default App;