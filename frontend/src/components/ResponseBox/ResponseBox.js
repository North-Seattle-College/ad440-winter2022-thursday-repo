import { usePromiseTracker } from "react-promise-tracker";
import ReactLoading from 'react-loading';
import FeedbackBox from "../FeedbackBox/FeedbackBox";
import ErrorBox from "../ErrorBox/ErrorBox";

export default function ResponseBox({ AIfeedback, APIResponse }) {
    const { promiseInProgress } = usePromiseTracker();

    const LoadingIndicator = () => {
        return (
            <div className='loadingIcon'>
                <ReactLoading type={'spin'} color={'#00807F'} height={'9%'} width={'9%'} />
            </div>
        );
    }

    if (promiseInProgress) {
        // Loading
        return <LoadingIndicator />
    } else if (!APIResponse) {
        // Firest page load (default)
        return <div></div>
    } else if (APIResponse === 200) {
        // Response good
        return <FeedbackBox AIfeedback={AIfeedback} />
    } else {
        // Anything but a code 200
        return <ErrorBox APIResponse={APIResponse} />
    }
}