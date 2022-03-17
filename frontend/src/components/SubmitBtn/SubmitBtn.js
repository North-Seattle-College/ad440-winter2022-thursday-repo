import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ input, setAIfeedback, setAPIResponse }) {
  const url = "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => {
          setAPIResponse(response.status);
        })
        .then(feedback => setAIfeedback(feedback))
        .catch(e => console.error(e)));
  };

  return (
    <div>
      <button disabled={!input} onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
}
