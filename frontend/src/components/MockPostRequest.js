import React from "react";
import { useState } from "react";

function MockPostRequest() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [body, setBody] = useState("");

  const handleSubmit = e => {
    e.preventDefault(); // prevent browser from reloading and get the data on time

    const data = { name, email, body };
    const url = "https://jsonplaceholder.typicode.com/comments";

    // A POST request using fetch to add data -shown on console-
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" }, // we want to get the response data in that format
      body: JSON.stringify(data), // defines the body data that we want to send to the server -- convert to JSON
    };
    fetch(url, requestOptions)
      .then(response => response.json())
      .then(res => console.log(res)); // response is shown on the console window
  };

  return (
    <div>
      <h2>POST Request</h2>
      <fieldset
        style={{
          width: "30%",
          marginLeft: "35%",
          borderColor: "blue",
          padding: 20,
        }}>
        <form>
          <input
            type="text"
            name="name"
            placeholder="Name"
            onChange={e => setName(e.target.value)}
          />{" "}
          <input
            type="text"
            name="email"
            placeholder="Email"
            onChange={e => setEmail(e.target.value)}
          />
          <br />
          <br />
          <textarea
            name="comment"
            placeholder="Please add your comments"
            cols="24"
            rows="7"
            onChange={e => setBody(e.target.value)}></textarea>
          <br />
          <button type="submit" onClick={handleSubmit}>
            Create Post
          </button>
        </form>
      </fieldset>
    </div>
  );
}

export default MockPostRequest;
