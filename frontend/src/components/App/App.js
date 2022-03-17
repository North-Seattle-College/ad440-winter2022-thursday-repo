import "./App.css";
import InputBox from "../InputBox/InputBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";
import logo from "../Logo/floop_logo.png";
import ResponseBox from "../ResponseBox/ResponseBox";

function App() {
  const [input, setInput] = useState('');
  const [AIfeedback, setAIfeedback] = useState();
  const [APIResponse, setAPIResponse] = useState();

  return (
    <div className="App">
      <img className="logo" src={logo} alt="Logo" />
      <div id="wrapper">
        <InputBox input={input} setInput={setInput} />
        <div className="userBtns">
          <div className="clearBtn">
            <ClearBtn setInput={setInput} />
          </div>
          <div className="submitBtn">
            <SubmitBtn input={input} setAIfeedback={setAIfeedback} setAPIResponse={setAPIResponse} />
          </div>
        </div>
        <div id="feedbackTitle"></div>
        <ResponseBox AIfeedback={AIfeedback} APIResponse={APIResponse} />
      </div>
    </div>
  );
}

export default App;
