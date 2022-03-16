import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ input, setShow, setAIfeedback }) {
  const url =
    "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      /*  fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }), // convert to JSON
        headers: { "Content-Type": "application/json" }, // get the response data in that format
      }) */
      fetch(url)
        .then(response => response.json())
        .then(feedback => setAIfeedback(feedback))
        .catch(e => console.error("Error indicated:", e)),
    );
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
