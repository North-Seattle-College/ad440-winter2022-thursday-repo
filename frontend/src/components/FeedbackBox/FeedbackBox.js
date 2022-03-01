// Task for David Nguyen
export default function FeedbackBox({ feedback }) {
  return (
    <div>
      <div className="analysis"></div>
      <div className="feedbackbox">
        <div className="feedback">{feedback}</div>
      </div>
    </div>
  );
}