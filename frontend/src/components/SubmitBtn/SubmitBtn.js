import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({
  input,
  setShow,
  setAPIResponse,
  setAIfeedback,
}) {
  const url =
    "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      /* fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }),
        headers: { "Content-Type": "application/json" },
      }) */
      fetch(url)
        .then(response => {
          if (response.ok) {
            return response.json();
          }
          setAPIResponse(response.status);
        })
        .then(feedback => setAIfeedback(feedback))
        .catch(e => console.error(e)),
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
