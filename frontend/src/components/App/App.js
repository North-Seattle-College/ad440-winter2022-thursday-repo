import "./App.css";
import InputBox from "../InputBox/InputBox";
import ErrorBox from "../ErrorBox/ErrorBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";
import React, { useState } from "react";

function App() {
  const [feedback, setFeedback, showAnalysis, setShowAnalysis] = useState('');
  return (
    <div className="App">
      <InputBox feedback={feedback} setFeedback={setFeedback}/>

      {/* Task for Payam Taherirostami: */}
      <SubmitBtn feedback={feedback} setFeedback={setFeedback} showAnalysis={showAnalysis} setShowAnalysiss={setShowAnalysis}/> 
       
      <ClearBtn setFeedback={setFeedback}/>
      <FeedbackBox feedback={feedback} showAnalysis={showAnalysis}/>
      <ErrorBox />
    </div>
  );
}

export default App;
