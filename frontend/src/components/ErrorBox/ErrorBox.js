export default function ErrorBox({ APIResponse }) {
  return (
    <div>
      <h4>Error:</h4>
      <div className="error">  ❌  "Request failed:" {APIResponse} </div>
    </div>
  );
}