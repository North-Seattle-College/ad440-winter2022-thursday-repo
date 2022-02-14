import React from "react";

export default function SubmitBtn({ feedback, setFeedback }) {
    const handleSubmit = (evt) => {
        evt.preventDefault();
        alert(`You entered: ${feedback}`)
        setFeedback('')
    }
    return (
        <button onClick={handleSubmit}>Submit</button>
    );
}