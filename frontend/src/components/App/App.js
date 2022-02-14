import "./App.css";
import InputBox from "../InputBox/InputBox";
import ErrorBox from "../ErrorBox/ErrorBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback] = useState('');
  {/* Task for David Nguyen */} 
  const [show, setShow] = useState(false);
  return (
    <div className="App">
      <InputBox feedback={feedback} setFeedback={setFeedback} setShow={setShow}/>

      {/* Task for Payam Taherirostami: */}
      <SubmitBtn feedback={feedback} setFeedback={setFeedback} setShow={setShow}/> 
       
      <ClearBtn setFeedback={setFeedback} setShow={setShow}/>

      {/* Task for David Nguyen */} 
      {show && <FeedbackBox feedback={feedback} show={show} />}
      {/* <ErrorBox /> */}
    </div>
  );
}

export default App;
