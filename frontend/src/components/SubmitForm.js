import React, { useState } from 'react';
import axios from 'axios';

function SubmitForm() {
  const [repoUrl, setRepoUrl] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.post('http://localhost:5000/test_repo', { repo_url: repoUrl });
    setResult(response.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          placeholder="Enter GitHub Repo URL"
        />
        <button type="submit">Submit</button>
      </form>
      {result && (
        <div>
          <h2>Test Result: {result.status}</h2>
          <pre>{JSON.stringify(result.details, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default SubmitForm;
