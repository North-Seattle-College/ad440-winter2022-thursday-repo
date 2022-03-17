import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ input, setShow, setAIfeedback }) {
  const url = "https://api.seredium.com/v1/feedback";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }), // convert to JSON
        headers: { "Content-Type": "application/json" }, // get the response data in that format
      })
        .then(response => response.json())
        .then(feedback => setAIfeedback(feedback))
        .catch(e => console.error("Error indicated:", e)));
    setShow(true);
  };

  return (
    <div>
      <button disabled={!input} onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
}
