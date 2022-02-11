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

      {/* Task for Payam Taherirostami: */}
      <SubmitBtn feedback={feedback} setFeedback={setFeedback} /> 
       
      <ClearBtn setFeedback={setFeedback}/>
      <FeedbackBox />
      <ErrorBox />
    </div>
  );
}

export default App;
