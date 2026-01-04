import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Default FastAPI port

export interface TaskResponse {
    assigned_agent: string;
    result: string;
    status: string;
}

export const executeTask = async (prompt: string, accessCode: string): Promise<TaskResponse> => {
    try {
        const response = await axios.post(
            `${API_URL}/execute`,
            { prompt },
            { headers: { 'x-access-code': accessCode } }
        );
        return response.data;
    } catch (error: any) {
        console.error("Error executing task:", error);
        if (error.response && error.response.status === 401) {
            return {
                assigned_agent: "System",
                result: "⛔ Access Denied: Invalid Access Code.",
                status: "error"
            };
        }
        return {
            assigned_agent: "System",
            result: "Error: Failed to connect to the Multi-Agent Backend. Is it running?",
            status: "error"
        };
    }
};
