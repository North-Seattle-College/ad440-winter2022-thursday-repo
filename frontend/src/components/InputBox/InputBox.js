import "./InputBox.css";

export default function InputBox({feedback, setFeedback}) {
  return (
    <div>
      <div>
        <h1>Feedback</h1>
      </div>

      <div className="third">To add description in future</div>
      <h2>Please enter a comment</h2>
      <input type="text" className="feedback-input"   
             value={feedback}
             onChange={e => setFeedback(e.target.value)}/>
    </div>
  );
}
