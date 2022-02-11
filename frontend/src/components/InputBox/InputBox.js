import "./InputBox.css";

export default function InputBox({ feedback, setFeedback }) {
  return (
    <div>
      <div>
        <h1>Feedback</h1>
      </div>

      <div className="description">
        As you write down your comments to give feedback to students, you will
        receive relevant coaching messages according to your feedback to improve
        it.
      </div>
      <h2>Teacher Comment</h2>
      <input
        type="text"
        className="feedback-input"
        placeholder="Your comment goes here..."
        value={feedback}
        onChange={e => setFeedback(e.target.value)}
      />
    </div>
  );
}
