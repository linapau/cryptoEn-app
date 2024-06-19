/*
import { useState, useEffect } from 'react'
import './App.css'

function App() {

  const [data, setData] = useState([])

  useEffect(() => {
    async function fetchData() {
      console.log(import.meta.env.VITE_API_URL)
      try {
        const response = await fetch('${import.meta.env.VITE_API_URL}');
        if (!response.ok) {
          throw new Error("Bad response");
        }

        const result = await response.json();
        console.log(result)
        setData(result)
      } catch (error) {
        console.log("Error while fetching data: ", error)
      }
    }
    fetchData();

  }, []);

  return (
    <>
      <h1>Siema Świecie</h1>
      {data.length > 0 ? (
        <ul>
          {data.map((item, index) => (
            <li key={index}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>No data available</p>
      )}
    </>
  );
}

export default App


import { useState } from 'react';
import './App.css';

function App() {
  const [error, setError] = useState(null);

  const handleDownload = async (fileName) => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}download_file/${fileName}`, {
        method: 'GET',
      });

      if (response.headers.get('content-type') === 'application/json') {
        const result = await response.json();
        if (!response.ok) {
          throw new Error(result.error || 'Error downloading file');
        }
      } else {
        // Assuming the response is a file
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
      }
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <>
      <h1>File Download</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={() => handleDownload('doggo.jpg')}>Download File</button>
    </>
  );
}

export default App;

*/



import { useState } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import FileList from './components/FileList';

function App() {
  const [uploadTrigger, setUploadTrigger] = useState(false);

  const handleUpload = (fileName) => {
    setUploadTrigger(!uploadTrigger); // Toggle state to trigger re-fetch in FileList
  };

  return (
    <>
      <h1>Upload file</h1>
      <FileUpload onUpload={handleUpload} />
      <FileList key={uploadTrigger} /> {/* Re-fetch files when uploadTrigger changes */}
    </>
  );
}

export default App;

