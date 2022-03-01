import { usePromiseTracker } from "react-promise-tracker";
import ReactLoading from 'react-loading';

export default function FeedbackBox({ AIfeedback }) {
  const { promiseInProgress } = usePromiseTracker();

  const LoadingIndicator = () => {
    return (
      <div className='loadingIcon'>
        <ReactLoading type={'spin'} color={'#00807F'} height={'9%'} width={'9%'} />
      </div>
    );
  }

  return promiseInProgress ? <LoadingIndicator /> : <div className="feedback">"{AIfeedback}"</div>;
}