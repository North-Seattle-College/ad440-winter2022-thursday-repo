export default function InputBox({ input, setInput }) {
  return (
    <div className="input-main">
      <div className="page-header">
        Want to bring your feedback to the next level? Enter one of your comments below and click submit! You will receive relevant coaching tips and advice on how to improve.
      </div>
      <h4 className="input-header">Comment</h4>
      <input
        type="text"
        className="user-input"
        value={input}
        onChange={e => setInput(e.target.value)}
      />
    </div>
  );
}
