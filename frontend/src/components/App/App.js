import "./App.css";
import InputBox from "../InputBox/InputBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback] = useState('');
  // Task for David Nguyen
  const [show, setShow] = useState(false);
  return (
    <div className="App">
      <InputBox feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
      <div className="userBtns">
        {/* Task for Payam Taherirostami: */}
        <ClearBtn setFeedback={setFeedback} setShow={setShow} />
        <SubmitBtn feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
      </div>
      {/* Task for David Nguyen */}
      {show && <FeedbackBox feedback={feedback} show={show} />}
    </div>
  );
}

export default App;
