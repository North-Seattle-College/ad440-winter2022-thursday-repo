import "./Feedback.css"

export default function FeedbackBox({feedback}) {
    return (
    <div>
            <div className="analysis"><h2>AI Feedback</h2></div>
            <div className="feedbackbox">
            <div className="feedback">{feedback}</div>
        </div>
    </div>
    );
}