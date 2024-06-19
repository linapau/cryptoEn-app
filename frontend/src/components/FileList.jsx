/*import React, { useState, useEffect } from 'react';

function FileList({ refresh }) {
    const [files, setFiles] = useState([]);
    const [error, setError] = useState(null);

    const fetchFiles = async () => {
        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}list_files/`);
            const result = await response.json();
            if (response.ok) {
                setFiles(result.files);
            } else {
                throw new Error(result.error || 'Error fetching files');
            }
        } catch (error) {
            setError(error.message);
        }
    };

    useEffect(() => {
        fetchFiles();
    }, [refresh]);

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
        <div>
            <h2>Uploaded Files</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <table>
                <thead>
                    <tr>
                        <th>File Name</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {files.map((file) => (
                        <tr key={file.name}>
                            <td>{file.name}</td>
                            <td>
                                <button onClick={() => handleDownload(file.name)}>Download</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default FileList;*/

import React, { useState, useEffect } from 'react';

function FileList() {
    const [files, setFiles] = useState([]);
    const [error, setError] = useState(null);

    const fetchFiles = async () => {
        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}list_files/`);
            const result = await response.json();
            if (response.ok) {
                setFiles(result.files);
            } else {
                throw new Error(result.error || 'Error fetching files');
            }
        } catch (error) {
            setError(error.message);
        }
    };

    useEffect(() => {
        fetchFiles();
    }, []);

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
        <div>
            <h2>Uploaded Files</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {files.map((file) => (
                    <li key={file.name}>
                        {file.name} <button class="basicBtn" id="btndown" onClick={() => handleDownload(file.name)}>Download</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default FileList;
