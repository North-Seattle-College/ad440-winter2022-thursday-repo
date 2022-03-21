import ReactLoading from "react-loading";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ErrorBox from "../ErrorBox/ErrorBox";

export default function ResponseBox({ AIfeedback, APIResponse, isLoading }) {
  const LoadingIndicator = () => {
    return (
      <div className="loadingIcon">
        <ReactLoading
          type={"spin"}
          color={"#00807F"}
          height={"9%"}
          width={"9%"}
        />
      </div>
    );
  };

  if (isLoading) {
    // Loading
    return <LoadingIndicator />;
  } else if (!APIResponse) {
    // Firest page load (default)
    return <div></div>;
  } else if (APIResponse === 200) {
    // Response good
    return <FeedbackBox AIfeedback={AIfeedback} />;
  } else if (APIResponse === 400) {
    // user input was invalid
    const error400 = `${APIResponse}: Make sure there are no double quotes in your input.`;
    return <ErrorBox APIResponse={error400} />;
  } else {
    // Any other error
    return <ErrorBox APIResponse={APIResponse} />;
  }
}
