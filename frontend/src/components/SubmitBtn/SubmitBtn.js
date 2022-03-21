export default function SubmitBtn({
  input,
  setAPIResponse,
  setAIfeedback,
  setIsLoading,
}) {
  const url = "https://api.seredium.com/v1/feedback/splitSentences";

  const handleSubmit = evt => {
    setIsLoading(true);
    evt.preventDefault();
    fetch(url, {
      method: "POST",
      body: `{"text": "${input}" }`,
      headers: { "Content-Type": "application/json" },
    })
      .then(response => {
        setAPIResponse(response.status);
        if (response.ok) {
          return response.json();
        }
        setIsLoading(false);
      })
      .then(feedback => {
        setAIfeedback(feedback.result.sentences);
        setIsLoading(false);
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
