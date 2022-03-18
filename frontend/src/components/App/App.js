import "./App.css";
import InputBox from "../InputBox/InputBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";
import logo from "../Logo/floop_logo.png";
import ResponseBox from "../ResponseBox/ResponseBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";

function App() {
  const [input, setInput] = useState("");
  const [AIfeedback, setAIfeedback] = useState();
  const [APIResponse, setAPIResponse] = useState();
  const [show, setShow] = useState(false);

  return (
    <div className="App">
      <img className="logo" src={logo} alt="Logo" />
      <div id="wrapper">
        <InputBox input={input} setInput={setInput} />
        <div className="userBtns">
          <div className="clearBtn">
            <ClearBtn setInput={setInput} setShow={setShow} />
          </div>
          <div className="submitBtn">
            <SubmitBtn
              input={input}
              setAIfeedback={setAIfeedback}
              setAPIResponse={setAPIResponse}
              setShow={setShow}
            />
          </div>
        </div>
        <div id="feedbackTitle"></div>
        <ResponseBox AIfeedback={AIfeedback} APIResponse={APIResponse} />
        {show && <FeedbackBox AIfeedback={AIfeedback} show={show} />}
      </div>
    </div>
  );
}

export default App;
