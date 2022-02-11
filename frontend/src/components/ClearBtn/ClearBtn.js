import './ClearBtn.css';
export default function ClearBtn({setFeedback}) {
  return (
      <button onClick={() => setFeedback(() => "")}>Cancel</button>
  );
}
