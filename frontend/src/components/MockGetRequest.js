import React from "react";

import { useState } from "react";

function MockGetRequest() {
  const [reports, setReport] = useState(null);
  const url =
    "https://9u4xt4nqr1.execute-api.us-west-2.amazonaws.com/default/test";

  // A GET request using fetch() to fetch a data from the URL address
  // Fetch data by clicking on a button
  const fetchData = () => {
    fetch(url, { method: "GET" })
      .then(res => res.json())
      .then(data => setReport(data));
  };

  return (
    <div>
      <h2>GET Request</h2>
      <button onClick={fetchData}>Get Data</button>

      {/* display reports from the API */}
      {reports && (
        <div>
          {/* looping */}
          {reports.map((report, index) => (
            <div key={index}>
              <br />
              Title: {report.title} | Description: {report.description}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
export default MockGetRequest;
