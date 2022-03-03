export default function ClearBtn({ setInput, setShow }) {
  const handleSubmit = (evt) => {
    evt.preventDefault();
    setShow(false);
    setInput('')
  }
  return (
    <button onClick={handleSubmit}>Clear</button>
  );
}
