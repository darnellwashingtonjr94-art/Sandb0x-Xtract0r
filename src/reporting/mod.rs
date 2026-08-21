use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct TelemetryReport {
    pub artifact_id: String,
    pub malicious_confidence: f32,
    pub network_traces_captured: usize,
}

pub fn generate_report(artifact_id: &str) -> TelemetryReport {
    TelemetryReport {
        artifact_id: artifact_id.to_string(),
        malicious_confidence: 0.0,
        network_traces_captured: 0,
    }
}
