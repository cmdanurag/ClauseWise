import React, { type ChangeEvent } from "react";

interface DocumentUploaderProps {
  onFileUpload: (file: File) => void;
}

const DocumentUploader: React.FC<DocumentUploaderProps> = ({ onFileUpload }) => {
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      onFileUpload(e.target.files[0]);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center w-full max-w-md">
      <label
        htmlFor="file-upload"
        className="cursor-pointer px-6 py-4 border-2 border-dashed border-gray-400 rounded-lg text-center hover:border-blue-500 transition-colors w-full"
      >
        Click or drag a document to upload
      </label>
      <input
        id="file-upload"
        type="file"
        className="hidden"
        onChange={handleChange}
        accept=".pdf,.doc,.docx,.txt"
      />
    </div>
  );
};

export default DocumentUploader;
