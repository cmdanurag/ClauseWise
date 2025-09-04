import React, { useState } from 'react';
import './DocumentUpload.css';

const DocumentUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [documentType, setDocumentType] = useState('');
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      // Validate file type
      const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
      if (!validTypes.includes(selectedFile.type)) {
        setError('Invalid file type. Please upload a PDF, DOCX, or TXT file.');
        setFile(null);
        return;
      }
      
      // Validate file size (max 10MB)
      if (selectedFile.size > 10 * 1024 * 1024) {
        setError('File size exceeds 10MB limit.');
        setFile(null);
        return;
      }
      
      setFile(selectedFile);
      setError('');
    }
  };

  const handleDocumentTypeChange = (event) => {
    setDocumentType(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!file) {
      setError('Please select a file to upload.');
      return;
    }
    
    if (!documentType) {
      setError('Please select a document type.');
      return;
    }
    
    setIsUploading(true);
    setError('');
    
    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('document_type', documentType);
      
      const response = await fetch('/api/v1/documents/analyze', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        throw new Error(`Upload failed: ${response.statusText}`);
      }
      
      const result = await response.json();
      onUploadSuccess(result);
    } catch (err) {
      setError(`Upload failed: ${err.message}`);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="document-upload">
      <h2>Upload Legal Document</h2>
      <p>Upload a legal document (PDF, DOCX, or TXT) for AI-powered analysis.</p>
      
      <form onSubmit={handleSubmit} className="upload-form">
        <div className="form-group">
          <label htmlFor="file">Select Document:</label>
          <input 
            type="file" 
            id="file" 
            accept=".pdf,.docx,.txt" 
            onChange={handleFileChange} 
            disabled={isUploading}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="documentType">Document Type:</label>
          <select 
            id="documentType" 
            value={documentType} 
            onChange={handleDocumentTypeChange} 
            disabled={isUploading}
          >
            <option value="">Select document type</option>
            <option value="rental_agreement">Rental Agreement</option>
            <option value="loan_contract">Loan Contract</option>
            <option value="terms_of_service">Terms of Service</option>
            <option value="employment_contract">Employment Contract</option>
            <option value="general_contract">General Contract</option>
          </select>
        </div>
        
        {error && <div className="error-message">{error}</div>}
        
        <button 
          type="submit" 
          disabled={isUploading || !file || !documentType}
          className="upload-button"
        >
          {isUploading ? 'Analyzing...' : 'Analyze Document'}
        </button>
      </form>
      
      {file && (
        <div className="file-info">
          <h3>Selected File:</h3>
          <p>Name: {file.name}</p>
          <p>Size: {(file.size / 1024 / 1024).toFixed(2)} MB</p>
          <p>Type: {file.type}</p>
        </div>
      )}
    </div>
  );
};

export default DocumentUpload;