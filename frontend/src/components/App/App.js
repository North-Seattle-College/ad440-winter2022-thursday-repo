import "./App.css";
import InputBox from "../InputBox/InputBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";
import logo from "../Logo/floop_logo.png"

function App() {
  const [input, setInput] = useState('');
  const [AIfeedback, setAIfeedback] = useState();
  const [show, setShow] = useState(false);
  return (

    <div className="App">
      <img className="logo" src={logo} alt="Logo" />
      <div id="wrapper">
        <InputBox input={input} setInput={setInput} setShow={setShow} />
        <div className="userBtns">
          <div className="clearBtn">
            <ClearBtn setInput={setInput} setShow={setShow} />
          </div>
          <div className="submitBtn">
            <SubmitBtn input={input} setInput={setInput} setShow={setShow} setAIfeedback={setAIfeedback} />
          </div>
        </div>
        <div id="feedbackTitle"></div>
        {show && <FeedbackBox AIfeedback={AIfeedback} show={show} />}
      </div>
    </div>
  );
}

export default App;
