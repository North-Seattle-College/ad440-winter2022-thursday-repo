export default function InputBox({ feedback, setFeedback, setShow }) {
  return (
    <div className="input-main">
      <div className="page-header">
        As you write down your comments to give feedback to students, you will
        receive relevant coaching messages according to your feedback to improve
        it.
      </div>
      <h3 className="input-header">Comment</h3>
      <input
        type="text"
        className="user-input"
        value={feedback}
        onChange={e => setFeedback(e.target.value)}
        onFocus={() => setShow(false)}
      />
    </div>
  );
}
