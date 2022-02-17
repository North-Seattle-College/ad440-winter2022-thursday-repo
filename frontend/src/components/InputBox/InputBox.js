export default function InputBox({ feedback, setFeedback, setShow }) {
  return (
    <div className="input-main">
      <div className="page-header">
        As you write down your comments to give feedback to students, you will
        receive relevant coaching messages according to your feedback to improve
        it.
      </div>
      <h2 className="input-header">Teacher Comment</h2>
      <input
        type="text"
        className="user-input"
        placeholder="Your comment goes here..."
        value={feedback}
        onChange={e => setFeedback(e.target.value)}
        onFocus={() => setShow(false)}
      />
    </div>
  );
}
