#[derive(Debug)]
pub struct SandboxEnvironment {
    pub id: String,
    pub is_isolated: bool,
}

impl SandboxEnvironment {
    pub fn create_new(id: &str) -> Self {
        Self {
            id: id.to_string(),
            is_isolated: true,
        }
    }

    pub fn teardown(&self) {
        println!("Tearing down sandbox: {}", self.id);
    }
}
