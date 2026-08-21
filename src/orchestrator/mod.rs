pub struct Orchestrator {
    pub is_running: bool,
}

impl Orchestrator {
    pub fn new() -> Self {
        Self { is_running: false }
    }

    pub fn start_pipeline(&mut self) {
        self.is_running = true;
        println!("Orchestrator pipeline started...");
    }
}
