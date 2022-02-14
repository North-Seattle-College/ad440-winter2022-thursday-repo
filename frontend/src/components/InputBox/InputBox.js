import "./InputBox.css";

export default function InputBox({ feedback, setFeedback }) {
  return (
    <div>
      <div className="third">
        As you write down messages to give feedback to students, you will
        receive relevant coaching messages according to your feedback to improve
        it.
      </div>
      <h2>Please enter a comment</h2>
      <input
        type="text"
        className="feedback-input"
        value={feedback}
        onChange={e => setFeedback(e.target.value)}
      />
    </div>
  );
}
