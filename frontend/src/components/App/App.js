import "./App.css";
import InputBox from "../InputBox/InputBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";
import logo from "../Logo/floop_logo.png"

function App() {
  const [feedback, setFeedback] = useState('');
  // Task for David Nguyen
  const [show, setShow] = useState(false);
  return (
    
    <div className="App">
      <img className="logo" src={logo} alt="Logo" />
      <div id="wrapper">
      <InputBox feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
      {/* Task Task for Payam Taherirostami */}
      <div className="userBtns">
          <div className="clearBtn">
            <ClearBtn setFeedback={setFeedback} setShow={setShow} />
          </div>
          <div className="submitBtn">
            <SubmitBtn feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
          </div>
      </div>
      {/* Task for David Nguyen */}
      <div id="feedbackTitle"><h3>Comment Feedback:</h3></div>
      {show && <FeedbackBox feedback={feedback} show={show} />}
    </div>
    </div>
  );
}

export default App;
