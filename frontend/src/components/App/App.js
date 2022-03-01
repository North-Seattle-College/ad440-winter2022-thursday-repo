import "./App.css";
import InputBox from "../InputBox/InputBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";
import logo from "../Logo/floop_logo.png"

function App() {
  const [feedback, setFeedback] = useState('');
  const [show, setShow] = useState(false);
  return (

    <div className="App">
      <img className="logo" src={logo} alt="Logo" />
      <div id="wrapper">
        <InputBox feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
        <div className="userBtns">
          <div className="clearBtn">
            <ClearBtn setFeedback={setFeedback} setShow={setShow} />
          </div>
          <div className="submitBtn">
            <SubmitBtn feedback={feedback} setFeedback={setFeedback} setShow={setShow} />
          </div>
        </div>
        <div id="feedbackTitle"><h4>Comment Feedback:</h4></div>
        {show && <FeedbackBox feedback={feedback} show={show} />}
      </div>
    </div>
  );
}

export default App;
