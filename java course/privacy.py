import React, { useState } from "react";
import "./App.css";

const App = () => {
  const [file, setFile] = useState(null);
  const [encryption, setEncryption] = useState("homomorphic");
  const [trustedEntities, setTrustedEntities] = useState([]);
  const [availableEntities] = useState([
    "Hospital A",
    "Bank B",
    "Insurance C",
  ]);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleEncryptionChange = (event) => {
    setEncryption(event.target.value);
  };

  const handleEntitySelection = (entity) => {
    if (!trustedEntities.includes(entity)) {
      setTrustedEntities([...trustedEntities, entity]);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file || trustedEntities.length === 0) {
      alert("Please upload a file and select at least one trusted entity.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("encryption", encryption);
    formData.append("trustedEntities", JSON.stringify(trustedEntities));

    try {
      const response = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      if (response.ok) {
        alert("File shared successfully!");
      } else {
        alert(Error, $(data,message));
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("An error occurred while sharing the file.");
    }
  };

  return (
    <div className="App">
      <h1>Privacy-Preserving Data Sharing Platform</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="fileInput">Upload Sensitive Data:</label>
          <input
            type="file"
            id="fileInput"
            accept=".pdf,.doc,.docx,.xlsx,.csv"
            onChange={handleFileChange}
          />
        </div>

        <div>
          <label htmlFor="encryptionSelect">Select Encryption Technique:</label>
          <select
            id="encryptionSelect"
            value={encryption}
            onChange={handleEncryptionChange}
          >
            <option value="homomorphic">Homomorphic Encryption</option>
            <option value="differential">Differential Privacy</option>
          </select>
        </div>

        <div>
          <h3>Select Trusted Entities:</h3>
          <ul>
            {availableEntities.map((entity) => (
              <li key={entity}>
                <button
                  type="button"
                  onClick={() => handleEntitySelection(entity)}
                >
                  {entity}
                </button>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h4>Selected Trusted Entities:</h4>
          <ul>
            {trustedEntities.map((entity, index) => (
              <li key={index}>{entity}</li>
            ))}
          </ul>
        </div>

        <button type="submit">Share Securely</button>
      </form>
    </div>
  );
};

export default App;