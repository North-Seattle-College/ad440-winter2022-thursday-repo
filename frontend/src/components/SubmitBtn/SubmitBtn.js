// Task for Payam Taherirostami
export default function SubmitBtn({ feedback, setFeedback, setShow }) {
  const handleSubmit = (evt) => {
    evt.preventDefault();
    setShow(true);
  }
  return (
    <div>
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}