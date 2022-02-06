import React, { useState } from "react";
import './SubmitBtn.css'
export default function SubmitBtn() {

    const [feedback, setFeedback] = useState("");
    
    const handleSubmit = (evt) => {
        evt.preventDefault();
        alert(`You entered:  ${feedback}`)
        setFeedback('')
    }
    return (

        <div>
             <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}