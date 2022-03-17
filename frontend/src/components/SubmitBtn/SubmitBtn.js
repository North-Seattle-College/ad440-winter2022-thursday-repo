import { trackPromise } from "react-promise-tracker";

export default function SubmitBtn({ input, setShow, setAIfeedback }) {
  const url = "https://api.seredium.com/v1/feedback";

  const handleSubmit = evt => {
    evt.preventDefault();
    trackPromise(
      fetch(url, {
        method: "POST",
        body: JSON.stringify({ input }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => {
          if (response.ok) {
            setAPIResponse(response.status);
            return response.json();
          }  
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
