'use client';

import { motion } from 'framer-motion';
import { Bot, Sparkles, Code2, BrainCircuit } from 'lucide-react';

interface ResultViewProps {
    result: {
        assigned_agent: string;
        result: string;
    } | null;
}

export default function ResultView({ result }: ResultViewProps) {
    if (!result) return null;

    const getAgentIcon = (agentName: string) => {
        if (agentName.includes("Claude")) return <Code2 className="w-6 h-6 text-orange-400" />;
        if (agentName.includes("Gemini")) return <Sparkles className="w-6 h-6 text-blue-400" />;
        if (agentName.includes("DeepSeek")) return <BrainCircuit className="w-6 h-6 text-green-400" />;
        return <Bot className="w-6 h-6 text-gray-400" />;
    };

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="w-full max-w-2xl mx-auto mt-8"
        >
            <div className="bg-gray-800/50 backdrop-blur-sm border border-white/10 rounded-xl overflow-hidden shadow-2xl">
                <div className="px-6 py-4 bg-gray-900/50 border-b border-white/5 flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                        <div className="p-2 bg-gray-800 rounded-lg">
                            {getAgentIcon(result.assigned_agent)}
                        </div>
                        <div>
                            <h3 className="text-white font-medium">Task Completed</h3>
                            <p className="text-sm text-gray-400">Handled by: <span className="text-blue-400 font-semibold">{result.assigned_agent}</span></p>
                        </div>
                    </div>
                </div>
                <div className="p-6">
                    <div className="prose prose-invert max-w-none">
                        <p className="whitespace-pre-wrap text-gray-300 leading-relaxed">
                            {result.result}
                        </p>
                    </div>
                </div>
            </div>
        </motion.div>
    );
}
