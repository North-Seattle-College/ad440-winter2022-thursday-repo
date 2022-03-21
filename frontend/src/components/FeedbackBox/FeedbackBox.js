export default function FeedbackBox({ AIfeedback }) {
  return (
    <div>
      <h4>Comment Feedback:</h4>
      <div className="feedback">
        {AIfeedback.map(
          ({ emotion, isQuestion, sentence, sentiment, sentimentScore }) => (
            <p key={sentence}>
              💡
              <br />
              Sentence: {`"${sentence}"`} <br />
              Is a question: {isQuestion ? "yes" : "no"} <br />
              Emotion: {emotion} <br />
              Sentiment: {sentiment} <br />
              Sentiment Score: {sentimentScore} <br />
            </p>
          ),
        )}
      </div>
    </div>
  );
}
