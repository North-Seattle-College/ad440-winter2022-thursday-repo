export default function ClearBtn({ setInput }) {
  const handleSubmit = (evt) => {
    evt.preventDefault();
    setInput('')
  }
  return (
    <button onClick={handleSubmit}>Clear</button>
  );
}
