import React from "react";
import './SubmitBtn.css';

export default function SubmitBtn({feedback , setFeedback}) {
    const handleSubmit = (evt) => {
        evt.preventDefault();
        alert(`You entered: ${feedback}`)
        setFeedback('')
    }
    return (
        <div>
             <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}