// Task for Payam Taherirostami

import React from "react";
import './SubmitBtn.css';


export default function SubmitBtn({feedback , setFeedback}) {
    const [showAnalysis, setShowAnalysis] = React.useState(false)
    const handleSubmit = (evt) => {
        evt.preventDefault();
        // setFeedback('')
        setShowAnalysis(true)
        showAnalysis(true)
    }
    return (
        <div>
             <button onClick={handleSubmit}>Submit</button>
             <div>{ showAnalysis ? feedback : null }</div>
        </div>
    );
}