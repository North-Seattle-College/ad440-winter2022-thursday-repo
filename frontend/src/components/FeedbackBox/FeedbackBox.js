import "./Feedback.css"

export default function FeedbackBox({feedback , showResults}) {
    return (
    <div>
            <div className="analysis"><h2>Analysis</h2></div>
            <div className="feedbackbox">
            <div className="feedback">{ showResults ? feedback : null }</div>
        </div>
    </div>
    );
}