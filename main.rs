use tokio::net::TcpListener;
use tokio::sync::mpsc;
use std::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("0.0.0.0:8080").await?;
    println!("Sandb0x-Xtract0r Worker Core active on port 8080");

    let (tx, mut rx) = mpsc::channel(32);

    tokio::spawn(async move {
        while let Some(sample_path) = rx.recv().await {
            println!("Executing detonation sequence for: {}", sample_path);
            let _ = Command::new("firecracker")
                .arg("--config-file")
                .arg(format!("/etc/sandb0x/{}.json", sample_path))
                .status();
        }
    });

    Ok(())
}
