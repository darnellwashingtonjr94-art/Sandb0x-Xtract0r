import axios from 'axios';

const API_BASE = 'http://localhost:8000/api/v1';

export const submitSample = async (file, platform = 'auto') => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('platform', platform);

  const response = await axios.post(`${API_BASE}/submit`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const fetchReport = async (taskId) => {
  const response = await axios.get(`${API_BASE}/reports/${taskId}?format=md`, {
    responseType: 'text',
  });
  return response.data;
};
