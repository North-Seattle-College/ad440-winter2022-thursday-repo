import "./App.css";
import InputBox from "../InputBox/InputBox";
import ErrorBox from "../ErrorBox/ErrorBox";
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ClearBtn from "../ClearBtn/ClearBtn";
import SubmitBtn from "../SubmitBtn/SubmitBtn";

function App() {
  return (
    <div className="App">
      <InputBox />
      <SubmitBtn />
      <ClearBtn />
      <FeedbackBox />
      <ErrorBox />
    </div>
  );
}

export default App;