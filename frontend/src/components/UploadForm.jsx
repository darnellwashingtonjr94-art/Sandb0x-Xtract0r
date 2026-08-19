import { useState } from 'react';
import { submitSample } from '../api/client';
import { UploadCloud, ShieldAlert } from 'lucide-react';

export default function UploadForm({ onTaskCreated }) {
  const [file, setFile] = useState(null);
  const [platform, setPlatform] = useState('auto');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    setIsSubmitting(true);
    try {
      const data = await submitSample(file, platform);
      onTaskCreated(data.task_id);
    } catch (error) {
      console.error("Upload failed", error);
      alert("Failed to submit sample. Is the backend running?");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="bg-sandbox-card p-6 rounded-xl shadow-lg border border-slate-700">
      <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
        <ShieldAlert className="text-sandbox-accent" />
        New Sandbox Detonation
      </h2>
      <form onSubmit={handleUpload} className="flex flex-col gap-4">
        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])}
          className="file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-sandbox-accent file:text-white hover:file:bg-blue-600 bg-slate-800 text-slate-300 rounded-lg p-2"
          required
        />
        <select 
          value={platform} 
          onChange={(e) => setPlatform(e.target.value)}
          className="bg-slate-800 text-white p-3 rounded-lg border border-slate-700"
        >
          <option value="auto">Auto-Detect Header</option>
          <option value="windows">Windows 10</option>
          <option value="linux">Linux / ELF</option>
          <option value="android">Android APK</option>
          <option value="container">Docker / Script</option>
        </select>
        <button 
          type="submit" 
          disabled={isSubmitting || !file}
          className="bg-sandbox-accent hover:bg-blue-600 disabled:opacity-50 text-white font-bold py-3 px-4 rounded-lg flex items-center justify-center gap-2 transition-all"
        >
          <UploadCloud />
          {isSubmitting ? 'Detonating...' : 'Submit Payload'}
        </button>
      </form>
    </div>
  );
}
