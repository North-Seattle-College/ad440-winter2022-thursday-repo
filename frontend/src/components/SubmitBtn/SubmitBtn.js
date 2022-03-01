import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ feedback, setShow }) {
  const url = "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      fetch(url, {
        method: "POST",
        body: JSON.stringify({ feedback }), // convert to JSON
        headers: { "Content-Type": "application/json" }, // get the response data in that format
      })
        .then(response => response.json())
        .then(feedbackData => console.log(feedbackData))
        .catch(e => console.error("Error indicated:", e)));
    setShow(true);
  };

  return (
    <div>
      <button disabled={!feedback} onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
}
