import { useState } from 'react';
import UploadForm from './components/UploadForm';
import ReportViewer from './components/ReportViewer';
import { Activity } from 'lucide-react';

function App() {
  const [activeTaskId, setActiveTaskId] = useState(null);

  return (
    <div className="max-w-5xl mx-auto p-6">
      <header className="flex items-center justify-between py-6 mb-8 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-blue-500/10 rounded-lg border border-blue-500/20">
            <Activity className="text-sandbox-accent h-8 w-8" />
          </div>
          <div>
            <h1 className="text-3xl font-black tracking-tight">S@ndb0x-Xtract0r</h1>
            <p className="text-slate-400 text-sm mt-1">Multi-LLM Automated Telemetry Engine</p>
          </div>
        </div>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-[350px_1fr] gap-6">
        <aside>
          <UploadForm onTaskCreated={setActiveTaskId} />
        </aside>
        
        <section>
          {activeTaskId ? (
            <ReportViewer taskId={activeTaskId} />
          ) : (
            <div className="h-full flex flex-col items-center justify-center text-slate-500 border-2 border-dashed border-slate-700 rounded-xl p-12 bg-slate-800/30">
              <Activity className="h-12 w-12 mb-4 opacity-50" />
              <p>Submit a payload to view real-time analysis.</p>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
