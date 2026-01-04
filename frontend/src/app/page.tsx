'use client';

import { useState } from 'react';
import InputForm from '@/components/InputForm';
import ResultView from '@/components/ResultView';
import Sidebar from '@/components/Sidebar';
import { executeTask, TaskResponse } from '@/lib/api';
import { Lock, ArrowRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface HistoryItem {
  prompt: string;
  agent: string;
  timestamp: Date;
}

export default function Home() {
  const [result, setResult] = useState<TaskResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [accessCode, setAccessCode] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [history, setHistory] = useState<HistoryItem[]>([]);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (accessCode.trim()) {
      setIsAuthenticated(true);
    }
  };

  const handleTaskSubmit = async (prompt: string) => {
    setIsLoading(true);
    setResult(null);

    // Pass accessCode to the API
    const response = await executeTask(prompt, accessCode);
    setResult(response);

    if (response.status === 'success') {
      const newItem: HistoryItem = {
        prompt: prompt,
        agent: response.assigned_agent,
        timestamp: new Date()
      };
      // Add to history (prepend)
      setHistory(prev => [newItem, ...prev]);
    }

    setIsLoading(false);
  };

  if (!isAuthenticated) {
    return (
      <main className="min-h-screen bg-[#0a0a0a] flex items-center justify-center p-4">
        <div className="w-full max-w-md bg-gray-900 border border-white/10 p-8 rounded-2xl shadow-2xl">
          <div className="flex justify-center mb-6">
            <div className="p-4 bg-gray-800 rounded-full">
              <Lock className="w-8 h-8 text-blue-400" />
            </div>
          </div>
          <h2 className="text-2xl font-bold text-center text-white mb-2">Access Restricted</h2>
          <p className="text-gray-400 text-center mb-6">Please enter your access code to verify you are authorized to manage this AI workforce.</p>

          <form onSubmit={handleLogin} className="space-y-4">
            <input
              type="password"
              className="w-full bg-gray-800 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter Access Code"
              value={accessCode}
              onChange={(e) => setAccessCode(e.target.value)}
            />
            <button
              type="submit"
              disabled={!accessCode.trim()}
              className="w-full bg-blue-600 hover:bg-blue-500 text-white font-medium py-3 rounded-lg transition-colors flex items-center justify-center gap-2"
            >
              Enter Platform <ArrowRight className="w-4 h-4" />
            </button>
          </form>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-[#0a0a0a] text-white selection:bg-blue-500/30 flex">

      {/* Sidebar */}
      <Sidebar history={history} />

      {/* Main Content */}
      <div className="flex-1 md:ml-64 relative min-h-screen">
        {/* Background Gradients */}
        <div className="fixed inset-0 z-0 overflow-hidden pointer-events-none">
          <div className="absolute top-[-10%] left-[20%] w-[40%] h-[40%] bg-blue-600/10 rounded-full blur-[120px]" />
          <div className="absolute bottom-[-10%] right-[0%] w-[40%] h-[40%] bg-purple-600/10 rounded-full blur-[120px]" />
        </div>

        <div className="relative z-10 container mx-auto px-4 py-20 flex flex-col items-center justify-center min-h-screen">

          {/* Header */}
          <div className="text-center mb-12 space-y-4">
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-400 to-white">
              Daz.AI-Workforce
            </h1>
            <p className="text-xl text-gray-400 max-w-2xl mx-auto">
              Authorized Session Active. Ready to deploy agents.
            </p>
          </div>

          {/* Interaction Area */}
          <div className="w-full space-y-8">
            <InputForm onSubmit={handleTaskSubmit} isLoading={isLoading} />

            <AnimatePresence mode='wait'>
              {result && <ResultView key={result.result} result={result} />}
            </AnimatePresence>
          </div>

        </div>
      </div>
    </main>
  );
}
