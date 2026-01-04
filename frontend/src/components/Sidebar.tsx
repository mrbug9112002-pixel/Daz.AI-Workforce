'use client';

import { motion } from 'framer-motion';
import { History, MessageSquare, ChevronRight } from 'lucide-react';

interface HistoryItem {
    prompt: string;
    agent: string;
    timestamp: Date;
}

interface SidebarProps {
    history: HistoryItem[];
}

export default function Sidebar({ history }: SidebarProps) {
    return (
        <div className="w-64 h-screen bg-gray-900/80 border-r border-white/10 hidden md:flex flex-col fixed left-0 top-0 backdrop-blur-md">
            <div className="p-6 border-b border-white/5">
                <h2 className="flex items-center gap-2 text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">
                    <History className="w-5 h-5 text-blue-400" />
                    History
                </h2>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {history.length === 0 ? (
                    <div className="text-gray-500 text-sm text-center mt-10 italic">
                        No tasks yet.
                    </div>
                ) : (
                    history.map((item, index) => (
                        <motion.div
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            key={index}
                            className="p-3 rounded-lg bg-gray-800/50 hover:bg-gray-800 transition-colors cursor-pointer group border border-transparent hover:border-white/5"
                        >
                            <div className="flex items-center gap-2 mb-1">
                                <MessageSquare className="w-3 h-3 text-gray-400" />
                                <span className="text-xs text-blue-400 font-mono">{item.agent}</span>
                            </div>
                            <p className="text-sm text-gray-300 line-clamp-2">{item.prompt}</p>
                        </motion.div>
                    ))
                )}
            </div>
        </div>
    );
}
