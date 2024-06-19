import React, { useState, useRef } from 'react';
import './../App.css';

function FileUpload({ onUpload }) {
    const [file, setFile] = useState(null);
    const [error, setError] = useState(null);
    const fileInputRef = useRef();

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}upload_file/`, {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();
            if (response.ok) {
                onUpload(result.file_name);
            } else {
                throw new Error(result.error || 'Error uploading file');
            }
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="file"
                ref={fileInputRef}
                className="hidden-file-input"
                onChange={handleFileChange}
            />
            <button
                type="button"
                className="custom-upload-button"
                onClick={() => fileInputRef.current.click()}
            >
                Choose File
            </button>
            {file && <span>{file.name}</span>}
            <button type="submit" className="custom-upload-button">
                Upload
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
    );
}

export default FileUpload;
