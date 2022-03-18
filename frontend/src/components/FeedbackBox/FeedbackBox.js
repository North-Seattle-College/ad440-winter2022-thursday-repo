export default function FeedbackBox({ AIfeedback }) {
  return (
    <div className="feedback">
      💡
      {AIfeedback && (
        <div>
          {AIfeedback.map((comment, index) => (
            <div key={index}>
              <br />
              Title: {comment.title} | Description: {comment.description}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
