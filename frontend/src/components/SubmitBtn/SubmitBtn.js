import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ input, setShow, setAIfeedback }) {
  const url = "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }), // convert to JSON
        headers: { "Content-Type": "application/json" }, // get the response data in that format
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
        }
          throw new Error("Request Failed");
        })
        .then(feedback => setAIfeedback(feedback))
        .catch(e => console.error(e)));
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
