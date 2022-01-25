import "./App.css";
import MockGetRequest from "./components/MockGetRequest";
import MockPostRequest from "./components/MockPostRequest";

function App() {
  return (
    <>
      <div className="App">
        <MockGetRequest />
        <hr
          style={{
            backgroundColor: "blue",
            height: 2,
            marginTop: "2%",
          }}
        />
        <MockPostRequest />
      </div>
    </>
  );
}

export default App;
