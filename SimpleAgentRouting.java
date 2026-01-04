import java.util.*;

public class SimpleAgentRouting {

    // 1. Define the Manager Agent (The Brain)
    static class ManagerAgent {
        
        public String processTask(String prompt) {
            String promptLower = prompt.toLowerCase();
            
            // 2. Define Keywords & Weights (Same as Python dictionary)
            Map<String, Integer> claudeKeywords = new HashMap<>();
            claudeKeywords.put("code", 10);
            claudeKeywords.put("python", 10);
            claudeKeywords.put("java", 10);
            claudeKeywords.put("fix", 5);
            claudeKeywords.put("debug", 8);

            Map<String, Integer> deepSeekKeywords = new HashMap<>();
            deepSeekKeywords.put("analyze", 5);
            deepSeekKeywords.put("logic", 8);
            deepSeekKeywords.put("math", 10);
            deepSeekKeywords.put("why", 3);

            Map<String, Integer> geminiKeywords = new HashMap<>();
            geminiKeywords.put("story", 10);
            geminiKeywords.put("creative", 10);
            geminiKeywords.put("write", 5);
            geminiKeywords.put("idea", 5);

            // 3. Calculate Scores
            int claudeScore = calculateScore(promptLower, claudeKeywords);
            int deepSeekScore = calculateScore(promptLower, deepSeekKeywords);
            int geminiScore = calculateScore(promptLower, geminiKeywords);

            System.out.println("Scores -> Claude: " + claudeScore + ", DeepSeek: " + deepSeekScore + ", Gemini: " + geminiScore);

            // 4. Determine Winner
            String winner = "Gemini (General Assistant)"; // Default fallback
            int maxScore = 0;

            if (claudeScore > maxScore) {
                winner = "Claude";
                maxScore = claudeScore;
            }
            if (deepSeekScore > maxScore) {
                winner = "DeepSeek";
                maxScore = deepSeekScore;
            }
            if (geminiScore > maxScore) {
                winner = "Gemini";
                maxScore = geminiScore;
            }

            // 5. Routing Logic (The Anti-Gravity Logic)
            if (winner.equals("Claude")) {
                // COST OPTIMIZATION OVERRIDE (Phase 6 Logic)
                // Instead of calling the expensive Claude API, we route to Gemini with instructions.
                return "Gemini (Acting as Claude) executing: [SYSTEM: Be an Expert Developer] " + prompt;
            } else if (winner.equals("DeepSeek")) {
                return "DeepSeek Agent executing: " + prompt;
            } else {
                return "Gemini Agent executing: " + prompt;
            }
        }

        // Helper to sum up weights
        private int calculateScore(String text, Map<String, Integer> keywords) {
            int score = 0;
            for (Map.Entry<String, Integer> entry : keywords.entrySet()) {
                if (text.contains(entry.getKey())) {
                    score += entry.getValue();
                }
            }
            return score;
        }
    }

    // Main method to test it (like python main.py)
    public static void main(String[] args) {
        ManagerAgent manager = new ManagerAgent();

        System.out.println("--- Test 1: Coding Task ---");
        String response1 = manager.processTask("Write a Java function to debug code");
        System.out.println("Result: " + response1);
        System.out.println();

        System.out.println("--- Test 2: Creative Task ---");
        String response2 = manager.processTask("Write a creative story about gravity");
        System.out.println("Result: " + response2);
    }
}
