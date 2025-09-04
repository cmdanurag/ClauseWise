import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api/v1";

export const uploadDocument = async (content: string) => {
  const response = await axios.post(`${API_BASE}/documents/upload`, { content });
  return response.data;
};

export const uploadDocumentFile = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE}/documents/upload-file`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};
