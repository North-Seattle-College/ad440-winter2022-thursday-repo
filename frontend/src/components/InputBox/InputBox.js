export default function InputBox({ feedback, setFeedback }) {
  return (
    <div className="input-main">
      <div className="page-header">
        As you write down messages to give feedback to students, you will
        receive relevant coaching messages according to your feedback to improve
        it.
      </div>
      <h2 className="input-header">Please enter a comment</h2 >
      <input
        type="text"
        className="user-input"
        value={feedback}
        onChange={e => setFeedback(e.target.value)}
      />
    </div>
  );
}
