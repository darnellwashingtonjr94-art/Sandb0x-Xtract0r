use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct EngineConfig {
    pub max_detonation_time: u64,
    pub strict_isolation: bool,
}

pub fn initialize_core() {
    println!("Core engine initialized.");
}
