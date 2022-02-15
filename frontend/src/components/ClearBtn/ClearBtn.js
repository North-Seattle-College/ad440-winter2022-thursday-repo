import './ClearBtn.css';
export default function ClearBtn({setFeedback, setShow}) {
  const handleSubmit = (evt) => {
    evt.preventDefault();
    setShow(false);
    setFeedback('')
  }
  return (
    <button onClick={handleSubmit}>Cancel</button>
  );
}
