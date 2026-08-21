use serde::{Deserialize, Serialize};

/// Defines the specific type of threat analysis the LLM should perform.
#[derive(Debug, Serialize, Deserialize)]
pub enum AnalysisTask {
    CodeReview,
    MalwareBehavior,
    NetworkAnomaly,
}

/// A common interface for any LLM provider integrated into the engine.
pub trait LlmProvider {
    fn analyze(&self, task: AnalysisTask, artifact_data: &str) -> String;
}

/// Example implementation for a specific bot (e.g., OpenAI).
pub struct OpenAiBot {
    pub api_key: String,
    pub model: String,
}

impl OpenAiBot {
    pub fn new(api_key: String) -> Self {
        Self {
            api_key,
            model: String::from("gpt-4-turbo"),
        }
    }
}

impl LlmProvider for OpenAiBot {
    fn analyze(&self, task: AnalysisTask, _artifact_data: &str) -> String {
        // Placeholder for the actual async HTTP request to the LLM's API
        println!("Sending {:?} task to {} model...", task, self.model);
        String::from("Analysis complete: No immediate threats detected.")
    }
}
