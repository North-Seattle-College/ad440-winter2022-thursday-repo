export default function SubmitBtn({ input, setAPIResponse, setAIfeedback }) {
  const url =
    "https://3s7yrqtdmb.execute-api.us-west-2.amazonaws.com/demo/splitSentences";

  const handleSubmit = evt => {
    evt.preventDefault();
    fetch(url, {
      method: "POST",
      body: input,
      headers: { "Content-Type": "application/json" },
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        setAPIResponse(response.status);
      })
      .then(feedback => {
        console.log(feedback.result.sentences);
        setAIfeedback(feedback); // Output the results - converted to JSON format
      });
  };

  return (
    <div>
      <button disabled={!input} onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
}
